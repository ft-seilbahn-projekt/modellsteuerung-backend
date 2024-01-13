import subprocess
import time

from aiohttp import web

from modellsteuerung_backend.hardware import desk, key
from modellsteuerung_backend.state.controller_state import use_state, use_state_machine
from modellsteuerung_backend.state.notifications import notifications, Notification, ErrorNr
from modellsteuerung_backend.utils import Level


def json_route(func):
    async def wrapper(*args, **kwargs):
        return web.json_response(await func(*args, **kwargs), headers={"Access-Control-Allow-Origin": "*"})

    return wrapper


class AioBackend:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes([web.get('/', self.info)])
        self.app.add_routes([web.get('/state', self.state)])
        self.app.add_routes([web.get('/notification', self.notifications)])
        self.app.add_routes([web.delete('/notification/{id}', self.remove_notification)])
        self.app.add_routes([web.get('/key', self.key_status)])
        self.app.add_routes([web.post('/key', self.key_unlock)])

        notifications.add_notification(Notification(
            id=0,
            level=Level.INFO,
            start_time=time.time(),
            title="Willkommen",
            description="Willkommen zur Modellsteuerung",
            location="Backend",
            errornr=ErrorNr.WELCOME,
            possible_sources=["Backend"]
        ))

    async def run(self, host, port):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()

    @json_route
    async def info(self, request):
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        return {
            "project": "modellsteuerung_backend",
            "version": "0.0.1",
            "description": "Backend for the ft-seilbahn-project",
            "author": "ft-seilbahn-project",
            "contact": "christian.bergschneider@gmx.de",
            "license": "MIT",
            "time": time.time(),
            "commit": commit,
        }

    @json_route
    async def state(self, request):
        state = use_state()
        controller = use_state_machine()

        return {
            "name": controller.current_state.name,
            "is_locked": state.is_locked,
            "is_warn": state.is_warn,
            "is_fatal": state.is_fatal,
            "can_drive_auto": state.can_drive_auto,
            "can_drive_manual": state.can_drive_manual,
            "speed": desk.speed_dial.value,
        }

    @json_route
    async def notifications(self, request):
        return [x.to_json() for x in notifications.get_notifications()]

    @json_route
    async def remove_notification(self, request):
        identifier = int(request.match_info["id"])
        notifications.remove_notification_by_id(identifier)
        return {
            "success": True,
        }

    @json_route
    async def key_status(self, request):
        return {
            "is_pulled": key.last_state,
            "is_verified": key.unlocked or time.time() - key.can_unlock_start < 30,
            "username": key.current_key_user or "",
        }

    @json_route
    async def key_unlock(self, request: web.Request):
        data = await request.json()
        result = key.unlock_key_for_user(data["username"], data["id"], data["hmac"])
        return {
            "success": result,
        }
