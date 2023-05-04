from modellsteuerung_backend.hardware.hardwaremod import HardwareMod
from modellsteuerung_backend.hardware.io import Io
from modellsteuerung_backend.hardware.swarm import *
from modellsteuerung_backend.state.drivectrlstate import Direction, Speed


class DoppelmayrDesk(HardwareMod):
    def __init__(self):
        self.speed_dial = 0
        self.emergency_stop = False
        self.started = False
        self.signal = False
        self.on = False
        self.station_occupied = False
        self.service_mode = False
        self.direction = Direction.FORWARDS,
        self.set_ok = False

        self._io_desk_on_off: FtSwarmSwitch | None = None

    async def register(self, swarm: FtSwarm):
        self._io_desk_on_off = await swarm.get_switch(Io.DESK_ON_OFF)

    async def process(self):
        if self._io_desk_on_off.get_flank():
            print("toggle desk on/off")


desk = DoppelmayrDesk()
