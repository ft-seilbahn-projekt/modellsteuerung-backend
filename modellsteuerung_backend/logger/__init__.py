import logging
import sys
import coloredlogs


def get_logger(name):
    logger = logging.getLogger(name)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = coloredlogs.ColoredFormatter("%(asctime)s %(name)30s %(levelname)s: %(message)s", datefmt="%H:%M:%S")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.DEBUG)
    return logger
