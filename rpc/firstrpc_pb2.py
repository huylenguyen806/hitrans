# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: firstrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='firstrpc.proto',
  package='firstrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x66irstrpc.proto\x12\x08\x66irstrpc\"\x07\n\x05\x45mpty\"~\n\x0e\x43onfigurations\x12\x11\n\ttrans_url\x18\x01 \x01(\t\x12\x13\n\x0bsource_lang\x18\x02 \x01(\t\x12\x13\n\x0btarget_lang\x18\x03 \x01(\t\x12\x0f\n\x07\x61pi_key\x18\x04 \x01(\t\x12\r\n\x05model\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x06 \x01(\t\"A\n\rTextSelection\x12\x14\n\x0c\x64ouble_click\x18\x01 \x01(\x08\x12\x1a\n\x12\x66inished_selection\x18\x02 \x01(\x08\"M\n\x08Settings\x12/\n\x0etext_selection\x18\x01 \x01(\x0b\x32\x17.firstrpc.TextSelection\x12\x10\n\x08shortcut\x18\x02 \x01(\t\"d\n\nConfigData\x12\x30\n\x0e\x63onfigurations\x18\x01 \x01(\x0b\x32\x18.firstrpc.Configurations\x12$\n\x08settings\x18\x02 \x01(\x0b\x32\x12.firstrpc.Settings2\xb8\x01\n\x08\x46irstRpc\x12\x36\n\x10\x43reateConfigFile\x12\x0f.firstrpc.Empty\x1a\x0f.firstrpc.Empty\"\x00\x12\x38\n\rGetConfigFile\x12\x0f.firstrpc.Empty\x1a\x14.firstrpc.ConfigData\"\x00\x12:\n\x0fWriteConfigFile\x12\x14.firstrpc.ConfigData\x1a\x0f.firstrpc.Empty\"\x00\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='firstrpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=28,
  serialized_end=35,
)


_CONFIGURATIONS = _descriptor.Descriptor(
  name='Configurations',
  full_name='firstrpc.Configurations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trans_url', full_name='firstrpc.Configurations.trans_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_lang', full_name='firstrpc.Configurations.source_lang', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_lang', full_name='firstrpc.Configurations.target_lang', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='api_key', full_name='firstrpc.Configurations.api_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='firstrpc.Configurations.model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='firstrpc.Configurations.version', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=37,
  serialized_end=163,
)


_TEXTSELECTION = _descriptor.Descriptor(
  name='TextSelection',
  full_name='firstrpc.TextSelection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_click', full_name='firstrpc.TextSelection.double_click', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished_selection', full_name='firstrpc.TextSelection.finished_selection', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=165,
  serialized_end=230,
)


_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='firstrpc.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_selection', full_name='firstrpc.Settings.text_selection', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shortcut', full_name='firstrpc.Settings.shortcut', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=232,
  serialized_end=309,
)


_CONFIGDATA = _descriptor.Descriptor(
  name='ConfigData',
  full_name='firstrpc.ConfigData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='configurations', full_name='firstrpc.ConfigData.configurations', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='firstrpc.ConfigData.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=311,
  serialized_end=411,
)

_SETTINGS.fields_by_name['text_selection'].message_type = _TEXTSELECTION
_CONFIGDATA.fields_by_name['configurations'].message_type = _CONFIGURATIONS
_CONFIGDATA.fields_by_name['settings'].message_type = _SETTINGS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Configurations'] = _CONFIGURATIONS
DESCRIPTOR.message_types_by_name['TextSelection'] = _TEXTSELECTION
DESCRIPTOR.message_types_by_name['Settings'] = _SETTINGS
DESCRIPTOR.message_types_by_name['ConfigData'] = _CONFIGDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'firstrpc_pb2'
  # @@protoc_insertion_point(class_scope:firstrpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

Configurations = _reflection.GeneratedProtocolMessageType('Configurations', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONS,
  '__module__' : 'firstrpc_pb2'
  # @@protoc_insertion_point(class_scope:firstrpc.Configurations)
  })
_sym_db.RegisterMessage(Configurations)

TextSelection = _reflection.GeneratedProtocolMessageType('TextSelection', (_message.Message,), {
  'DESCRIPTOR' : _TEXTSELECTION,
  '__module__' : 'firstrpc_pb2'
  # @@protoc_insertion_point(class_scope:firstrpc.TextSelection)
  })
_sym_db.RegisterMessage(TextSelection)

Settings = _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGS,
  '__module__' : 'firstrpc_pb2'
  # @@protoc_insertion_point(class_scope:firstrpc.Settings)
  })
_sym_db.RegisterMessage(Settings)

ConfigData = _reflection.GeneratedProtocolMessageType('ConfigData', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGDATA,
  '__module__' : 'firstrpc_pb2'
  # @@protoc_insertion_point(class_scope:firstrpc.ConfigData)
  })
_sym_db.RegisterMessage(ConfigData)



_FIRSTRPC = _descriptor.ServiceDescriptor(
  name='FirstRpc',
  full_name='firstrpc.FirstRpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=414,
  serialized_end=598,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateConfigFile',
    full_name='firstrpc.FirstRpc.CreateConfigFile',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetConfigFile',
    full_name='firstrpc.FirstRpc.GetConfigFile',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CONFIGDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteConfigFile',
    full_name='firstrpc.FirstRpc.WriteConfigFile',
    index=2,
    containing_service=None,
    input_type=_CONFIGDATA,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FIRSTRPC)

DESCRIPTOR.services_by_name['FirstRpc'] = _FIRSTRPC

# @@protoc_insertion_point(module_scope)