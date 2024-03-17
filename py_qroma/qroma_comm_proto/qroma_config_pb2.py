# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qroma-config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import qroma_types_pb2 as qroma__types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='qroma-config.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12qroma-config.proto\x1a\x11qroma-types.proto\"W\n\x17QromaCommSerialIoConfig\x12\x10\n\x08\x62\x61udRate\x18\x01 \x01(\r\x12\x14\n\x0crxBufferSize\x18\x02 \x01(\r\x12\x14\n\x0ctxBufferSize\x18\x03 \x01(\r\"B\n\x1fQromaCommSerialProcessingConfig\x12\x1f\n\x17msDelayInProcessingLoop\x18\x01 \x01(\r\";\n\x16QromaCoreLoggingConfig\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\"^\n\x16HeartbeatConfiguration\x12%\n\rheartbeatType\x18\x01 \x01(\x0e\x32\x0e.HeartbeatType\x12\x1d\n\x15heartbeatIntervalInMs\x18\x02 \x01(\r\"y\n QromaCoreManagementConfiguration\x12\x1c\n\x14projectLoopDelayInMs\x18\x01 \x01(\r\x12\x37\n\x16heartbeatConfiguration\x18\x02 \x01(\x0b\x32\x17.HeartbeatConfiguration\"\xf2\x01\n\x0fQromaCoreConfig\x12\x30\n\x0eserialIoConfig\x18\x01 \x01(\x0b\x32\x18.QromaCommSerialIoConfig\x12@\n\x16serialProcessingConfig\x18\x02 \x01(\x0b\x32 .QromaCommSerialProcessingConfig\x12.\n\rloggingConfig\x18\x03 \x01(\x0b\x32\x17.QromaCoreLoggingConfig\x12;\n\x10managementConfig\x18\x04 \x01(\x0b\x32!.QromaCoreManagementConfigurationb\x06proto3'
  ,
  dependencies=[qroma__types__pb2.DESCRIPTOR,])




_QROMACOMMSERIALIOCONFIG = _descriptor.Descriptor(
  name='QromaCommSerialIoConfig',
  full_name='QromaCommSerialIoConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='baudRate', full_name='QromaCommSerialIoConfig.baudRate', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rxBufferSize', full_name='QromaCommSerialIoConfig.rxBufferSize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='txBufferSize', full_name='QromaCommSerialIoConfig.txBufferSize', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=41,
  serialized_end=128,
)


_QROMACOMMSERIALPROCESSINGCONFIG = _descriptor.Descriptor(
  name='QromaCommSerialProcessingConfig',
  full_name='QromaCommSerialProcessingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msDelayInProcessingLoop', full_name='QromaCommSerialProcessingConfig.msDelayInProcessingLoop', index=0,
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
  serialized_start=130,
  serialized_end=196,
)


_QROMACORELOGGINGCONFIG = _descriptor.Descriptor(
  name='QromaCoreLoggingConfig',
  full_name='QromaCoreLoggingConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logLevel', full_name='QromaCoreLoggingConfig.logLevel', index=0,
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
  serialized_start=198,
  serialized_end=257,
)


_HEARTBEATCONFIGURATION = _descriptor.Descriptor(
  name='HeartbeatConfiguration',
  full_name='HeartbeatConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeatType', full_name='HeartbeatConfiguration.heartbeatType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeatIntervalInMs', full_name='HeartbeatConfiguration.heartbeatIntervalInMs', index=1,
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
  serialized_start=259,
  serialized_end=353,
)


_QROMACOREMANAGEMENTCONFIGURATION = _descriptor.Descriptor(
  name='QromaCoreManagementConfiguration',
  full_name='QromaCoreManagementConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='projectLoopDelayInMs', full_name='QromaCoreManagementConfiguration.projectLoopDelayInMs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heartbeatConfiguration', full_name='QromaCoreManagementConfiguration.heartbeatConfiguration', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=355,
  serialized_end=476,
)


