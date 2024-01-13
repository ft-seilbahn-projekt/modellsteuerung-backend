import asyncio
import logging

import dotenv

from .api import AioBackend

dotenv.load_dotenv()

import atexit

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
    swarm_logger = logging.getLogger("swarm")
    swarm_logger.setLevel(logging.DEBUG)

    await startup_event()
    atexit.register(shutdown_event)

    rest = AioBackend()
    logger.info("Server started on port 8080")
    await rest.run("127.0.0.1", 8080)

    # run until ctrl+c
    while True:
        await asyncio.sleep(1)
