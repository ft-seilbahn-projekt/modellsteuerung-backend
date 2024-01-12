from swarm import FtSwarm

from modellsteuerung_backend.hardware.modifier import Modifier


class Key(Modifier):
    async def register(self, swarm: FtSwarm):
        pass

    async def process(self):
        pass


key = Key()
