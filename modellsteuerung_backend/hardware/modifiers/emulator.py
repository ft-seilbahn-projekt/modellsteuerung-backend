from swarm import FtSwarm, FtSwarmPixel

from modellsteuerung_backend.api.grpc.grpcdefs_pb2 import Speed
from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.state.controller_state import use_state
from modellsteuerung_backend.state.drivectrlstate import drive_ctrl_state
from modellsteuerung_backend.utils import is_emulated, Level


class Emulator(Modifier):
    _out_drive_led: FtSwarmPixel
    _out_sys_led: FtSwarmPixel
    _out_lock_led: FtSwarmPixel

    def __init__(self):
        super().__init__()
        self.emulator_running = is_emulated()

        self.was_locked = False
        self.last_level: Level | None = None
        self.last_speed = -1

    async def register(self, swarm: FtSwarm):
        if not self.emulator_running:
            self.logger.info("Emulator not running")
            return

        self.logger.info("Emulator running")

        self._out_drive_led = await swarm.get_pixel("osimfa")
        self._out_sys_led = await swarm.get_pixel("osimmnot")
        self._out_lock_led = await swarm.get_pixel("osimlock")

        await self._out_lock_led.set_brightness(100)
        await self._out_sys_led.set_brightness(100)
        await self._out_drive_led.set_brightness(100)

        await self._out_lock_led.set_color(0xffffff)

    async def process(self):
        if not self.emulator_running:
            return

        state = use_state()

        if self.was_locked != state.is_locked:
            self.was_locked = state.is_locked
            if state.is_locked:
                await self._out_lock_led.set_color(0xff0000)
            else:
                await self._out_lock_led.set_color(0x00ff00)

        level = state.get_level()
        if level != self.last_level:
            self.last_level = level
            if level == Level.INFO:
                await self._out_sys_led.set_color(0x00ff00)
            elif level == Level.WARNING:
                await self._out_sys_led.set_color(0xffff00)
            elif level == Level.FATAL:
                await self._out_sys_led.set_color(0xff0000)
            else:
                await self._out_sys_led.set_color(0x0000ff)

        if drive_ctrl_state.get_speed() != self.last_speed:
            self.last_speed = drive_ctrl_state.get_state().requested_speed
            if self.last_speed == Speed.STOP:
                await self._out_drive_led.set_color(0xff0000)
            elif self.last_speed == Speed.SLOW:
                await self._out_drive_led.set_color(0xff7f00)
            elif self.last_speed == Speed.MEDIUM:
                await self._out_drive_led.set_color(0x7fff00)
            elif self.last_speed == Speed.FAST:
                await self._out_drive_led.set_color(0x00ff00)


emulator = Emulator()
