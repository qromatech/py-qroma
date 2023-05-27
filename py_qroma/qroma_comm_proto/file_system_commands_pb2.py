# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file-system-commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='file-system-commands.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x66ile-system-commands.proto\"L\n\x07\x44irItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x0b\x64irItemType\x18\x02 \x01(\x0e\x32\x0c.DirItemType\x12\x10\n\x08\x66ilesize\x18\x03 \x01(\r\"@\n\x08\x46ileData\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x66ilesize\x18\x02 \x01(\r\x12\x10\n\x08\x63hecksum\x18\x03 \x01(\r\";\n\x1cStoreUpcomingFileDataCommand\x12\x1b\n\x08\x66ileData\x18\x01 \x01(\x0b\x32\t.FileData\"b\n\x1dStoreUpcomingFileDataResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x14\n\x0c\x62ytesWritten\x18\x02 \x01(\r\x12\x1a\n\x07\x63ommand\x18\x03 \x01(\x0b\x32\t.FileData\"!\n\rRmFileCommand\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\t\"G\n\x0eRmFileResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12$\n\x0crmDirCommand\x18\x02 \x01(\x0b\x32\x0e.RmFileCommand\")\n\x15ReportFileDataCommand\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"I\n\x16ReportFileDataResponse\x12\x12\n\nfileExists\x18\x01 \x01(\x08\x12\x1b\n\x08\x66ileData\x18\x02 \x01(\x0b\x32\t.FileData\")\n\x16ListDirContentsCommand\x12\x0f\n\x07\x64irPath\x18\x01 \x01(\t\"F\n\x17ListDirContentsResponse\x12\x0f\n\x07\x64irPath\x18\x01 \x01(\t\x12\x1a\n\x08\x64irItems\x18\x02 \x03(\x0b\x32\x08.DirItem\"*\n\x17PrintDirContentsCommand\x12\x0f\n\x07\x64irPath\x18\x01 \x01(\t\"\'\n\x16ResetFilesystemCommand\x12\r\n\x05\x64ummy\x18\x01 \x01(\x08\"*\n\x17ResetFilesystemResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\",\n\x18PrintFileContentsCommand\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\t\"\xb9\x03\n\x11\x46ileSystemCommand\x12;\n\x17printDirContentsCommand\x18\x01 \x01(\x0b\x32\x18.PrintDirContentsCommandH\x00\x12=\n\x18printFileContentsCommand\x18\x02 \x01(\x0b\x32\x19.PrintFileContentsCommandH\x00\x12\'\n\rrmFileCommand\x18\x03 \x01(\x0b\x32\x0e.RmFileCommandH\x00\x12\x45\n\x1cstoreUpcomingFileDataCommand\x18\x06 \x01(\x0b\x32\x1d.StoreUpcomingFileDataCommandH\x00\x12\x37\n\x15reportFileDataCommand\x18\x07 \x01(\x0b\x32\x16.ReportFileDataCommandH\x00\x12\x39\n\x16listDirContentsCommand\x18\x08 \x01(\x0b\x32\x17.ListDirContentsCommandH\x00\x12\x39\n\x16resetFilesystemCommand\x18\t \x01(\x0b\x32\x17.ResetFilesystemCommandH\x00\x42\t\n\x07\x63ommand\"\xc8\x02\n\x12\x46ileSystemResponse\x12(\n\rrmFileCommand\x18\x02 \x01(\x0b\x32\x0f.RmFileResponseH\x00\x12G\n\x1dstoreUpcomingFileDataResponse\x18\x06 \x01(\x0b\x32\x1e.StoreUpcomingFileDataResponseH\x00\x12\x39\n\x16reportFileDataResponse\x18\x07 \x01(\x0b\x32\x17.ReportFileDataResponseH\x00\x12;\n\x17listDirContentsResponse\x18\x08 \x01(\x0b\x32\x18.ListDirContentsResponseH\x00\x12;\n\x17resetFilesystemResponse\x18\t \x01(\x0b\x32\x18.ResetFilesystemResponseH\x00\x42\n\n\x08response*9\n\x0b\x44irItemType\x12\x0f\n\x0b\x44IT_NOT_SET\x10\x00\x12\x0c\n\x08\x44IT_FILE\x10\x01\x12\x0b\n\x07\x44IT_DIR\x10\x02\x62\x06proto3'
)

