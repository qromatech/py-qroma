# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qroma-types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='qroma-types.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11qroma-types.proto\"1\n\x10Qroma_LogMessage\x12\x0c\n\x04tick\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t*`\n\x0eQroma_LogLevel\x12\x10\n\x0cLogLevel_All\x10\x00\x12\x11\n\rLogLevel_Info\x10\n\x12\x12\n\x0eLogLevel_Error\x10\x64\x12\x15\n\x10LogLevel_Nothing\x10\xff\x01*\xac\x01\n\x13Qroma_DebugCommMode\x12\x18\n\x14\x44\x65\x62ugCommMode_NotSet\x10\x00\x12\x16\n\x12\x44\x65\x62ugCommMode_None\x10\x01\x12\x1c\n\x18\x44\x65\x62ugCommMode_SerialOnly\x10\x02\x12\x1f\n\x1b\x44\x65\x62ugCommMode_BluetoothOnly\x10\x03\x12$\n DebugCommMode_SerialAndBluetooth\x10\x04\x62\x06proto3'
)

_QROMA_LOGLEVEL = _descriptor.EnumDescriptor(
  name='Qroma_LogLevel',
  full_name='Qroma_LogLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LogLevel_All', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LogLevel_Info', index=1, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LogLevel_Error', index=2, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LogLevel_Nothing', index=3, number=255,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=72,
  serialized_end=168,
)
_sym_db.RegisterEnumDescriptor(_QROMA_LOGLEVEL)

Qroma_LogLevel = enum_type_wrapper.EnumTypeWrapper(_QROMA_LOGLEVEL)
_QROMA_DEBUGCOMMMODE = _descriptor.EnumDescriptor(
  name='Qroma_DebugCommMode',
  full_name='Qroma_DebugCommMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DebugCommMode_NotSet', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DebugCommMode_None', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DebugCommMode_SerialOnly', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DebugCommMode_BluetoothOnly', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DebugCommMode_SerialAndBluetooth', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=171,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_QROMA_DEBUGCOMMMODE)

Qroma_DebugCommMode = enum_type_wrapper.EnumTypeWrapper(_QROMA_DEBUGCOMMMODE)
LogLevel_All = 0
LogLevel_Info = 10
LogLevel_Error = 100
LogLevel_Nothing = 255
DebugCommMode_NotSet = 0
DebugCommMode_None = 1
DebugCommMode_SerialOnly = 2
DebugCommMode_BluetoothOnly = 3
DebugCommMode_SerialAndBluetooth = 4



_QROMA_LOGMESSAGE = _descriptor.Descriptor(
  name='Qroma_LogMessage',
  full_name='Qroma_LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick', full_name='Qroma_LogMessage.tick', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Qroma_LogMessage.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['Qroma_LogMessage'] = _QROMA_LOGMESSAGE
DESCRIPTOR.enum_types_by_name['Qroma_LogLevel'] = _QROMA_LOGLEVEL
DESCRIPTOR.enum_types_by_name['Qroma_DebugCommMode'] = _QROMA_DEBUGCOMMMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Qroma_LogMessage = _reflection.GeneratedProtocolMessageType('Qroma_LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _QROMA_LOGMESSAGE,
  '__module__' : 'qroma_types_pb2'
  # @@protoc_insertion_point(class_scope:Qroma_LogMessage)
  })
_sym_db.RegisterMessage(Qroma_LogMessage)


# @@protoc_insertion_point(module_scope)