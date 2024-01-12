import os
from enum import Enum


class Level(str, Enum):
    INFO = "info"
    WARNING = "warning"
    FATAL = "fatal"


def is_emulated() -> bool:
    return os.getenv("EMULATED") is not None


class PersistedFiFo:
    def __init__(self, max_size: int, filename: str):
        self.max_size = max_size
        self.filename = filename
        self._fifo = []

        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    self._fifo.append(line.strip())

        self._fifo = self._fifo[-self.max_size:]

        with open(self.filename, "w") as f:
            for line in self._fifo:
                f.write(line + "\n")

    def append(self, line: str):
        self._fifo.append(line)

        with open(self.filename, "a") as f:
            f.write(line + "\n")

        if len(self._fifo) > self.max_size:
            self._fifo.pop(0)

        with open(self.filename, "w") as f:
            for line in self._fifo:
                f.write(line + "\n")

    def __iter__(self):
        return iter(self._fifo)

    def get_all(self):
        return self._fifo
