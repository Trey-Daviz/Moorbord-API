# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: demo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndemo.proto\"$\n\x0f\x44\x61tabaseRequest\x12\x11\n\tfirstname\x18\x01 \x01(\t\"!\n\rDatabaseReply\x12\x10\n\x08lastname\x18\x01 \x01(\t\"\x19\n\x0bInfoRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x19\n\tInfoReply\x12\x0c\n\x04name\x18\x01 \x01(\t2f\n\x0c\x44\x61tabaseCall\x12,\n\x06\x44\x42\x43\x61ll\x12\x10.DatabaseRequest\x1a\x0e.DatabaseReply\"\x00\x12(\n\nInfoFromID\x12\x0c.InfoRequest\x1a\n.InfoReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'demo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATABASEREQUEST._serialized_start=14
  _DATABASEREQUEST._serialized_end=50
  _DATABASEREPLY._serialized_start=52
  _DATABASEREPLY._serialized_end=85
  _INFOREQUEST._serialized_start=87
  _INFOREQUEST._serialized_end=112
  _INFOREPLY._serialized_start=114
  _INFOREPLY._serialized_end=139
  _DATABASECALL._serialized_start=141
  _DATABASECALL._serialized_end=243
# @@protoc_insertion_point(module_scope)