_DIRITEMTYPE = _descriptor.EnumDescriptor(
  name='DirItemType',
  full_name='DirItemType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DIT_NOT_SET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIT_FILE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIT_DIR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1626,
  serialized_end=1683,
)
_sym_db.RegisterEnumDescriptor(_DIRITEMTYPE)

DirItemType = enum_type_wrapper.EnumTypeWrapper(_DIRITEMTYPE)
DIT_NOT_SET = 0
DIT_FILE = 1
DIT_DIR = 2



_DIRITEM = _descriptor.Descriptor(
  name='DirItem',
  full_name='DirItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DirItem.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dirItemType', full_name='DirItem.dirItemType', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filesize', full_name='DirItem.filesize', index=2,
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
  serialized_start=30,
  serialized_end=106,
)


_FILEDATA = _descriptor.Descriptor(
  name='FileData',
  full_name='FileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='FileData.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filesize', full_name='FileData.filesize', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='FileData.checksum', index=2,
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
  serialized_start=108,
  serialized_end=172,
)


_STOREUPCOMINGFILEDATACOMMAND = _descriptor.Descriptor(
  name='StoreUpcomingFileDataCommand',
  full_name='StoreUpcomingFileDataCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileData', full_name='StoreUpcomingFileDataCommand.fileData', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=174,
  serialized_end=233,
)


_STOREUPCOMINGFILEDATARESPONSE = _descriptor.Descriptor(
  name='StoreUpcomingFileDataResponse',
  full_name='StoreUpcomingFileDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='StoreUpcomingFileDataResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytesWritten', full_name='StoreUpcomingFileDataResponse.bytesWritten', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command', full_name='StoreUpcomingFileDataResponse.command', index=2,
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
  ],
  serialized_start=235,
  serialized_end=333,
)


_RMFILECOMMAND = _descriptor.Descriptor(
  name='RmFileCommand',
  full_name='RmFileCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filePath', full_name='RmFileCommand.filePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=335,
  serialized_end=368,
)


_RMFILERESPONSE = _descriptor.Descriptor(
  name='RmFileResponse',
  full_name='RmFileResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='RmFileResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rmDirCommand', full_name='RmFileResponse.rmDirCommand', index=1,
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
  serialized_start=370,
  serialized_end=441,
)


_REPORTFILEDATACOMMAND = _descriptor.Descriptor(
  name='ReportFileDataCommand',
  full_name='ReportFileDataCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='ReportFileDataCommand.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=443,
  serialized_end=484,
)


_REPORTFILEDATARESPONSE = _descriptor.Descriptor(
  name='ReportFileDataResponse',
  full_name='ReportFileDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileExists', full_name='ReportFileDataResponse.fileExists', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileData', full_name='ReportFileDataResponse.fileData', index=1,
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
  serialized_start=486,
  serialized_end=559,
)


_LISTDIRCONTENTSCOMMAND = _descriptor.Descriptor(
  name='ListDirContentsCommand',
  full_name='ListDirContentsCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dirPath', full_name='ListDirContentsCommand.dirPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=561,
  serialized_end=602,
)


_LISTDIRCONTENTSRESPONSE = _descriptor.Descriptor(
  name='ListDirContentsResponse',
  full_name='ListDirContentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dirPath', full_name='ListDirContentsResponse.dirPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dirItems', full_name='ListDirContentsResponse.dirItems', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=604,
  serialized_end=674,
)


_PRINTDIRCONTENTSCOMMAND = _descriptor.Descriptor(
  name='PrintDirContentsCommand',
  full_name='PrintDirContentsCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dirPath', full_name='PrintDirContentsCommand.dirPath', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=676,
  serialized_end=718,
)


_RESETFILESYSTEMCOMMAND = _descriptor.Descriptor(
  name='ResetFilesystemCommand',
  full_name='ResetFilesystemCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dummy', full_name='ResetFilesystemCommand.dummy', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=720,
  serialized_end=759,
)


_RESETFILESYSTEMRESPONSE = _descriptor.Descriptor(
  name='ResetFilesystemResponse',
  full_name='ResetFilesystemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='ResetFilesystemResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=761,
  serialized_end=803,
)


_PRINTFILECONTENTSCOMMAND = _descriptor.Descriptor(
  name='PrintFileContentsCommand',
  full_name='PrintFileContentsCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filePath', full_name='PrintFileContentsCommand.filePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=805,
  serialized_end=849,
)


