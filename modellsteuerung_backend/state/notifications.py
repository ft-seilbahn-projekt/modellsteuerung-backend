import json
import time
from dataclasses import dataclass
from enum import Enum
from typing import Union

from swarm import FtSwarm

from modellsteuerung_backend.hardware.modifier import Modifier
from modellsteuerung_backend.logger import get_logger
from modellsteuerung_backend.state.controller_state import controller
from modellsteuerung_backend.utils import Level
from statemachine.exceptions import TransitionNotAllowed


class ErrorNr(str, Enum):
    LOCKDOWN_UNKNOWN = "LU"
    DOPPELMAYR_EMERGENCY_STOP = "DES"


def try_event(event_fn):
    try:
        event_fn()
    except TransitionNotAllowed:
        pass


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
        self.logger = get_logger("notifications")

    def add_notification(self, notification: Notification) -> Notification:
        if notification.id == 0:
            notification.id = self._id_counter
            self._id_counter += 1
        else:
            self._id_counter = max(self._id_counter, notification.id + 1)
        self._notifications.append(notification)
        self.logger.info("Added notification:" + json.dumps(notification.__dict__))
        return notification

    def remove_notification(self, notification: Notification):
        self._notifications.remove(notification)

    def remove_notification_by_id(self, identifier: int):
        for notification in self._notifications:
            if notification.id == identifier:
                self._notifications.remove(notification)
                return

    def get_notifications(self):
        return self._notifications

    def has_of_level(self, level: Level):
        return any(notification.level == level for notification in self._notifications)

    def can_unlock(self):
        return not self.has_of_level(Level.FATAL)


class NotificationModifier(Modifier):
    def __init__(self, notifier: Notifications):
        super().__init__()
        self.notifications = notifier

    async def register(self, swarm: FtSwarm):
        pass

    async def process(self):
        if self.notifications.has_of_level(Level.FATAL):
            try_event(controller.event_fatal)

        if self.notifications.has_of_level(Level.WARNING):
            try_event(controller.event_warn)

        if not self.notifications.has_of_level(Level.WARNING) \
                and not self.notifications.has_of_level(Level.FATAL):
            try_event(controller.event_clear_warn)


notifications = Notifications()
notification_modifier = NotificationModifier(notifications)
