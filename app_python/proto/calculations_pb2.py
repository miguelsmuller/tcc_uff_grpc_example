# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/calculations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18proto/calculations.proto\x12\x0c\x63\x61lculations\"D\n\x0f\x42haskaraRequest\x12\x0f\n\x07value_a\x18\x01 \x01(\x05\x12\x0f\n\x07value_b\x18\x02 \x01(\x05\x12\x0f\n\x07value_c\x18\x03 \x01(\x05\",\n\x12RootsEquationReply\x12\n\n\x02x1\x18\x01 \x01(\x02\x12\n\n\x02x2\x18\x02 \x01(\x02\"8\n\x18\x46ibonacciSequenceRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\x05\"\'\n\x16\x46ibonacciSequenceReply\x12\r\n\x05value\x18\x01 \x01(\x05\x32\xd9\x01\n\x0c\x43\x61lculations\x12_\n\x1aGetRootsEquationByBhaskara\x12\x1d.calculations.BhaskaraRequest\x1a .calculations.RootsEquationReply\"\x00\x12h\n\x14GetFibonacciSequence\x12&.calculations.FibonacciSequenceRequest\x1a$.calculations.FibonacciSequenceReply\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.calculations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BHASKARAREQUEST._serialized_start=42
  _BHASKARAREQUEST._serialized_end=110
  _ROOTSEQUATIONREPLY._serialized_start=112
  _ROOTSEQUATIONREPLY._serialized_end=156
  _FIBONACCISEQUENCEREQUEST._serialized_start=158
  _FIBONACCISEQUENCEREQUEST._serialized_end=214
  _FIBONACCISEQUENCEREPLY._serialized_start=216
  _FIBONACCISEQUENCEREPLY._serialized_end=255
  _CALCULATIONS._serialized_start=258
  _CALCULATIONS._serialized_end=475
# @@protoc_insertion_point(module_scope)