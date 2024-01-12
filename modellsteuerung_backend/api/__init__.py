import subprocess
import time

from .grpc import grpcdefs_pb2_grpc, grpcdefs_pb2
from modellsteuerung_backend.state.controller_state import use_state, use_state_machine
from ..hardware import desk
from ..state.drivectrlstate import Speed
from ..state.notifications import notifications
from ..utils import Level


class Backend(grpcdefs_pb2_grpc.BackendServicer):
    async def info(self, request, context):
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        return grpcdefs_pb2.Info(
            project="modellsteuerung_backend",
            version="0.0.1",
            description="Backend for the ft-seilbahn-project",
            author="ft-seilbahn-project",
            contact="christian.bergschneider@gmx.de",
            license="MIT",
            time=time.time(),
            commit=commit,
        )

    async def state(self, request, context):
        s = use_state()
        c = use_state_machine()

        def get_speed():
            match desk.speed_dial:
                case Speed.STOP:
                    return grpcdefs_pb2.Speed.STOP
                case Speed.SLOW:
                    return grpcdefs_pb2.Speed.SLOW
                case Speed.MEDIUM:
                    return grpcdefs_pb2.Speed.MEDIUM
                case Speed.FAST:
                    return grpcdefs_pb2.Speed.FAST
                case _:
                    return grpcdefs_pb2.Speed.STOP

        return grpcdefs_pb2.State(
            name=c.current_state.name,
            is_locked=s.is_locked,
            is_warn=s.is_warn,
            is_fatal=s.is_fatal,
            can_drive_auto=s.can_drive_auto,
            can_drive_manual=s.can_drive_manual,
            speed=get_speed(),
        )

    async def notifications(self, request, context):
        n = []

        def get_level(level: Level):
            match level:
                case Level.FATAL:
                    return grpcdefs_pb2.Level.FATAL
                case Level.WARNING:
                    return grpcdefs_pb2.Level.WARNING
                case Level.INFO:
                    return grpcdefs_pb2.Level.INFO
                case _:
                    return grpcdefs_pb2.Level.INFO

        for notification in notifications.get_notifications():
            n.append(grpcdefs_pb2.Notification(
                id=notification.id,
                level=get_level(notification.level),
                title=notification.title,
                description=notification.description,
                location=notification.location,
                start_time=notification.start_time,
                errorrnr=notification.errornr.value,
                possible_sources=notification.possible_sources,
            ))

        return grpcdefs_pb2.NotificationList(notifications=n)
