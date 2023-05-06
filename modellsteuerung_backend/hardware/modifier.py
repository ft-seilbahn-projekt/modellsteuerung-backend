from abc import ABC, abstractmethod

from modellsteuerung_backend.hardware.swarm import FtSwarm


class Modifier(ABC):
    @abstractmethod
    async def register(self, swarm: FtSwarm):
        pass

    @abstractmethod
    async def process(self):
        pass