_FILESYSTEMCOMMAND = _descriptor.Descriptor(
  name='FileSystemCommand',
  full_name='FileSystemCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='printDirContentsCommand', full_name='FileSystemCommand.printDirContentsCommand', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='printFileContentsCommand', full_name='FileSystemCommand.printFileContentsCommand', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rmFileCommand', full_name='FileSystemCommand.rmFileCommand', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storeUpcomingFileDataCommand', full_name='FileSystemCommand.storeUpcomingFileDataCommand', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reportFileDataCommand', full_name='FileSystemCommand.reportFileDataCommand', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listDirContentsCommand', full_name='FileSystemCommand.listDirContentsCommand', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resetFilesystemCommand', full_name='FileSystemCommand.resetFilesystemCommand', index=6,
      number=9, type=11, cpp_type=10, label=1,
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
      name='command', full_name='FileSystemCommand.command',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=852,
  serialized_end=1293,
)


_FILESYSTEMRESPONSE = _descriptor.Descriptor(
  name='FileSystemResponse',
  full_name='FileSystemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rmFileCommand', full_name='FileSystemResponse.rmFileCommand', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='storeUpcomingFileDataResponse', full_name='FileSystemResponse.storeUpcomingFileDataResponse', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reportFileDataResponse', full_name='FileSystemResponse.reportFileDataResponse', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listDirContentsResponse', full_name='FileSystemResponse.listDirContentsResponse', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resetFilesystemResponse', full_name='FileSystemResponse.resetFilesystemResponse', index=4,
      number=9, type=11, cpp_type=10, label=1,
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
      name='response', full_name='FileSystemResponse.response',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1296,
  serialized_end=1624,
)

