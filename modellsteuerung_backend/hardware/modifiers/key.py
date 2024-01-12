import os
import time

from swarm import FtSwarm, FtSwarmSwitch, FtSwarmPixel

from modellsteuerung_backend.hardware.io import Input, Output
from modellsteuerung_backend.hardware.modifier import Modifier
import hmac

from modellsteuerung_backend.hardware.utils.colors import RED, GREEN, MAGENTA, BLUE
from modellsteuerung_backend.state.notifications import notifications, Notification, ErrorNr
from modellsteuerung_backend.utils import Level


class Key(Modifier):
    _out_key: FtSwarmPixel
    _in_key: FtSwarmSwitch

    def __init__(self):
        super().__init__()
        self.prev_color = 0
        self.current_key_user: str | None = None
        self.can_unlock_start: float = 0
        self.unlocked = False
        self.last_error_id = 0
        self.last_state = False

    async def register(self, swarm: FtSwarm):
        self._in_key = await swarm.get_switch(Input.DESK_KEY_SWITCH)
        self._out_key = await swarm.get_pixel(Output.KEY_SWITCH)

    def _gen_hmac(self, msg: str):
        return hmac.new(os.getenv("HMAC_KEY").encode('utf-8'), msg.encode('utf-8'), 'sha256').hexdigest()[0:5].upper()

    def check_key(self, identifier: int, provided_key: str):
        return self._gen_hmac(str(identifier)) == provided_key

    def unlock_key_for_user(self, user: str, identifier: int, provided_key: str):
        if self.check_key(identifier, provided_key):
            self.current_key_user = user
            self.can_unlock_start = time.time()
            return True
        return False

    async def process(self):
        key_state = await self._in_key.get_state()
        self.last_state = key_state
        await self._determine_state(key_state)

    async def _determine_state(self, key_state: bool):
        if time.time() - self.can_unlock_start > 30:
            await self._handle_while_locked(key_state)
        else:
            await self._handle_while_unlocked(key_state)

    async def _handle_while_unlocked(self, key_state: bool):
        if key_state:
            await self.set_color(MAGENTA)
        else:
            await self.set_color(BLUE)
            self.unlocked = True
            self.can_unlock_start = 0

    async def _handle_while_locked(self, key_state: bool):
        if key_state:
            await self.set_color(GREEN)
            self.unlocked = False
        elif self.unlocked:
            await self.set_color(BLUE)
        else:
            await self.set_color(RED)
            notifications.add_notification_if_none_with_nr(Notification(
                id=0,
                title="Ersatzschlüssel gezogen",
                description="Der Ersatzschlüssel wurde gezogen. Bitte den Schlüssel wieder einstecken.",
                start_time=time.time(),
                location="Steuerpult",
                possible_sources=["Schlüsselschalter am Pult"],
                level=Level.FATAL,
                errornr=ErrorNr.EXTRA_KEY_REMOVED,
            ))

    async def set_color(self, color: int):
        if color == self.prev_color:
            return
        self.prev_color = color
        await self._out_key.set_color(color)


key = Key()