_QROMACORECONFIG = _descriptor.Descriptor(
  name='QromaCoreConfig',
  full_name='QromaCoreConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialIoConfig', full_name='QromaCoreConfig.serialIoConfig', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialProcessingConfig', full_name='QromaCoreConfig.serialProcessingConfig', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loggingConfig', full_name='QromaCoreConfig.loggingConfig', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='managementConfig', full_name='QromaCoreConfig.managementConfig', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=479,
  serialized_end=721,
)

_QROMACORELOGGINGCONFIG.fields_by_name['logLevel'].enum_type = qroma__types__pb2._QROMA_LOGLEVEL
_HEARTBEATCONFIGURATION.fields_by_name['heartbeatType'].enum_type = qroma__types__pb2._HEARTBEATTYPE
_QROMACOREMANAGEMENTCONFIGURATION.fields_by_name['heartbeatConfiguration'].message_type = _HEARTBEATCONFIGURATION
_QROMACORECONFIG.fields_by_name['serialIoConfig'].message_type = _QROMACOMMSERIALIOCONFIG
_QROMACORECONFIG.fields_by_name['serialProcessingConfig'].message_type = _QROMACOMMSERIALPROCESSINGCONFIG
_QROMACORECONFIG.fields_by_name['loggingConfig'].message_type = _QROMACORELOGGINGCONFIG
_QROMACORECONFIG.fields_by_name['managementConfig'].message_type = _QROMACOREMANAGEMENTCONFIGURATION
DESCRIPTOR.message_types_by_name['QromaCommSerialIoConfig'] = _QROMACOMMSERIALIOCONFIG
DESCRIPTOR.message_types_by_name['QromaCommSerialProcessingConfig'] = _QROMACOMMSERIALPROCESSINGCONFIG
DESCRIPTOR.message_types_by_name['QromaCoreLoggingConfig'] = _QROMACORELOGGINGCONFIG
DESCRIPTOR.message_types_by_name['HeartbeatConfiguration'] = _HEARTBEATCONFIGURATION
DESCRIPTOR.message_types_by_name['QromaCoreManagementConfiguration'] = _QROMACOREMANAGEMENTCONFIGURATION
DESCRIPTOR.message_types_by_name['QromaCoreConfig'] = _QROMACORECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QromaCommSerialIoConfig = _reflection.GeneratedProtocolMessageType('QromaCommSerialIoConfig', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOMMSERIALIOCONFIG,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:QromaCommSerialIoConfig)
  })
_sym_db.RegisterMessage(QromaCommSerialIoConfig)

QromaCommSerialProcessingConfig = _reflection.GeneratedProtocolMessageType('QromaCommSerialProcessingConfig', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOMMSERIALPROCESSINGCONFIG,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:QromaCommSerialProcessingConfig)
  })
_sym_db.RegisterMessage(QromaCommSerialProcessingConfig)

QromaCoreLoggingConfig = _reflection.GeneratedProtocolMessageType('QromaCoreLoggingConfig', (_message.Message,), {
  'DESCRIPTOR' : _QROMACORELOGGINGCONFIG,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:QromaCoreLoggingConfig)
  })
_sym_db.RegisterMessage(QromaCoreLoggingConfig)

HeartbeatConfiguration = _reflection.GeneratedProtocolMessageType('HeartbeatConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _HEARTBEATCONFIGURATION,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatConfiguration)
  })
_sym_db.RegisterMessage(HeartbeatConfiguration)

QromaCoreManagementConfiguration = _reflection.GeneratedProtocolMessageType('QromaCoreManagementConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _QROMACOREMANAGEMENTCONFIGURATION,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:QromaCoreManagementConfiguration)
  })
_sym_db.RegisterMessage(QromaCoreManagementConfiguration)

QromaCoreConfig = _reflection.GeneratedProtocolMessageType('QromaCoreConfig', (_message.Message,), {
  'DESCRIPTOR' : _QROMACORECONFIG,
  '__module__' : 'qroma_config_pb2'
  # @@protoc_insertion_point(class_scope:QromaCoreConfig)
  })
_sym_db.RegisterMessage(QromaCoreConfig)


# @@protoc_insertion_point(module_scope)