_DIRITEM.fields_by_name['dirItemType'].enum_type = _DIRITEMTYPE
_STOREUPCOMINGFILEDATACOMMAND.fields_by_name['fileData'].message_type = _FILEDATA
_STOREUPCOMINGFILEDATARESPONSE.fields_by_name['command'].message_type = _FILEDATA
_RMFILERESPONSE.fields_by_name['rmDirCommand'].message_type = _RMFILECOMMAND
_REPORTFILEDATARESPONSE.fields_by_name['fileData'].message_type = _FILEDATA
_LISTDIRCONTENTSRESPONSE.fields_by_name['dirItems'].message_type = _DIRITEM
_FILESYSTEMCOMMAND.fields_by_name['printDirContentsCommand'].message_type = _PRINTDIRCONTENTSCOMMAND
_FILESYSTEMCOMMAND.fields_by_name['printFileContentsCommand'].message_type = _PRINTFILECONTENTSCOMMAND
_FILESYSTEMCOMMAND.fields_by_name['rmFileCommand'].message_type = _RMFILECOMMAND
_FILESYSTEMCOMMAND.fields_by_name['storeUpcomingFileDataCommand'].message_type = _STOREUPCOMINGFILEDATACOMMAND
_FILESYSTEMCOMMAND.fields_by_name['reportFileDataCommand'].message_type = _REPORTFILEDATACOMMAND
_FILESYSTEMCOMMAND.fields_by_name['listDirContentsCommand'].message_type = _LISTDIRCONTENTSCOMMAND
_FILESYSTEMCOMMAND.fields_by_name['resetFilesystemCommand'].message_type = _RESETFILESYSTEMCOMMAND
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['printDirContentsCommand'])
_FILESYSTEMCOMMAND.fields_by_name['printDirContentsCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['printFileContentsCommand'])
_FILESYSTEMCOMMAND.fields_by_name['printFileContentsCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['rmFileCommand'])
_FILESYSTEMCOMMAND.fields_by_name['rmFileCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['storeUpcomingFileDataCommand'])
_FILESYSTEMCOMMAND.fields_by_name['storeUpcomingFileDataCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['reportFileDataCommand'])
_FILESYSTEMCOMMAND.fields_by_name['reportFileDataCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['listDirContentsCommand'])
_FILESYSTEMCOMMAND.fields_by_name['listDirContentsCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMCOMMAND.oneofs_by_name['command'].fields.append(
  _FILESYSTEMCOMMAND.fields_by_name['resetFilesystemCommand'])
_FILESYSTEMCOMMAND.fields_by_name['resetFilesystemCommand'].containing_oneof = _FILESYSTEMCOMMAND.oneofs_by_name['command']
_FILESYSTEMRESPONSE.fields_by_name['rmFileCommand'].message_type = _RMFILERESPONSE
_FILESYSTEMRESPONSE.fields_by_name['storeUpcomingFileDataResponse'].message_type = _STOREUPCOMINGFILEDATARESPONSE
_FILESYSTEMRESPONSE.fields_by_name['reportFileDataResponse'].message_type = _REPORTFILEDATARESPONSE
_FILESYSTEMRESPONSE.fields_by_name['listDirContentsResponse'].message_type = _LISTDIRCONTENTSRESPONSE
_FILESYSTEMRESPONSE.fields_by_name['resetFilesystemResponse'].message_type = _RESETFILESYSTEMRESPONSE
_FILESYSTEMRESPONSE.oneofs_by_name['response'].fields.append(
  _FILESYSTEMRESPONSE.fields_by_name['rmFileCommand'])
_FILESYSTEMRESPONSE.fields_by_name['rmFileCommand'].containing_oneof = _FILESYSTEMRESPONSE.oneofs_by_name['response']
_FILESYSTEMRESPONSE.oneofs_by_name['response'].fields.append(
  _FILESYSTEMRESPONSE.fields_by_name['storeUpcomingFileDataResponse'])
_FILESYSTEMRESPONSE.fields_by_name['storeUpcomingFileDataResponse'].containing_oneof = _FILESYSTEMRESPONSE.oneofs_by_name['response']
_FILESYSTEMRESPONSE.oneofs_by_name['response'].fields.append(
  _FILESYSTEMRESPONSE.fields_by_name['reportFileDataResponse'])
_FILESYSTEMRESPONSE.fields_by_name['reportFileDataResponse'].containing_oneof = _FILESYSTEMRESPONSE.oneofs_by_name['response']
_FILESYSTEMRESPONSE.oneofs_by_name['response'].fields.append(
  _FILESYSTEMRESPONSE.fields_by_name['listDirContentsResponse'])
_FILESYSTEMRESPONSE.fields_by_name['listDirContentsResponse'].containing_oneof = _FILESYSTEMRESPONSE.oneofs_by_name['response']
_FILESYSTEMRESPONSE.oneofs_by_name['response'].fields.append(
  _FILESYSTEMRESPONSE.fields_by_name['resetFilesystemResponse'])
_FILESYSTEMRESPONSE.fields_by_name['resetFilesystemResponse'].containing_oneof = _FILESYSTEMRESPONSE.oneofs_by_name['response']
DESCRIPTOR.message_types_by_name['DirItem'] = _DIRITEM
DESCRIPTOR.message_types_by_name['FileData'] = _FILEDATA
DESCRIPTOR.message_types_by_name['StoreUpcomingFileDataCommand'] = _STOREUPCOMINGFILEDATACOMMAND
DESCRIPTOR.message_types_by_name['StoreUpcomingFileDataResponse'] = _STOREUPCOMINGFILEDATARESPONSE
DESCRIPTOR.message_types_by_name['RmFileCommand'] = _RMFILECOMMAND
DESCRIPTOR.message_types_by_name['RmFileResponse'] = _RMFILERESPONSE
DESCRIPTOR.message_types_by_name['ReportFileDataCommand'] = _REPORTFILEDATACOMMAND
DESCRIPTOR.message_types_by_name['ReportFileDataResponse'] = _REPORTFILEDATARESPONSE
DESCRIPTOR.message_types_by_name['ListDirContentsCommand'] = _LISTDIRCONTENTSCOMMAND
DESCRIPTOR.message_types_by_name['ListDirContentsResponse'] = _LISTDIRCONTENTSRESPONSE
DESCRIPTOR.message_types_by_name['PrintDirContentsCommand'] = _PRINTDIRCONTENTSCOMMAND
DESCRIPTOR.message_types_by_name['ResetFilesystemCommand'] = _RESETFILESYSTEMCOMMAND
DESCRIPTOR.message_types_by_name['ResetFilesystemResponse'] = _RESETFILESYSTEMRESPONSE
DESCRIPTOR.message_types_by_name['PrintFileContentsCommand'] = _PRINTFILECONTENTSCOMMAND
DESCRIPTOR.message_types_by_name['FileSystemCommand'] = _FILESYSTEMCOMMAND
DESCRIPTOR.message_types_by_name['FileSystemResponse'] = _FILESYSTEMRESPONSE
DESCRIPTOR.enum_types_by_name['DirItemType'] = _DIRITEMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DirItem = _reflection.GeneratedProtocolMessageType('DirItem', (_message.Message,), {
  'DESCRIPTOR' : _DIRITEM,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:DirItem)
  })
_sym_db.RegisterMessage(DirItem)

FileData = _reflection.GeneratedProtocolMessageType('FileData', (_message.Message,), {
  'DESCRIPTOR' : _FILEDATA,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:FileData)
  })
_sym_db.RegisterMessage(FileData)

StoreUpcomingFileDataCommand = _reflection.GeneratedProtocolMessageType('StoreUpcomingFileDataCommand', (_message.Message,), {
  'DESCRIPTOR' : _STOREUPCOMINGFILEDATACOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:StoreUpcomingFileDataCommand)
  })
_sym_db.RegisterMessage(StoreUpcomingFileDataCommand)

StoreUpcomingFileDataResponse = _reflection.GeneratedProtocolMessageType('StoreUpcomingFileDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOREUPCOMINGFILEDATARESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:StoreUpcomingFileDataResponse)
  })
_sym_db.RegisterMessage(StoreUpcomingFileDataResponse)

RmFileCommand = _reflection.GeneratedProtocolMessageType('RmFileCommand', (_message.Message,), {
  'DESCRIPTOR' : _RMFILECOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:RmFileCommand)
  })
