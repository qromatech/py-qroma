# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qroma-comm-config-commands.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import qroma_types_pb2 as qroma__types__pb2
from . import qroma_config_pb2 as qroma__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n qroma-comm-config-commands.proto\x1a\x11qroma-types.proto\x1a\x12qroma-config.proto\",\n\x16RequestQromaCommConfig\x12\x12\n\nignoreThis\x18\x01 \x01(\r\"4\n\x1eRequestQromaCommSerialIoConfig\x12\x12\n\nignoreThis\x18\x01 \x01(\r\"5\n\x1fRequestQromaCommReportingConfig\x12\x12\n\nignoreThis\x18\x01 \x01(\r\"7\n\x12SetLogLevelRequest\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\"8\n\x13SetLogLevelResponse\x12!\n\x08logLevel\x18\x01 \x01(\x0e\x32\x0f.Qroma_LogLevel\"<\n\x1bSetHeartbeatIntervalRequest\x12\x1d\n\x15heartbeatIntervalInMs\x18\x01 \x01(\r\"=\n\x1cSetHeartbeatIntervalResponse\x12\x1d\n\x15heartbeatIntervalInMs\x18\x01 \x01(\r\"\xe0\x02\n\x16QromaCommConfigCommand\x12\x39\n\x16requestQromaCommConfig\x18\x01 \x01(\x0b\x32\x17.RequestQromaCommConfigH\x00\x12I\n\x1erequestQromaCommSerialIoConfig\x18\x02 \x01(\x0b\x32\x1f.RequestQromaCommSerialIoConfigH\x00\x12K\n\x1frequestQromaCommReportingConfig\x18\x03 \x01(\x0b\x32 .RequestQromaCommReportingConfigH\x00\x12*\n\x0bsetLogLevel\x18\x04 \x01(\x0b\x32\x13.SetLogLevelRequestH\x00\x12<\n\x14setHeartbeatInterval\x18\x05 \x01(\x0b\x32\x1c.SetHeartbeatIntervalRequestH\x00\x42\t\n\x07\x63ommand\"\xba\x02\n\x17QromaCommConfigResponse\x12+\n\x0fqromaCommConfig\x18\x01 \x01(\x0b\x32\x10.QromaCommConfigH\x00\x12;\n\x17qromaCommSerialIoConfig\x18\x02 \x01(\x0b\x32\x18.QromaCommSerialIoConfigH\x00\x12=\n\x18qromaCommReportingConfig\x18\x03 \x01(\x0b\x32\x19.QromaCommReportingConfigH\x00\x12+\n\x0bsetLogLevel\x18\x04 \x01(\x0b\x32\x14.SetLogLevelResponseH\x00\x12=\n\x14setHeartbeatInterval\x18\x05 \x01(\x0b\x32\x1d.SetHeartbeatIntervalResponseH\x00\x42\n\n\x08responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'qroma_comm_config_commands_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUESTQROMACOMMCONFIG']._serialized_start=75
  _globals['_REQUESTQROMACOMMCONFIG']._serialized_end=119
  _globals['_REQUESTQROMACOMMSERIALIOCONFIG']._serialized_start=121
  _globals['_REQUESTQROMACOMMSERIALIOCONFIG']._serialized_end=173
  _globals['_REQUESTQROMACOMMREPORTINGCONFIG']._serialized_start=175
  _globals['_REQUESTQROMACOMMREPORTINGCONFIG']._serialized_end=228
  _globals['_SETLOGLEVELREQUEST']._serialized_start=230
  _globals['_SETLOGLEVELREQUEST']._serialized_end=285
  _globals['_SETLOGLEVELRESPONSE']._serialized_start=287
  _globals['_SETLOGLEVELRESPONSE']._serialized_end=343
  _globals['_SETHEARTBEATINTERVALREQUEST']._serialized_start=345
  _globals['_SETHEARTBEATINTERVALREQUEST']._serialized_end=405
  _globals['_SETHEARTBEATINTERVALRESPONSE']._serialized_start=407
  _globals['_SETHEARTBEATINTERVALRESPONSE']._serialized_end=468
  _globals['_QROMACOMMCONFIGCOMMAND']._serialized_start=471
  _globals['_QROMACOMMCONFIGCOMMAND']._serialized_end=823
  _globals['_QROMACOMMCONFIGRESPONSE']._serialized_start=826
  _globals['_QROMACOMMCONFIGRESPONSE']._serialized_end=1140
# @@protoc_insertion_point(module_scope)
