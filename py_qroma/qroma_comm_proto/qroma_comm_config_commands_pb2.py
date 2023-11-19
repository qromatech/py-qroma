# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qroma-comm-config-commands.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qroma_types_pb2 as qroma__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qroma-comm-config-commands.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n qroma-comm-config-commands.proto\x1a\x11qroma-types.proto\",\n\x16RequestQromaCommConfig\x12\x12\n\nignoreThis\x18\x01 \x01(\r\"S\n\x0fQromaCommConfig\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\x12\x1d\n\x15heartbeatIntervalInMs\x18\x02 \x01(\r\"7\n\x12SetLogLevelRequest\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\"8\n\x13SetLogLevelResponse\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\"<\n\x1bSetHeartbeatIntervalRequest\x12\x1d\n\x15heartbeatIntervalInMs\x18\x01 \x01(\r\"=\n\x1cSetHeartbeatIntervalResponse\x12\x1d\n\x15heartbeatIntervalInMs\x18\x01 \x01(\r\"\xc8\x01\n\x16QromaCommConfigCommand\x12\x39\n\x16requestQromaCommConfig\x18\x01 \x01(\x0b\x32\x17.RequestQromaCommConfigH\x00\x12*\n\x0bsetLogLevel\x18\x02 \x01(\x0b\x32\x13.SetLogLevelRequestH\x00\x12<\n\x14setHeartbeatInterval\x18\x03 \x01(\x0b\x32\x1c.SetHeartbeatIntervalRequestH\x00\x42\t\n\x07\x63ommand\"\xbe\x01\n\x17QromaCommConfigResponse\x12+\n\x0fqromaCommConfig\x18\x01 \x01(\x0b\x32\x10.QromaCommConfigH\x00\x12+\n\x0bsetLogLevel\x18\x02 \x01(\x0b\x32\x14.SetLogLevelResponseH\x00\x12=\n\x14setHeartbeatInterval\x18\x03 \x01(\x0b\x32\x1d.SetHeartbeatIntervalResponseH\x00\x42\n\n\x08responseb\x06proto3'
  ,
  dependencies=[qroma__types__pb2.DESCRIPTOR,])




_REQUESTQROMACOMMCONFIG = _descriptor.Descriptor(
  name='RequestQromaCommConfig',
  full_name='RequestQromaCommConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignoreThis', full_name='RequestQromaCommConfig.ignoreThis', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=55,
  serialized_end=99,
)


_QROMACOMMCONFIG = _descriptor.Descriptor(
  name='QromaCommConfig',
  full_name='QromaCommConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logLevel', full_name='QromaCommConfig.logLevel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeatIntervalInMs', full_name='QromaCommConfig.heartbeatIntervalInMs', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=101,
  serialized_end=184,
)


_SETLOGLEVELREQUEST = _descriptor.Descriptor(
  name='SetLogLevelRequest',
  full_name='SetLogLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logLevel', full_name='SetLogLevelRequest.logLevel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=186,
  serialized_end=241,
)


_SETLOGLEVELRESPONSE = _descriptor.Descriptor(
  name='SetLogLevelResponse',
  full_name='SetLogLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logLevel', full_name='SetLogLevelResponse.logLevel', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=243,
  serialized_end=299,
)


_SETHEARTBEATINTERVALREQUEST = _descriptor.Descriptor(
  name='SetHeartbeatIntervalRequest',
  full_name='SetHeartbeatIntervalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeatIntervalInMs', full_name='SetHeartbeatIntervalRequest.heartbeatIntervalInMs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=301,
  serialized_end=361,
)


_SETHEARTBEATINTERVALRESPONSE = _descriptor.Descriptor(
  name='SetHeartbeatIntervalResponse',
  full_name='SetHeartbeatIntervalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeatIntervalInMs', full_name='SetHeartbeatIntervalResponse.heartbeatIntervalInMs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=363,
  serialized_end=424,
)


