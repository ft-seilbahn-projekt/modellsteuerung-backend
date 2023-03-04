import asyncio
import os
from threading import Thread

from .swarm import FtSwarm, FtSwarmAnalogIn
from ..logger import get_logger
from ..state import set_poti_state


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
        # Init the swarm
        self.booted.release()
        await asyncio.gather(self.loop(), self.swarm.inputloop())

    async def loop(self):
        # Init the swarm
        self.logger.debug("Swarm Backend is running")
        analog_in: FtSwarmAnalogIn = await self.swarm.get_analogin("endstoplower", 20)

        while not self.teardown_requested:
            set_poti_state(analog_in.value)
            await asyncio.sleep(1)

        self.logger.debug("Swarm Backend is shutting down")


backend = SwarmBackend()
