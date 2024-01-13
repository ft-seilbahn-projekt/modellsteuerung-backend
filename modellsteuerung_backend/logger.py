import logging
import os

logging.basicConfig(format="%(asctime)s %(name)40s %(levelname)7s: %(message)s", datefmt="%H:%M:%S",
                    level=logging.DEBUG, filename="modellsteuerung.log")


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(logging.Formatter("%(asctime)s %(name)40s %(levelname)7s: %(message)s", "%H:%M:%S"))
    logger.addHandler(console)

    return logger


# Initialize loggers
get_logger("asyncio")
get_logger("grpc._cython.cygrpc")
