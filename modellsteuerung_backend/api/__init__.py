import subprocess
import time

from .grpc import grpcdefs_pb2_grpc, grpcdefs_pb2
from modellsteuerung_backend.state.controller_state import use_state, use_state_machine
from .grpc.grpcdefs_pb2 import NTCStat
from ..hardware import desk, key, ntc
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

    async def remove_notification(self, request, context):
        notifications.remove_notification_by_id(request.id)
        return grpcdefs_pb2.Void()

    async def key_unlock(self, request: grpcdefs_pb2.KeyPair, context):
        result = key.unlock_key_for_user(request.username, request.id, request.hmac)
        return grpcdefs_pb2.Status(value=result)

    async def key_status(self, request, context):
        return grpcdefs_pb2.KeyStatus(
            is_pulled=key.last_state,
            is_verified=key.unlocked or time.time() - key.can_unlock_start < 30,
            username=key.current_key_user or "",
        )

    async def stats_data(self, request, context) -> grpcdefs_pb2.StatsData:
        stats: list[NTCStat] = []

        for ntc_id in ntc.get_ids():
            name: str = ntc.get_name(ntc_id)
            data: list[grpcdefs_pb2.NTCStatElement] = [
                grpcdefs_pb2.NTCStatElement(time=float(x.split(":")[0]), degrees=float(x.split(":")[1]))
                for x in ntc.get_data(ntc_id)
            ]
            stats.append(NTCStat(id=ntc_id, name=name, elements=data))

        return grpcdefs_pb2.StatsData(ntc=stats)
