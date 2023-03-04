import logging
import coloredlogs

coloredlogs.install(level=logging.DEBUG, fmt="%(asctime)s %(name)35s %(levelname)7s: %(message)s", datefmt="%H:%M:%S")


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
