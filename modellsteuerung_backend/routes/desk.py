from dataclasses import dataclass

from fastapi import APIRouter

from modellsteuerung_backend.hardware import desk
from modellsteuerung_backend.state.drivectrlstate import Direction, Speed

router = APIRouter(
    prefix="/desk",
    tags=["desk"],
)


@dataclass
class Desk:
    speed_dial: Speed
    emergency_stop: bool
    started: bool
    signal: bool
    on: bool
    station_occupied: bool
    service_mode: bool
    direction: Direction
    set_ok: bool


@router.get("/")
async def get_desk() -> Desk:
    return Desk(
        speed_dial=desk.speed_dial,
        emergency_stop=desk.emergency_stop,
        started=desk.started,
        signal=desk.signal,
        on=desk.on,
        station_occupied=desk.station_occupied,
        service_mode=desk.service_mode,
        direction=desk.direction[0],
        set_ok=desk.set_ok,
    )
