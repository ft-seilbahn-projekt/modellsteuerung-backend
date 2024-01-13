import simpleaudio
from swarm import FtSwarm

from modellsteuerung_backend.hardware.io import Input
from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.hardware.utils.flank import FlankedSwitch
from modellsteuerung_backend.state.controller_state import use_state


class Call(Modifier):
    _in_call: FlankedSwitch

    async def register(self, swarm: FtSwarm):
        self._in_call = FlankedSwitch(await swarm.get_switch(Input.DESK_SIGNAL), True)

    async def process(self):
        if await self._in_call.get_flank() and not use_state().is_locked:
            simpleaudio.WaveObject.from_wave_file('info.wav').play().wait_done()


call = Call()
