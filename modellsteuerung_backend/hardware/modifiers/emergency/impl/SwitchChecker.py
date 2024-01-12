from swarm import FtSwarm, FtSwarmSwitch

from modellsteuerung_backend.hardware.modifiers.emergency.abstract import EmergencyChecker


class SwitchChecker(EmergencyChecker):
    _in_switch: FtSwarmSwitch

    def __init__(self, switch_name: str, error_when: bool = True):
        self.switch_name = switch_name
        self.error_when = error_when

    async def register(self, swarm: FtSwarm):
        self._in_switch = await swarm.get_switch(self.switch_name)

    async def check(self) -> bool:
        return await self._in_switch.get_state() == self.error_when
