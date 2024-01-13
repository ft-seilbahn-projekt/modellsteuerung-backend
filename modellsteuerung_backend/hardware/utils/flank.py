from swarm import Toggle, FtSwarmSwitch


class FlankedSwitch:
    def __init__(self, switch: FtSwarmSwitch, invert: bool = False):
        self.switch = switch
        self._state = False
        self.invert = invert

    async def get_toggle(self) -> Toggle:
        return await self.switch.get_toggle()

    async def get_state(self) -> bool:
        return await self.switch.get_state()

    async def is_pressed(self) -> bool:
        return await self.get_state()

    async def is_released(self) -> bool:
        return not await self.get_state()

    async def has_toggled_up(self) -> bool:
        return (await self.get_toggle()) == Toggle.TOGGLEUP

    async def has_toggled_down(self) -> bool:
        return (await self.get_toggle()) == Toggle.TOGGLEDOWN

    async def get_flank(self) -> bool:
        now = (await self.get_state()) != self.invert

        if now != self._state:
            self._state = now
            return self._state

        return False
