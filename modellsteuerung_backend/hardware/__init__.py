import asyncio
import os
from threading import Thread

from swarm import FtSwarm

from modellsteuerung_backend.hardware.modifiers.desk import desk
from .modifiers.call import call
from .modifiers.emergency import emergency
from .modifiers.emulator import emulator
from .modifiers.key import key
from .modifiers.leds import leds
from .modifiers.sense import ntc
from ..logger import get_logger
from ..state.notifications import notification_modifier

from serial.tools.list_ports import comports


def find():
    env = os.environ.get("SERIAL_PORT")
    if env:
        return env
    else:
        return comports()[0].device


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
        self.swarm = FtSwarm(find())
        self.booted.release()
        await self.loop()

    async def loop(self):
        # Init the hardware
        self.logger.debug("Swarm Backend is running")

        mods = [
            desk,
            #leds,
            #emergency,
            #emulator,
            #key,
            #call,
            #ntc,
            notification_modifier,
        ]

        for mod in mods:
            self.logger.debug(f"Registering {mod.__class__.__name__}")
            await mod.register(self.swarm)

        while not self.teardown_requested:
            await asyncio.gather(*[mod.process() for mod in mods])
            await asyncio.sleep(0.01)

        self.logger.debug("Swarm Backend is shutting down")


backend = SwarmBackend()