_sym_db.RegisterMessage(RmFileCommand)

RmFileResponse = _reflection.GeneratedProtocolMessageType('RmFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _RMFILERESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:RmFileResponse)
  })
_sym_db.RegisterMessage(RmFileResponse)

ReportFileDataCommand = _reflection.GeneratedProtocolMessageType('ReportFileDataCommand', (_message.Message,), {
  'DESCRIPTOR' : _REPORTFILEDATACOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ReportFileDataCommand)
  })
_sym_db.RegisterMessage(ReportFileDataCommand)

ReportFileDataResponse = _reflection.GeneratedProtocolMessageType('ReportFileDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTFILEDATARESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ReportFileDataResponse)
  })
_sym_db.RegisterMessage(ReportFileDataResponse)

ListDirContentsCommand = _reflection.GeneratedProtocolMessageType('ListDirContentsCommand', (_message.Message,), {
  'DESCRIPTOR' : _LISTDIRCONTENTSCOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ListDirContentsCommand)
  })
_sym_db.RegisterMessage(ListDirContentsCommand)

ListDirContentsResponse = _reflection.GeneratedProtocolMessageType('ListDirContentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDIRCONTENTSRESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ListDirContentsResponse)
  })
_sym_db.RegisterMessage(ListDirContentsResponse)

PrintDirContentsCommand = _reflection.GeneratedProtocolMessageType('PrintDirContentsCommand', (_message.Message,), {
  'DESCRIPTOR' : _PRINTDIRCONTENTSCOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:PrintDirContentsCommand)
  })
_sym_db.RegisterMessage(PrintDirContentsCommand)

ResetFilesystemCommand = _reflection.GeneratedProtocolMessageType('ResetFilesystemCommand', (_message.Message,), {
  'DESCRIPTOR' : _RESETFILESYSTEMCOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ResetFilesystemCommand)
  })
_sym_db.RegisterMessage(ResetFilesystemCommand)

ResetFilesystemResponse = _reflection.GeneratedProtocolMessageType('ResetFilesystemResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETFILESYSTEMRESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:ResetFilesystemResponse)
  })
_sym_db.RegisterMessage(ResetFilesystemResponse)

PrintFileContentsCommand = _reflection.GeneratedProtocolMessageType('PrintFileContentsCommand', (_message.Message,), {
  'DESCRIPTOR' : _PRINTFILECONTENTSCOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:PrintFileContentsCommand)
  })
_sym_db.RegisterMessage(PrintFileContentsCommand)

FileSystemCommand = _reflection.GeneratedProtocolMessageType('FileSystemCommand', (_message.Message,), {
  'DESCRIPTOR' : _FILESYSTEMCOMMAND,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:FileSystemCommand)
  })
_sym_db.RegisterMessage(FileSystemCommand)

FileSystemResponse = _reflection.GeneratedProtocolMessageType('FileSystemResponse', (_message.Message,), {
  'DESCRIPTOR' : _FILESYSTEMRESPONSE,
  '__module__' : 'file_system_commands_pb2'
  # @@protoc_insertion_point(class_scope:FileSystemResponse)
  })
_sym_db.RegisterMessage(FileSystemResponse)


# @@protoc_insertion_point(module_scope)
