from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.hardware.io import Io
from modellsteuerung_backend.hardware.swarm import *
from modellsteuerung_backend.state.controller_state import controller, ControllerStateValue
from modellsteuerung_backend.state.drivectrlstate import Direction, Speed
from statemachine.exceptions import TransitionNotAllowed

from modellsteuerung_backend.state.notifications import notifications
from modellsteuerung_backend.utils import Level

FLANK_ID = "deskhwmod"


def try_event(event_fn):
    try:
        event_fn()
    except TransitionNotAllowed:
        pass


class DoppelmayrDesk(Modifier):
    def __init__(self):
        # TODO legacy
        self.emergency_stop = False
        self.started = False
        self.signal = False
        self.on = False
        self.station_occupied = False
        self.service_mode = False
        self.set_ok = False

        # internal state
        self.speed_dial = Speed.STOP
        self.direction = Direction.FORWARDS

        # IO
        self._io_desk_occupied: FtSwarmSwitch | None = None
        self._io_desk_halt: FtSwarmSwitch | None = None
        self._io_desk_emergency_stop: FtSwarmSwitch | None = None
        self._io_desk_emergency_stop_station_mode: FtSwarmSwitch | None = None
        self._io_desk_speed_dial_1: FtSwarmSwitch | None = None
        self._io_desk_speed_dial_2: FtSwarmSwitch | None = None
        self._io_desk_speed_dial_3: FtSwarmSwitch | None = None
        self._io_desk_forwards: FtSwarmSwitch | None = None
        self._io_desk_backwards: FtSwarmSwitch | None = None
        self._io_desk_passenger_mode: FtSwarmSwitch | None = None
        self._io_desk_service_mode: FtSwarmSwitch | None = None
        self._io_desk_confirm_system: FtSwarmSwitch | None = None
        self._io_desk_confirm_operation: FtSwarmSwitch | None = None
        self._io_desk_start: FtSwarmSwitch | None = None

    # Dear IDE, this is not duplicated code!
    # noinspection DuplicatedCode
    async def register(self, swarm: FtSwarm):
        self._io_desk_occupied = await swarm.get_switch(Io.DESK_OCCUPIED)
        self._io_desk_halt = await swarm.get_switch(Io.DESK_HALT)
        self._io_desk_emergency_stop = await swarm.get_switch(Io.DESK_EMERGENCY_STOP)
        self._io_desk_emergency_stop_station_mode = await swarm.get_switch(Io.DESK_EMERGENCY_STOP_STATION_MODE)
        self._io_desk_speed_dial_1 = await swarm.get_switch(Io.DESK_SPEED_1)
        self._io_desk_speed_dial_2 = await swarm.get_switch(Io.DESK_SPEED_2)
        self._io_desk_speed_dial_3 = await swarm.get_switch(Io.DESK_SPEED_3)
        self._io_desk_forwards = await swarm.get_switch(Io.DESK_FORWARDS)
        self._io_desk_backwards = await swarm.get_switch(Io.DESK_BACKWARDS)
        self._io_desk_passenger_mode = await swarm.get_switch(Io.DESK_PASSENGER_MODE)
        self._io_desk_service_mode = await swarm.get_switch(Io.DESK_SERVICE_MODE)
        self._io_desk_confirm_system = await swarm.get_switch(Io.DESK_CONFIRM_SYSTEM)
        self._io_desk_confirm_operation = await swarm.get_switch(Io.DESK_CONFIRM_OPERATION)
        self._io_desk_start = await swarm.get_switch(Io.DESK_START)

    async def process(self):
        if (not self._io_desk_speed_dial_1.state) \
                and (not self._io_desk_speed_dial_2.state) \
                and (not self._io_desk_speed_dial_3.state):
            self.speed_dial = Speed.STOP

        elif self._io_desk_speed_dial_1.state \
                and (not self._io_desk_speed_dial_2.state) \
                and (not self._io_desk_speed_dial_3.state):
            self.speed_dial = Speed.SLOW

        elif (not self._io_desk_speed_dial_1.state) \
                and self._io_desk_speed_dial_2.state \
                and (not self._io_desk_speed_dial_3.state):
            self.speed_dial = Speed.MEDIUM

        elif self._io_desk_speed_dial_1.state \
                and (not self._io_desk_speed_dial_2.state) \
                and self._io_desk_speed_dial_3.state:
            self.speed_dial = Speed.FAST

        if self._io_desk_forwards.state:
            self.direction = Direction.FORWARDS
        elif self._io_desk_backwards.state:
            self.direction = Direction.BACKWARDS

        if self._io_desk_forwards.state and self._io_desk_backwards.state:
            try_event(controller.event_stop)

        # Update current state based on IO
        if self._io_desk_halt.state \
                or self._io_desk_emergency_stop.state \
                or self._io_desk_emergency_stop_station_mode.state:
            try_event(controller.event_fatal)

        if self._io_desk_occupied.get_flank(FLANK_ID):
            if not ControllerStateValue.load(controller.current_state_value).is_locked:
                try_event(controller.event_lock)
            elif self._io_desk_confirm_operation.state:
                try_event(controller.event_lock)

        if self._io_desk_service_mode.get_flank(FLANK_ID):
            try_event(controller.event_service)

        if self._io_desk_passenger_mode.get_flank(FLANK_ID):
            try_event(controller.transition_passenger)

        if self._io_desk_start.get_flank(FLANK_ID) and self.speed_dial != Speed.STOP:
            try_event(controller.event_start)

        if self._io_desk_confirm_system.get_flank(FLANK_ID) and not notifications.has_of_level(Level.FATAL):
            try_event(controller.transition_all_clear)


desk = DoppelmayrDesk()
