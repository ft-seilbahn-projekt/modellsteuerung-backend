import asyncio
from threading import Thread
from platformio.device.finder import SerialPortFinder

from .swarm import FtSwarm
from ..logger import get_logger


class SwarmBackend(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.teardown_requested = False
        self.logger = get_logger(__name__)
        self.swarm = None
        self.booted = asyncio.Lock()
        self.booted._locked = True  # Syncronized lock

    def run(self):
        asyncio.run(self.async_run())

    async def async_run(self):
        finder = SerialPortFinder()
        self.swarm = FtSwarm(finder.find(), True)  # True for debug mode
        # Init the swarm
        self.booted.release()
        await asyncio.gather(self.loop(), self.swarm.inputloop())

    async def loop(self):
        # Init the swarm
        taster = await self.swarm.get_switch("endstoplower")

        while not self.teardown_requested:

            if taster.state:
                self.logger.debug("Taster gedrückt")
            else:
                self.logger.debug("Taster nicht gedrückt")

            await asyncio.sleep(1)

        self.logger.debug("Swarm Backend is shutting down")


backend = SwarmBackend()
