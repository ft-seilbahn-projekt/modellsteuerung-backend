import time

from swarm import FtSwarm

from modellsteuerung_backend.hardware.io import Input, Output
from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.hardware.modifiers.desk import try_event
from modellsteuerung_backend.hardware.modifiers.emergency.abstract import EmergencyPrefab
from modellsteuerung_backend.hardware.modifiers.emergency.impl import checkers
from modellsteuerung_backend.hardware.utils.flank import FlankedSwitch
from modellsteuerung_backend.hardware.utils.lamp import BlinkingLamp
from modellsteuerung_backend.state.controller_state import use_state, Controller, controller
from modellsteuerung_backend.state.drivectrlstate import drive_ctrl_state
from modellsteuerung_backend.state.notifications import notifications, Notification, ErrorNr
from modellsteuerung_backend.utils import Level


class Emergency(Modifier):
    _in_confirm_operation: FlankedSwitch | None = None
    _out_confirm_operation: BlinkingLamp | None = None

    async def register(self, swarm: FtSwarm):
        for c, _ in checkers:
            await c.register(swarm)

        self._in_confirm_operation = FlankedSwitch(await swarm.get_switch(Input.DESK_CONFIRM_OPERATION))
        self._out_confirm_operation = BlinkingLamp(await swarm.get_lamp(Output.DESK_CONFIRM_OPERATION))

    async def check_all(self) -> bool:
        for c, _ in checkers:
            if await c.check():
                return True
        return False

    async def first_prefab(self) -> EmergencyPrefab | None:
        for c, p in checkers:
            if await c.check():
                return p
        return None

    async def process(self):
        if self.is_lockdown():
            drive_ctrl_state.set_emergency_stop(True)
            await self.process_lockdown()
            return

        drive_ctrl_state.set_emergency_stop(False)
        await self._out_confirm_operation.off()

        if prefab := await self.first_prefab():
            await self.lockdown(
                title=prefab.title,
                description=prefab.description,
                location=prefab.location,
                errornr=prefab.errornr,
                possible_sources=prefab.possible_sources
            )

    async def process_lockdown(self):
        # can unlock?
        if (
                not await self.check_all()
                and notifications.can_unlock()
        ):
            if await self._in_confirm_operation.get_flank():
                try_event(controller.transition_all_clear)
            elif not use_state().is_locked:
                await self._out_confirm_operation.blink()
            else:
                await self._out_confirm_operation.off()
        else:
            await self._out_confirm_operation.off()

    def is_lockdown(self) -> bool:
        return use_state().is_fatal

    async def lockdown(
            self,
            title="Unbekannter Fehler",
            description="Ein unbekannter Fehler ist aufgetreten. Bitte prüfe alle Komponenten und bestätige",
            location="Unbekannt",
            errornr=ErrorNr.LOCKDOWN_UNKNOWN,
            possible_sources=None
    ):
        if possible_sources is None:
            possible_sources = []
        self.logger.info("LOCKDOWN")
        notifications.add_notification(Notification(
            id=0,
            level=Level.FATAL,
            title=title,
            description=description,
            location=location,
            start_time=time.time(),
            errornr=errornr,
            possible_sources=possible_sources
        ))

    async def __call__(self, *args, **kwargs):
        await self.lockdown(*args, **kwargs)


emergency = Emergency()
