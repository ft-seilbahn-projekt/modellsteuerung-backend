from abc import ABC, abstractmethod

from swarm import FtSwarm

from modellsteuerung_backend.state.notifications import ErrorNr


class EmergencyChecker(ABC):
    @abstractmethod
    async def register(self, swarm: FtSwarm):
        pass

    @abstractmethod
    async def check(self) -> bool:
        pass


class EmergencyPrefab:
    def __init__(
            self,
            title: str,
            description: str,
            location: str,
            errornr: ErrorNr,
            possible_sources: list[str]
    ):
        self.title = title
        self.description = description
        self.location = location
        self.errornr = errornr
        self.possible_sources = possible_sources

    def copy(
            self,
            title: str = None,
            description: str = None,
            location: str = None,
            errornr: ErrorNr = None,
            possible_sources: list[str] = None
    ):
        return EmergencyPrefab(
            title=title or self.title,
            description=description or self.description,
            location=location or self.location,
            errornr=errornr or self.errornr,
            possible_sources=possible_sources or [x for x in self.possible_sources]
        )
