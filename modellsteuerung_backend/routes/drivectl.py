from fastapi import APIRouter

from modellsteuerung_backend.state.drivectrlstate import DriveCtrlState, drive_ctrl_state, Direction

router = APIRouter(
    prefix="/drivectl",
    tags=["drivectl"],
)


@router.get("/state")
async def get_state() -> DriveCtrlState:
    """
    Get the current state of the drive control.
    """
    return drive_ctrl_state.get_state()


@router.post("/set-speed")
async def set_speed(speed: int):
    """
    Set the speed of the drive control.
    """
    drive_ctrl_state.set_speed(speed)


@router.post("/set-direction")
async def set_direction(direction: Direction):
    """
    Set the direction of the drive control.
    """
    drive_ctrl_state.set_direction(direction)


@router.post("/set-emergency-stop")
async def set_emergency_stop(emergency_stop: bool):
    """
    Set the emergency stop of the drive control.
    """
    drive_ctrl_state.set_emergency_stop(emergency_stop)
