import os
from enum import Enum


class Level(str, Enum):
    INFO = "info"
    WARNING = "warning"
    FATAL = "fatal"


def is_emulated() -> bool:
    return os.getenv("EMULATED") is not None