_QROMACOMMCONFIGCOMMAND = _descriptor.Descriptor(
  name='QromaCommConfigCommand',
  full_name='QromaCommConfigCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestQromaCommConfig', full_name='QromaCommConfigCommand.requestQromaCommConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setLogLevel', full_name='QromaCommConfigCommand.setLogLevel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setHeartbeatInterval', full_name='QromaCommConfigCommand.setHeartbeatInterval', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='command', full_name='QromaCommConfigCommand.command',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=427,
  serialized_end=627,
)


_QROMACOMMCONFIGRESPONSE = _descriptor.Descriptor(
  name='QromaCommConfigResponse',
  full_name='QromaCommConfigResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='qromaCommConfig', full_name='QromaCommConfigResponse.qromaCommConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setLogLevel', full_name='QromaCommConfigResponse.setLogLevel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='setHeartbeatInterval', full_name='QromaCommConfigResponse.setHeartbeatInterval', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='response', full_name='QromaCommConfigResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=630,
  serialized_end=820,
)

_QROMACOMMCONFIG.fields_by_name['logLevel'].enum_type = qroma__types__pb2._QROMA_LOGLEVEL
_SETLOGLEVELREQUEST.fields_by_name['logLevel'].enum_type = qroma__types__pb2._QROMA_LOGLEVEL
_SETLOGLEVELRESPONSE.fields_by_name['logLevel'].enum_type = qroma__types__pb2._QROMA_LOGLEVEL
_QROMACOMMCONFIGCOMMAND.fields_by_name['requestQromaCommConfig'].message_type = _REQUESTQROMACOMMCONFIG
_QROMACOMMCONFIGCOMMAND.fields_by_name['setLogLevel'].message_type = _SETLOGLEVELREQUEST
_QROMACOMMCONFIGCOMMAND.fields_by_name['setHeartbeatInterval'].message_type = _SETHEARTBEATINTERVALREQUEST
_QROMACOMMCONFIGCOMMAND.oneofs_by_name['command'].fields.append(
  _QROMACOMMCONFIGCOMMAND.fields_by_name['requestQromaCommConfig'])
_QROMACOMMCONFIGCOMMAND.fields_by_name['requestQromaCommConfig'].containing_oneof = _QROMACOMMCONFIGCOMMAND.oneofs_by_name['command']
_QROMACOMMCONFIGCOMMAND.oneofs_by_name['command'].fields.append(
  _QROMACOMMCONFIGCOMMAND.fields_by_name['setLogLevel'])
_QROMACOMMCONFIGCOMMAND.fields_by_name['setLogLevel'].containing_oneof = _QROMACOMMCONFIGCOMMAND.oneofs_by_name['command']
_QROMACOMMCONFIGCOMMAND.oneofs_by_name['command'].fields.append(
  _QROMACOMMCONFIGCOMMAND.fields_by_name['setHeartbeatInterval'])
_QROMACOMMCONFIGCOMMAND.fields_by_name['setHeartbeatInterval'].containing_oneof = _QROMACOMMCONFIGCOMMAND.oneofs_by_name['command']
_QROMACOMMCONFIGRESPONSE.fields_by_name['qromaCommConfig'].message_type = _QROMACOMMCONFIG
_QROMACOMMCONFIGRESPONSE.fields_by_name['setLogLevel'].message_type = _SETLOGLEVELRESPONSE
_QROMACOMMCONFIGRESPONSE.fields_by_name['setHeartbeatInterval'].message_type = _SETHEARTBEATINTERVALRESPONSE
_QROMACOMMCONFIGRESPONSE.oneofs_by_name['response'].fields.append(
  _QROMACOMMCONFIGRESPONSE.fields_by_name['qromaCommConfig'])
_QROMACOMMCONFIGRESPONSE.fields_by_name['qromaCommConfig'].containing_oneof = _QROMACOMMCONFIGRESPONSE.oneofs_by_name['response']
_QROMACOMMCONFIGRESPONSE.oneofs_by_name['response'].fields.append(
  _QROMACOMMCONFIGRESPONSE.fields_by_name['setLogLevel'])
