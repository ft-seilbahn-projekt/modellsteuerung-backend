from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Speed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP: _ClassVar[Speed]
    SLOW: _ClassVar[Speed]
    MEDIUM: _ClassVar[Speed]
    FAST: _ClassVar[Speed]

class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFO: _ClassVar[Level]
    WARNING: _ClassVar[Level]
    FATAL: _ClassVar[Level]
STOP: Speed
SLOW: Speed
MEDIUM: Speed
FAST: Speed
INFO: Level
WARNING: Level
FATAL: Level

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Info(_message.Message):
    __slots__ = ("project", "version", "description", "author", "contact", "license", "time", "commit")
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_FIELD_NUMBER: _ClassVar[int]
    project: str
    version: str
    description: str
    author: str
    contact: str
    license: str
    time: float
    commit: str
    def __init__(self, project: _Optional[str] = ..., version: _Optional[str] = ..., description: _Optional[str] = ..., author: _Optional[str] = ..., contact: _Optional[str] = ..., license: _Optional[str] = ..., time: _Optional[float] = ..., commit: _Optional[str] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("name", "is_locked", "can_drive_auto", "can_drive_manual", "is_fatal", "is_warn", "speed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    CAN_DRIVE_AUTO_FIELD_NUMBER: _ClassVar[int]
    CAN_DRIVE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    IS_FATAL_FIELD_NUMBER: _ClassVar[int]
    IS_WARN_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_locked: bool
    can_drive_auto: bool
    can_drive_manual: bool
    is_fatal: bool
    is_warn: bool
    speed: Speed
    def __init__(self, name: _Optional[str] = ..., is_locked: bool = ..., can_drive_auto: bool = ..., can_drive_manual: bool = ..., is_fatal: bool = ..., is_warn: bool = ..., speed: _Optional[_Union[Speed, str]] = ...) -> None: ...

class Notification(_message.Message):
    __slots__ = ("id", "level", "title", "description", "location", "start_time", "errorrnr", "possible_sources")
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ERRORRNR_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_SOURCES_FIELD_NUMBER: _ClassVar[int]
    id: int
    level: Level
    title: str
    description: str
    location: str
    start_time: float
    errorrnr: str
    possible_sources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., level: _Optional[_Union[Level, str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., location: _Optional[str] = ..., start_time: _Optional[float] = ..., errorrnr: _Optional[str] = ..., possible_sources: _Optional[_Iterable[str]] = ...) -> None: ...

class NotificationList(_message.Message):
    __slots__ = ("notifications",)
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Notification]
    def __init__(self, notifications: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ...) -> None: ...
