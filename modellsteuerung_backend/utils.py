from enum import Enum


class Level(str, Enum):
    INFO = "info"
    WARNING = "warning"
    FATAL = "fatal"