_QROMACOMMCONFIGRESPONSE.fields_by_name['setLogLevel'].containing_oneof = _QROMACOMMCONFIGRESPONSE.oneofs_by_name['response']
_QROMACOMMCONFIGRESPONSE.oneofs_by_name['response'].fields.append(
  _QROMACOMMCONFIGRESPONSE.fields_by_name['setHeartbeatInterval'])
_QROMACOMMCONFIGRESPONSE.fields_by_name['setHeartbeatInterval'].containing_oneof = _QROMACOMMCONFIGRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['RequestQromaCommConfig'] = _REQUESTQROMACOMMCONFIG
DESCRIPTOR.message_types_by_name['QromaCommConfig'] = _QROMACOMMCONFIG
DESCRIPTOR.message_types_by_name['SetLogLevelRequest'] = _SETLOGLEVELREQUEST
DESCRIPTOR.message_types_by_name['SetLogLevelResponse'] = _SETLOGLEVELRESPONSE
DESCRIPTOR.message_types_by_name['SetHeartbeatIntervalRequest'] = _SETHEARTBEATINTERVALREQUEST
DESCRIPTOR.message_types_by_name['SetHeartbeatIntervalResponse'] = _SETHEARTBEATINTERVALRESPONSE
DESCRIPTOR.message_types_by_name['QromaCommConfigCommand'] = _QROMACOMMCONFIGCOMMAND
DESCRIPTOR.message_types_by_name['QromaCommConfigResponse'] = _QROMACOMMCONFIGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestQromaCommConfig = _reflection.GeneratedProtocolMessageType('RequestQromaCommConfig', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTQROMACOMMCONFIG,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:RequestQromaCommConfig)
  })
_sym_db.RegisterMessage(RequestQromaCommConfig)

QromaCommConfig = _reflection.GeneratedProtocolMessageType('QromaCommConfig', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOMMCONFIG,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:QromaCommConfig)
  })
_sym_db.RegisterMessage(QromaCommConfig)

SetLogLevelRequest = _reflection.GeneratedProtocolMessageType('SetLogLevelRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETLOGLEVELREQUEST,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:SetLogLevelRequest)
  })
_sym_db.RegisterMessage(SetLogLevelRequest)

SetLogLevelResponse = _reflection.GeneratedProtocolMessageType('SetLogLevelResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETLOGLEVELRESPONSE,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:SetLogLevelResponse)
  })
_sym_db.RegisterMessage(SetLogLevelResponse)

SetHeartbeatIntervalRequest = _reflection.GeneratedProtocolMessageType('SetHeartbeatIntervalRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETHEARTBEATINTERVALREQUEST,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:SetHeartbeatIntervalRequest)
  })
_sym_db.RegisterMessage(SetHeartbeatIntervalRequest)

SetHeartbeatIntervalResponse = _reflection.GeneratedProtocolMessageType('SetHeartbeatIntervalResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETHEARTBEATINTERVALRESPONSE,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:SetHeartbeatIntervalResponse)
  })
_sym_db.RegisterMessage(SetHeartbeatIntervalResponse)

QromaCommConfigCommand = _reflection.GeneratedProtocolMessageType('QromaCommConfigCommand', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOMMCONFIGCOMMAND,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:QromaCommConfigCommand)
  })
_sym_db.RegisterMessage(QromaCommConfigCommand)

QromaCommConfigResponse = _reflection.GeneratedProtocolMessageType('QromaCommConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOMMCONFIGRESPONSE,
  '__module__' : 'qroma_comm_config_commands_pb2'
  # @@protoc_insertion_point(class_scope:QromaCommConfigResponse)
  })
_sym_db.RegisterMessage(QromaCommConfigResponse)


# @@protoc_insertion_point(module_scope)
