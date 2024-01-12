import logging

import dotenv

dotenv.load_dotenv()

from grpc_reflection.v1alpha import reflection
import atexit
import asyncio
import grpc.aio

from .logger import get_logger
from .hardware import backend

logger = get_logger(__name__)


async def startup_event():
    logger.info("Starting up...")
    backend.start()
    logger.info("Startup complete")


def shutdown_event():
    logger.info("Shutting down...")
    backend.teardown_requested = True
    logger.info("Shutdown complete")


async def main():
    # set logger called "swarm" to info level
    logging.getLogger("swarm").setLevel(logging.INFO)
    await startup_event()
    atexit.register(shutdown_event)

    server = grpc.aio.server()

    from .api.grpc import grpcdefs_pb2_grpc, grpcdefs_pb2
    from .api import Backend
    grpcdefs_pb2_grpc.add_BackendServicer_to_server(Backend(), server)

    reflection.enable_server_reflection((
        grpcdefs_pb2.DESCRIPTOR.services_by_name["Backend"].full_name,
        reflection.SERVICE_NAME,
    ), server)

    server.add_insecure_port("[::]:50051")
    await server.start()
    logger.info("Server started on port 50051")
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(main())
