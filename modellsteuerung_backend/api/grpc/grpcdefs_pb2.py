# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modellsteuerung_backend/api/grpc/grpcdefs.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/modellsteuerung_backend/api/grpc/grpcdefs.proto\"\x06\n\x04Void\"\x8d\x01\n\x04Info\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x05 \x01(\t\x12\x0f\n\x07license\x18\x06 \x01(\t\x12\x0c\n\x04time\x18\x07 \x01(\x02\x12\x0e\n\x06\x63ommit\x18\x08 \x01(\t\"\x94\x01\n\x05State\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tis_locked\x18\x02 \x01(\x08\x12\x16\n\x0e\x63\x61n_drive_auto\x18\x03 \x01(\x08\x12\x18\n\x10\x63\x61n_drive_manual\x18\x04 \x01(\x08\x12\x10\n\x08is_fatal\x18\x05 \x01(\x08\x12\x0f\n\x07is_warn\x18\x06 \x01(\x08\x12\x15\n\x05speed\x18\x07 \x01(\x0e\x32\x06.Speed\"\xa7\x01\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\x05level\x18\x02 \x01(\x0e\x32\x06.Level\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x12\n\nstart_time\x18\x06 \x01(\x02\x12\x10\n\x08\x65rrorrnr\x18\x07 \x01(\t\x12\x18\n\x10possible_sources\x18\x08 \x03(\t\"8\n\x10NotificationList\x12$\n\rnotifications\x18\x01 \x03(\x0b\x32\r.Notification*1\n\x05Speed\x12\x08\n\x04STOP\x10\x00\x12\x08\n\x04SLOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04\x46\x41ST\x10\x03*)\n\x05Level\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x46\x41TAL\x10\x02\x32h\n\x07\x42\x61\x63kend\x12\x16\n\x04info\x12\x05.Void\x1a\x05.Info\"\x00\x12\x18\n\x05state\x12\x05.Void\x1a\x06.State\"\x00\x12+\n\rnotifications\x12\x05.Void\x1a\x11.NotificationList\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'modellsteuerung_backend.api.grpc.grpcdefs_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SPEED']._serialized_start=582
  _globals['_SPEED']._serialized_end=631
  _globals['_LEVEL']._serialized_start=633
  _globals['_LEVEL']._serialized_end=674
  _globals['_VOID']._serialized_start=51
  _globals['_VOID']._serialized_end=57
  _globals['_INFO']._serialized_start=60
  _globals['_INFO']._serialized_end=201
  _globals['_STATE']._serialized_start=204
  _globals['_STATE']._serialized_end=352
  _globals['_NOTIFICATION']._serialized_start=355
  _globals['_NOTIFICATION']._serialized_end=522
  _globals['_NOTIFICATIONLIST']._serialized_start=524
  _globals['_NOTIFICATIONLIST']._serialized_end=580
  _globals['_BACKEND']._serialized_start=676
  _globals['_BACKEND']._serialized_end=780
# @@protoc_insertion_point(module_scope)