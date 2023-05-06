import asyncio
import os
from threading import Thread

from .desk import desk
from .swarm import FtSwarm, FtSwarmAnalogIn
from ..logger import get_logger
from ..state.notifications import notification_modifier


class SerialPortFinder:
    def find(self):
        env = os.environ.get("SERIAL_PORT")
        if env:
            return env
        else:
            return input("Please enter the serial port: ")


class SwarmBackend(Thread):
    swarm: FtSwarm

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
        self.swarm = FtSwarm(finder.find(), True)  # True for debug comms mode
        # Init the hardware
        self.booted.release()
        await asyncio.gather(self.loop(), self.swarm.inputloop())

    async def loop(self):
        # Init the hardware
        self.logger.debug("Swarm Backend is running")

        mods = [
            desk,
            notification_modifier
        ]

        for mod in mods:
            await mod.register(self.swarm)

        tick_time = 0.1
        while not self.teardown_requested:
            tick_start = asyncio.get_event_loop().time()
            for mod in mods:
                await mod.process()
            tick_end = asyncio.get_event_loop().time()
            await asyncio.sleep(max(0, tick_time - (tick_end - tick_start)))

        self.logger.debug("Swarm Backend is shutting down")


backend = SwarmBackend()
