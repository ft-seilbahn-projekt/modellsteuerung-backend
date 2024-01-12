from abc import ABC, abstractmethod

from swarm import FtSwarm

from modellsteuerung_backend.logger import get_logger


class Modifier(ABC):
    def __init__(self):
        self.logger = get_logger(self.__class__.__name__)

    @abstractmethod
    async def register(self, swarm: FtSwarm):
        pass

    @abstractmethod
    async def process(self):
        pass
