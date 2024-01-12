from modellsteuerung_backend.hardware.io import Input
from modellsteuerung_backend.hardware.modifiers.emergency.abstract import EmergencyChecker, EmergencyPrefab
from modellsteuerung_backend.hardware.modifiers.emergency.impl.SwitchChecker import SwitchChecker
from modellsteuerung_backend.state.notifications import ErrorNr

PREFAB_ES_BASE = EmergencyPrefab(
    title="Not-Aus",
    description="Der Not-Aus wurde betätigt.",
    location="Doppelmayr-Pult",
    errornr=ErrorNr.DOPPELMAYR_EMERGENCY_STOP,
    possible_sources=["Not-Aus-Schalter"]
)

checkers: list[tuple[EmergencyChecker, EmergencyPrefab]] = [
    (
        SwitchChecker(Input.DESK_EMERGENCY_STOP, True),
        PREFAB_ES_BASE.copy(possible_sources=["Not-Aus-Schalter"])
    ),
    (
        SwitchChecker(Input.DESK_EMERGENCY_STOP_STATION_MODE, True),
        PREFAB_ES_BASE.copy(possible_sources=["Not-Aus-Schalter (SB)"])
    ),
    (
        SwitchChecker(Input.DESK_HALT, True),
        PREFAB_ES_BASE.copy(possible_sources=["Halt-Schalter"]))

]
