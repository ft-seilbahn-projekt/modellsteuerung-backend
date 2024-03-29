import json

from statemachine import StateMachine, State
from dataclasses import dataclass

from modellsteuerung_backend.utils import Level


@dataclass
class ControllerStateValue:
    is_locked: bool = False
    can_drive_auto: bool = False
    can_drive_manual: bool = False
    is_fatal: bool = False
    is_warn: bool = False

    def t(self):
        return json.dumps({
            'is_locked': self.is_locked,
            'can_drive_auto': self.can_drive_auto,
            'can_drive_manual': self.can_drive_manual,
            'is_fatal': self.is_fatal,
            'is_warn': self.is_warn
        })

    @staticmethod
    def load(data) -> 'ControllerStateValue':
        data = json.loads(data)
        return ControllerStateValue(
            is_locked=data['is_locked'],
            can_drive_auto=data['can_drive_auto'],
            can_drive_manual=data['can_drive_manual'],
            is_fatal=data['is_fatal'],
            is_warn=data['is_warn']
        )

    def get_level(self) -> Level:
        if self.is_fatal:
            return Level.FATAL
        elif self.is_warn:
            return Level.WARNING
        else:
            return Level.INFO


class Controller(StateMachine):
    # states
    state_deactivated = \
        State('Deactivated', initial=True, value=ControllerStateValue(is_locked=True).t())
    state_off = \
        State('Off', value=ControllerStateValue().t())
    state_service = \
        State('Service', value=ControllerStateValue(can_drive_manual=True).t())
    state_service_lock = \
        State('Service Lock', value=ControllerStateValue(can_drive_manual=True, is_locked=True).t())
    state_drv_info = \
        State('Normal Info', value=ControllerStateValue(can_drive_auto=True).t())
    state_drv_info_lock = \
        State('Normal Info Lock', value=ControllerStateValue(can_drive_auto=True, is_locked=True).t())
    state_drv_warn = \
        State('Normal Warning', value=ControllerStateValue(can_drive_auto=True, is_warn=True).t())
    state_drv_warn_lock = \
        State('Normal Warning Lock', value=ControllerStateValue(can_drive_auto=True, is_warn=True, is_locked=True).t())
    state_fatal = \
        State('Fatal Error', value=ControllerStateValue(is_fatal=True).t())
    state_fatal_lock = \
        State('Fatal Error Lock', value=ControllerStateValue(is_fatal=True, is_locked=True).t())

    # transitions
    transition_activate = state_deactivated.to(state_off)
    transition_all_clear = state_fatal.to(state_off)
    transition_passenger = state_service.to(state_off)

    # events
    event_fatal = state_deactivated.to(state_fatal_lock) | \
                  state_drv_info_lock.to(state_fatal_lock) | \
                  state_drv_warn_lock.to(state_fatal_lock) | \
                  state_off.to(state_fatal) | \
                  state_drv_info.to(state_fatal) | \
                  state_drv_warn.to(state_fatal)

    event_service = state_off.to(state_service) | \
                    state_drv_info.to(state_service) | \
                    state_drv_warn.to(state_service) | \
                    state_fatal.to(state_service)

    event_lock = state_service.to(state_service_lock) | \
                 state_drv_info.to(state_drv_info_lock) | \
                 state_drv_warn.to(state_drv_warn_lock) | \
                 state_fatal.to(state_fatal_lock) | \
                 state_off.to(state_deactivated)

    event_unlock = state_service_lock.to(state_service) | \
                   state_drv_info_lock.to(state_drv_info) | \
                   state_drv_warn_lock.to(state_drv_warn) | \
                   state_fatal_lock.to(state_fatal) | \
                   state_deactivated.to(state_off)

    event_warn = state_drv_info.to(state_drv_warn) | \
                 state_drv_info_lock.to(state_drv_warn_lock)

    event_clear_warn = state_drv_warn.to(state_drv_info) | \
                       state_drv_warn_lock.to(state_drv_info_lock)

    event_start = state_off.to(state_drv_info)

    event_stop = state_drv_info.to(state_off) | \
                 state_drv_warn.to(state_off)


controller = Controller()


def use_state_machine():
    return controller


def use_state() -> ControllerStateValue:
    return ControllerStateValue.load(controller.current_state_value)
