from dataclasses import dataclass
from enum import Enum

from modellsteuerung_backend.network.drivectl import InboundDriveCtlPacket
from modellsteuerung_backend.utils import Level


class Direction(str, Enum):
    FORWARDS = "forwards"
    BACKWARDS = "backwards"


class Speed(int, Enum):
    STOP = 0
    SLOW = 1
    MEDIUM = 2
    FAST = 3


@dataclass
class DriveCtrlState:
    direction: Direction = Direction.FORWARDS
    requested_speed: int = 0
    actual_speed: int = 0
    error: Level = None
    emergency_stop: bool = False


class InternalDriveCtrlState:
    def __init__(self):
        self._speed = 0
        self._direction = Direction.FORWARDS
        self._last_incoming_packet: InboundDriveCtlPacket = InboundDriveCtlPacket(b"\x00\x00")
        self._emergency_stop = False

    def set_speed(self, speed: int):
        self._speed = speed
        self.fire()

    def get_speed(self):
        return self._speed

    def set_direction(self, direction: Direction):
        self._direction = direction
        self.fire()

    def set_last_incoming_packet(self, packet: InboundDriveCtlPacket):
        self._last_incoming_packet = packet

    def get_direction(self):
        return self._direction

    def get_emergency_stop(self):
        return self._emergency_stop

    def set_emergency_stop(self, emergency_stop: bool):
        self._emergency_stop = emergency_stop
        self.fire()

    def get_state(self) -> DriveCtrlState:
        return DriveCtrlState(
            direction=self._direction,
            requested_speed=self._speed,
            actual_speed=self._last_incoming_packet.get_speed(),
            error=self._last_incoming_packet.get_error(),
            emergency_stop=self._emergency_stop
        )

    def handle_incoming_packet(self, packet: InboundDriveCtlPacket):
        if packet.get_error() is not Level.INFO:
            self._handle_error(packet.get_error())

        self._last_incoming_packet = packet

    def _handle_error(self, new_error: Level):
        if new_error == Level.FATAL:
            self._speed = Speed.STOP
            self._emergency_stop = True
        elif new_error == Level.WARNING:
            self._speed = Speed.SLOW

    def serialize(self) -> bytes:
        """
        Serializes the state into a byte array.
        :return: The serialized state

        Format:
        a b c c c c c c
        a = direction
        b = emergency stop
        c = speed
        """

        direction = 0
        if self._direction == Direction.BACKWARDS:
            direction = 1

        direction = direction << 7

        if self._emergency_stop:
            direction = direction | 1 << 6

        return bytes([direction | self._speed])

    def fire(self):
        print(self.serialize())
        # TODO: Send to actual drive control


drive_ctrl_state = InternalDriveCtrlState()
