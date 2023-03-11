import time
from dataclasses import dataclass
from enum import Enum
from typing import Union

from modellsteuerung_backend.hardware import desk
from modellsteuerung_backend.state.drivectrlstate import drive_ctrl_state
from modellsteuerung_backend.utils import Level


class ErrorNr(str, Enum):
    DOPPELMAYR_EMERGENCY_STOP = "DES"


@dataclass
class Notification:
    id: int  # Set this to 0 for autoincrement
    level: Level
    title: str
    description: str
    location: str
    start_time: float
    end_time: float = None
    errornr: Union[ErrorNr, None] = None
    possible_sources: Union[list[str], None] = None


class Notifications:
    def __init__(self):
        self._notifications = []
        self._id_counter = 1

    def add_notification(self, notification: Notification, update=True) -> Notification:
        if notification.id == 0:
            notification.id = self._id_counter
            self._id_counter += 1
        else:
            self._id_counter = max(self._id_counter, notification.id + 1)
        self._notifications.append(notification)
        if update:
            self._update()
        return notification

    def remove_notification(self, notification: Notification, update=True):
        self._notifications.remove(notification)
        if update:
            self._update()

    def remove_notification_by_id(self, identifier: int):
        for notification in self._notifications:
            if notification.id == identifier:
                self._notifications.remove(notification)
                self._update()
                return

    def get_notifications(self):
        self._update()
        return self._notifications

    def _update(self):
        # TODO Update this to use the doublemayr pult and not the drive control
        if desk.emergency_stop and \
                not any(
                    (
                            notification.level == Level.FATAL
                            and notification.errornr == ErrorNr.DOPPELMAYR_EMERGENCY_STOP
                    ) for notification in self._notifications
                ):
            self.add_notification(
                Notification(
                    id=0,
                    level=Level.FATAL,
                    title="Doppelmayr Pult Notaus",
                    description="Das Doppelmayr Pult hat den Notaus Knopf gedrückt. "
                                "Das Modell ist nun nicht mehr steuerbar.",
                    location="Doppelmayr",
                    start_time=time.time(),
                    errornr=ErrorNr.DOPPELMAYR_EMERGENCY_STOP,
                    possible_sources=["Doppelmayr Pult"]
                ),
                False
            )
            if drive_ctrl_state.get_emergency_stop() != desk.emergency_stop:
                drive_ctrl_state.set_emergency_stop(desk.emergency_stop)
        else:
            for notification in self._notifications:
                if notification.level == Level.FATAL \
                        and notification.errornr == ErrorNr.DOPPELMAYR_EMERGENCY_STOP:
                    self.remove_notification(notification, False)

            if drive_ctrl_state.get_emergency_stop() != desk.emergency_stop:
                drive_ctrl_state.set_emergency_stop(desk.emergency_stop)


notifications = Notifications()
