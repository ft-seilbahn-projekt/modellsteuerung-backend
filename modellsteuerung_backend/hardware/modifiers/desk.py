from modellsteuerung_backend.hardware.utils.flank import FlankedSwitch
from modellsteuerung_backend.hardware.utils.lamp import BlinkingLamp
from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.hardware.io import Input, Output
from swarm import *
from modellsteuerung_backend.state.controller_state import controller, use_state, Controller
from modellsteuerung_backend.state.drivectrlstate import Direction, Speed, drive_ctrl_state
from statemachine.exceptions import TransitionNotAllowed

from modellsteuerung_backend.state.notifications import notifications
from modellsteuerung_backend.utils import Level


def try_event(event_fn, logger=None):
    try:
        event_fn()
    except TransitionNotAllowed as e:
        if logger:
            logger.warn("Transition not allowed", e.state, e.event)


class DoppelmayrDesk(Modifier):
    def __init__(self):
        super().__init__()

        # internal state
        self.speed_dial = Speed.STOP
        self.direction = Direction.FORWARDS
        self.was_locked = False
        self.was_state = ""

        # IO
        self._in_desk_occupied: FlankedSwitch | None = None
        self._in_desk_speed_dial_1: FtSwarmSwitch | None = None
        self._in_desk_speed_dial_2: FtSwarmSwitch | None = None
        self._in_desk_speed_dial_3: FtSwarmSwitch | None = None
        self._in_desk_forwards: FtSwarmSwitch | None = None
        self._in_desk_backwards: FtSwarmSwitch | None = None
        self._in_desk_passenger_mode: FlankedSwitch | None = None
        self._in_desk_service_mode: FlankedSwitch | None = None
        self._in_desk_confirm_system: FlankedSwitch | None = None
        self._in_desk_confirm_operation: FtSwarmSwitch | None = None
        self._in_desk_start: FlankedSwitch | None = None
        self._in_desk_disable: FtSwarmSwitch | None = None
        self._in_desk_enable: FtSwarmSwitch | None = None

        self._out_desk_on_off: FtSwarmLamp | None = None
        self._out_desk_start: BlinkingLamp | None = None

    async def register(self, hw: FtSwarm):
        self._in_desk_occupied = FlankedSwitch(await hw.get_switch(Input.DESK_OCCUPIED))
        self._in_desk_speed_dial_1 = await hw.get_switch(Input.DESK_SPEED_1)
        self._in_desk_speed_dial_2 = await hw.get_switch(Input.DESK_SPEED_2)
        self._in_desk_speed_dial_3 = await hw.get_switch(Input.DESK_SPEED_3)
        self._in_desk_forwards = await hw.get_switch(Input.DESK_FORWARDS)
        self._in_desk_backwards = await hw.get_switch(Input.DESK_BACKWARDS)
        self._in_desk_passenger_mode = FlankedSwitch(await hw.get_switch(Input.DESK_PASSENGER_MODE))
        self._in_desk_service_mode = FlankedSwitch(await hw.get_switch(Input.DESK_SERVICE_MODE))
        self._in_desk_confirm_system = FlankedSwitch(await hw.get_switch(Input.DESK_CONFIRM_SYSTEM))
        self._in_desk_confirm_operation = await hw.get_switch(Input.DESK_CONFIRM_OPERATION)
        self._in_desk_start = FlankedSwitch(await hw.get_switch(Input.DESK_START))
        self._in_desk_disable = await hw.get_switch(Input.DESK_SYSTEM_DISABLE)
        self._in_desk_enable = await hw.get_switch(Input.DESK_SYSTEM_ENABLE)

        self._out_desk_on_off = await hw.get_lamp(Output.DESK_ON_OFF)
        self._out_desk_start = BlinkingLamp(await hw.get_lamp(Output.DESK_START))

    async def process(self):
        state = use_state()

        state_1 = await self._in_desk_speed_dial_1.get_state()
        state_2 = await self._in_desk_speed_dial_2.get_state()
        state_3 = await self._in_desk_speed_dial_3.get_state()

        if not state_1 and not state_2 and not state_3:
            self.speed_dial = Speed.STOP
            try_event(controller.event_stop)
        elif state_1 and not state_2 and not state_3:
            self.speed_dial = Speed.SLOW
        elif not state_1 and state_2 and not state_3:
            self.speed_dial = Speed.MEDIUM
        elif not state_1 and not state_2 and state_3:
            self.speed_dial = Speed.FAST

        if await self._in_desk_forwards.get_state():
            self.direction = Direction.FORWARDS
        elif await self._in_desk_backwards.get_state():
            self.direction = Direction.BACKWARDS

        if await self._in_desk_forwards.get_state() and await self._in_desk_backwards.get_state():
            try_event(controller.event_stop)

        if await self._in_desk_occupied.get_flank():
            if await self._in_desk_disable.get_state():
                try_event(controller.event_lock)
                self.logger.info("Desk locked by disable switch")
            elif await self._in_desk_enable.get_state():
                try_event(controller.event_unlock)
                self.logger.info("Desk unlocked by enable switch")
            else:
                self.logger.warn("Desk occupied, but no lock or unlock switch pressed")

        if await self._in_desk_service_mode.get_flank():
            try_event(controller.event_service)

        if await self._in_desk_passenger_mode.get_flank():
            try_event(controller.transition_passenger)

        if await self._in_desk_start.get_flank() and self.speed_dial != Speed.STOP:
            try_event(controller.event_start)

        if await self._in_desk_confirm_system.get_flank() and not notifications.has_of_level(Level.FATAL):
            try_event(controller.transition_all_clear)

        if self.was_locked != state.is_locked:
            self.was_locked = state.is_locked
            if state.is_locked:
                await self.on_lock()
            else:
                await self.on_unlock()

        if self.was_state != controller.current_state.id:
            self.was_state = controller.current_state.id
            await self.on_state_change()

        if controller.current_state == Controller.state_off and self.speed_dial != Speed.STOP:
            await self._out_desk_start.blink()
        else:
            await self._out_desk_start.off()

        if state.can_drive_auto:
            drive_ctrl_state.set_speed(self.speed_dial)
            drive_ctrl_state.set_direction(self.direction)
        else:
            drive_ctrl_state.set_speed(Speed.STOP)

    async def on_lock(self):
        await self._out_desk_on_off.off()
        await self._out_desk_start.off()

    async def on_unlock(self):
        await self._out_desk_on_off.on()

    async def on_state_change(self):
        pass


desk = DoppelmayrDesk()
