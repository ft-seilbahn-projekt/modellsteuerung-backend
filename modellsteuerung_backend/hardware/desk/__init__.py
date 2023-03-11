import os

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

        self._env_speed_knob_threshold = int(os.environ["DESK_SPEED_KNOB_THRESHOLD"])
        self._env_speed_knob_baseline = int(os.environ["DESK_SPEED_KNOB_BASELINE"])

        self._speed_dial_input: FtSwarmAnalogIn = None

    async def register(self, swarm: FtSwarm):
        self._speed_dial_input = await swarm.get_analogin(Io.TEST_DEVICE, 40)

    async def process(self):
        speed_dial_value = self._speed_dial_input.value

        # speed is correct if baseline + speed * threshold < value < baseline + (speed+1) * threshold
        # speed is 0 if value < baseline
        # speed is 1 if baseline < value < baseline + threshold
        # speed is 2 if baseline + threshold < value < baseline + 2 * threshold
        # ...

        if speed_dial_value < self._env_speed_knob_baseline:
            self.speed_dial = 0
        else:
            self.speed_dial = (speed_dial_value - self._env_speed_knob_baseline) // self._env_speed_knob_threshold + 1

        self.speed_dial = min(self.speed_dial, Speed.FAST)


desk = DoppelmayrDesk()
