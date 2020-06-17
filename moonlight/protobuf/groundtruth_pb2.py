# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: groundtruth.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='groundtruth.proto',
  package='tensorflow.moonlight',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11groundtruth.proto\x12\x14tensorflow.moonlight\"\x8c\x02\n\x0bGroundTruth\x12\r\n\x05title\x18\x01 \x01(\t\x12\x1d\n\x15ground_truth_filename\x18\x02 \x01(\t\x12\x31\n\tpage_spec\x18\x03 \x03(\x0b\x32\x1e.tensorflow.moonlight.PageSpec\x12\x32\n\x03tag\x18\x04 \x03(\x0e\x32%.tensorflow.moonlight.GroundTruth.Tag\"h\n\x03Tag\x12\x0f\n\x0bUNKNOWN_TAG\x10\x00\x12\x0e\n\nMONOPHONIC\x10\x01\x12\x10\n\x0cSINGLE_STAFF\x10\x02\x12\t\n\x05PIANO\x10\x03\x12\x17\n\x13VOICES_CROSS_STAVES\x10\x04\x12\n\n\x06\x43HORDS\x10\x05\"\x1c\n\x08PageSpec\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t'
)



_GROUNDTRUTH_TAG = _descriptor.EnumDescriptor(
  name='Tag',
  full_name='tensorflow.moonlight.GroundTruth.Tag',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TAG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MONOPHONIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_STAFF', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PIANO', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VOICES_CROSS_STAVES', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHORDS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=208,
  serialized_end=312,
)
_sym_db.RegisterEnumDescriptor(_GROUNDTRUTH_TAG)


_GROUNDTRUTH = _descriptor.Descriptor(
  name='GroundTruth',
  full_name='tensorflow.moonlight.GroundTruth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='tensorflow.moonlight.GroundTruth.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ground_truth_filename', full_name='tensorflow.moonlight.GroundTruth.ground_truth_filename', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_spec', full_name='tensorflow.moonlight.GroundTruth.page_spec', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tag', full_name='tensorflow.moonlight.GroundTruth.tag', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GROUNDTRUTH_TAG,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=312,
)


_PAGESPEC = _descriptor.Descriptor(
  name='PageSpec',
  full_name='tensorflow.moonlight.PageSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='tensorflow.moonlight.PageSpec.filename', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=314,
  serialized_end=342,
)

_GROUNDTRUTH.fields_by_name['page_spec'].message_type = _PAGESPEC
_GROUNDTRUTH.fields_by_name['tag'].enum_type = _GROUNDTRUTH_TAG
_GROUNDTRUTH_TAG.containing_type = _GROUNDTRUTH
DESCRIPTOR.message_types_by_name['GroundTruth'] = _GROUNDTRUTH
DESCRIPTOR.message_types_by_name['PageSpec'] = _PAGESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GroundTruth = _reflection.GeneratedProtocolMessageType('GroundTruth', (_message.Message,), {
  'DESCRIPTOR' : _GROUNDTRUTH,
  '__module__' : 'groundtruth_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.moonlight.GroundTruth)
  })
_sym_db.RegisterMessage(GroundTruth)

PageSpec = _reflection.GeneratedProtocolMessageType('PageSpec', (_message.Message,), {
  'DESCRIPTOR' : _PAGESPEC,
  '__module__' : 'groundtruth_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.moonlight.PageSpec)
  })
_sym_db.RegisterMessage(PageSpec)


# @@protoc_insertion_point(module_scope)
