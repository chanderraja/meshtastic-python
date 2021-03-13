# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: radioconfig.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='radioconfig.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\021RadioConfigProtosH\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11radioconfig.proto\"\xad\x0f\n\x0bRadioConfig\x12\x31\n\x0bpreferences\x18\x01 \x01(\x0b\x32\x1c.RadioConfig.UserPreferences\x1a\xea\x0e\n\x0fUserPreferences\x12\x1f\n\x17position_broadcast_secs\x18\x01 \x01(\r\x12\x1b\n\x13send_owner_interval\x18\x02 \x01(\r\x12\x1b\n\x13wait_bluetooth_secs\x18\x04 \x01(\r\x12\x16\n\x0escreen_on_secs\x18\x05 \x01(\r\x12\x1a\n\x12phone_timeout_secs\x18\x06 \x01(\r\x12\x1d\n\x15phone_sds_timeout_sec\x18\x07 \x01(\r\x12\x1d\n\x15mesh_sds_timeout_secs\x18\x08 \x01(\r\x12\x10\n\x08sds_secs\x18\t \x01(\r\x12\x0f\n\x07ls_secs\x18\n \x01(\r\x12\x15\n\rmin_wake_secs\x18\x0b \x01(\r\x12\x11\n\twifi_ssid\x18\x0c \x01(\t\x12\x15\n\rwifi_password\x18\r \x01(\t\x12\x14\n\x0cwifi_ap_mode\x18\x0e \x01(\x08\x12\x1b\n\x06region\x18\x0f \x01(\x0e\x32\x0b.RegionCode\x12&\n\x0e\x63harge_current\x18\x10 \x01(\x0e\x32\x0e.ChargeCurrent\x12\x11\n\tis_router\x18% \x01(\x08\x12\x14\n\x0cis_low_power\x18& \x01(\x08\x12\x16\n\x0e\x66ixed_position\x18\' \x01(\x08\x12\x15\n\rfactory_reset\x18\x64 \x01(\x08\x12\x19\n\x11\x64\x65\x62ug_log_enabled\x18\x65 \x01(\x08\x12(\n\x0elocation_share\x18  \x01(\x0e\x32\x10.LocationSharing\x12$\n\rgps_operation\x18! \x01(\x0e\x32\r.GpsOperation\x12\x1b\n\x13gps_update_interval\x18\" \x01(\r\x12\x18\n\x10gps_attempt_time\x18$ \x01(\r\x12\x17\n\x0fignore_incoming\x18g \x03(\r\x12\x1c\n\x14serialplugin_enabled\x18x \x01(\x08\x12\x19\n\x11serialplugin_echo\x18y \x01(\x08\x12\x18\n\x10serialplugin_rxd\x18z \x01(\r\x12\x18\n\x10serialplugin_txd\x18{ \x01(\r\x12\x1c\n\x14serialplugin_timeout\x18| \x01(\r\x12\x19\n\x11serialplugin_mode\x18} \x01(\r\x12\'\n\x1f\x65xt_notification_plugin_enabled\x18~ \x01(\x08\x12)\n!ext_notification_plugin_output_ms\x18\x7f \x01(\r\x12\'\n\x1e\x65xt_notification_plugin_output\x18\x80\x01 \x01(\r\x12\'\n\x1e\x65xt_notification_plugin_active\x18\x81\x01 \x01(\x08\x12.\n%ext_notification_plugin_alert_message\x18\x82\x01 \x01(\x08\x12+\n\"ext_notification_plugin_alert_bell\x18\x83\x01 \x01(\x08\x12\"\n\x19range_test_plugin_enabled\x18\x84\x01 \x01(\x08\x12!\n\x18range_test_plugin_sender\x18\x85\x01 \x01(\r\x12\x1f\n\x16range_test_plugin_save\x18\x86\x01 \x01(\x08\x12%\n\x1cstore_forward_plugin_enabled\x18\x94\x01 \x01(\x08\x12%\n\x1cstore_forward_plugin_records\x18\x89\x01 \x01(\r\x12=\n4environmental_measurement_plugin_measurement_enabled\x18\x8c\x01 \x01(\x08\x12\x38\n/environmental_measurement_plugin_screen_enabled\x18\x8d\x01 \x01(\x08\x12\x44\n;environmental_measurement_plugin_read_error_count_threshold\x18\x8e\x01 \x01(\r\x12\x39\n0environmental_measurement_plugin_update_interval\x18\x8f\x01 \x01(\r\x12;\n2environmental_measurement_plugin_recovery_interval\x18\x90\x01 \x01(\r\x12;\n2environmental_measurement_plugin_display_farenheit\x18\x91\x01 \x01(\x08\x12v\n,environmental_measurement_plugin_sensor_type\x18\x92\x01 \x01(\x0e\x32?.RadioConfig.UserPreferences.EnvironmentalMeasurementSensorType\x12\x34\n+environmental_measurement_plugin_sensor_pin\x18\x93\x01 \x01(\r\"/\n\"EnvironmentalMeasurementSensorType\x12\t\n\x05\x44HT11\x10\x00J\x06\x08\x88\x01\x10\x89\x01*f\n\nRegionCode\x12\t\n\x05Unset\x10\x00\x12\x06\n\x02US\x10\x01\x12\t\n\x05\x45U433\x10\x02\x12\t\n\x05\x45U865\x10\x03\x12\x06\n\x02\x43N\x10\x04\x12\x06\n\x02JP\x10\x05\x12\x07\n\x03\x41NZ\x10\x06\x12\x06\n\x02KR\x10\x07\x12\x06\n\x02TW\x10\x08\x12\x06\n\x02RU\x10\t*\xd1\x01\n\rChargeCurrent\x12\x0b\n\x07MAUnset\x10\x00\x12\t\n\x05MA100\x10\x01\x12\t\n\x05MA190\x10\x02\x12\t\n\x05MA280\x10\x03\x12\t\n\x05MA360\x10\x04\x12\t\n\x05MA450\x10\x05\x12\t\n\x05MA550\x10\x06\x12\t\n\x05MA630\x10\x07\x12\t\n\x05MA700\x10\x08\x12\t\n\x05MA780\x10\t\x12\t\n\x05MA880\x10\n\x12\t\n\x05MA960\x10\x0b\x12\n\n\x06MA1000\x10\x0c\x12\n\n\x06MA1080\x10\r\x12\n\n\x06MA1160\x10\x0e\x12\n\n\x06MA1240\x10\x0f\x12\n\n\x06MA1320\x10\x10*j\n\x0cGpsOperation\x12\x0e\n\nGpsOpUnset\x10\x00\x12\x13\n\x0fGpsOpStationary\x10\x01\x12\x0f\n\x0bGpsOpMobile\x10\x02\x12\x11\n\rGpsOpTimeOnly\x10\x03\x12\x11\n\rGpsOpDisabled\x10\x04*@\n\x0fLocationSharing\x12\x0c\n\x08LocUnset\x10\x00\x12\x0e\n\nLocEnabled\x10\x01\x12\x0f\n\x0bLocDisabled\x10\x02\x42*\n\x13\x63om.geeksville.meshB\x11RadioConfigProtosH\x03\x62\x06proto3'
)

_REGIONCODE = _descriptor.EnumDescriptor(
  name='RegionCode',
  full_name='RegionCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unset', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EU433', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EU865', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JP', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANZ', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TW', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RU', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1989,
  serialized_end=2091,
)
_sym_db.RegisterEnumDescriptor(_REGIONCODE)

RegionCode = enum_type_wrapper.EnumTypeWrapper(_REGIONCODE)
_CHARGECURRENT = _descriptor.EnumDescriptor(
  name='ChargeCurrent',
  full_name='ChargeCurrent',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MAUnset', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA100', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA190', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA280', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA360', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA450', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA550', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA630', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA700', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA780', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA880', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA960', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA1000', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA1080', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA1160', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA1240', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MA1320', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2094,
  serialized_end=2303,
)
_sym_db.RegisterEnumDescriptor(_CHARGECURRENT)

ChargeCurrent = enum_type_wrapper.EnumTypeWrapper(_CHARGECURRENT)
_GPSOPERATION = _descriptor.EnumDescriptor(
  name='GpsOperation',
  full_name='GpsOperation',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GpsOpUnset', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GpsOpStationary', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GpsOpMobile', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GpsOpTimeOnly', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GpsOpDisabled', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2305,
  serialized_end=2411,
)
_sym_db.RegisterEnumDescriptor(_GPSOPERATION)

GpsOperation = enum_type_wrapper.EnumTypeWrapper(_GPSOPERATION)
_LOCATIONSHARING = _descriptor.EnumDescriptor(
  name='LocationSharing',
  full_name='LocationSharing',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LocUnset', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LocEnabled', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LocDisabled', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2413,
  serialized_end=2477,
)
_sym_db.RegisterEnumDescriptor(_LOCATIONSHARING)

LocationSharing = enum_type_wrapper.EnumTypeWrapper(_LOCATIONSHARING)
Unset = 0
US = 1
EU433 = 2
EU865 = 3
CN = 4
JP = 5
ANZ = 6
KR = 7
TW = 8
RU = 9
MAUnset = 0
MA100 = 1
MA190 = 2
MA280 = 3
MA360 = 4
MA450 = 5
MA550 = 6
MA630 = 7
MA700 = 8
MA780 = 9
MA880 = 10
MA960 = 11
MA1000 = 12
MA1080 = 13
MA1160 = 14
MA1240 = 15
MA1320 = 16
GpsOpUnset = 0
GpsOpStationary = 1
GpsOpMobile = 2
GpsOpTimeOnly = 3
GpsOpDisabled = 4
LocUnset = 0
LocEnabled = 1
LocDisabled = 2


_RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE = _descriptor.EnumDescriptor(
  name='EnvironmentalMeasurementSensorType',
  full_name='RadioConfig.UserPreferences.EnvironmentalMeasurementSensorType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DHT11', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1932,
  serialized_end=1979,
)
_sym_db.RegisterEnumDescriptor(_RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE)


_RADIOCONFIG_USERPREFERENCES = _descriptor.Descriptor(
  name='UserPreferences',
  full_name='RadioConfig.UserPreferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position_broadcast_secs', full_name='RadioConfig.UserPreferences.position_broadcast_secs', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='send_owner_interval', full_name='RadioConfig.UserPreferences.send_owner_interval', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wait_bluetooth_secs', full_name='RadioConfig.UserPreferences.wait_bluetooth_secs', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='screen_on_secs', full_name='RadioConfig.UserPreferences.screen_on_secs', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_timeout_secs', full_name='RadioConfig.UserPreferences.phone_timeout_secs', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_sds_timeout_sec', full_name='RadioConfig.UserPreferences.phone_sds_timeout_sec', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mesh_sds_timeout_secs', full_name='RadioConfig.UserPreferences.mesh_sds_timeout_secs', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sds_secs', full_name='RadioConfig.UserPreferences.sds_secs', index=7,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ls_secs', full_name='RadioConfig.UserPreferences.ls_secs', index=8,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_wake_secs', full_name='RadioConfig.UserPreferences.min_wake_secs', index=9,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wifi_ssid', full_name='RadioConfig.UserPreferences.wifi_ssid', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wifi_password', full_name='RadioConfig.UserPreferences.wifi_password', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wifi_ap_mode', full_name='RadioConfig.UserPreferences.wifi_ap_mode', index=12,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='RadioConfig.UserPreferences.region', index=13,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='charge_current', full_name='RadioConfig.UserPreferences.charge_current', index=14,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_router', full_name='RadioConfig.UserPreferences.is_router', index=15,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_low_power', full_name='RadioConfig.UserPreferences.is_low_power', index=16,
      number=38, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fixed_position', full_name='RadioConfig.UserPreferences.fixed_position', index=17,
      number=39, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='factory_reset', full_name='RadioConfig.UserPreferences.factory_reset', index=18,
      number=100, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='debug_log_enabled', full_name='RadioConfig.UserPreferences.debug_log_enabled', index=19,
      number=101, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location_share', full_name='RadioConfig.UserPreferences.location_share', index=20,
      number=32, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gps_operation', full_name='RadioConfig.UserPreferences.gps_operation', index=21,
      number=33, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gps_update_interval', full_name='RadioConfig.UserPreferences.gps_update_interval', index=22,
      number=34, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gps_attempt_time', full_name='RadioConfig.UserPreferences.gps_attempt_time', index=23,
      number=36, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ignore_incoming', full_name='RadioConfig.UserPreferences.ignore_incoming', index=24,
      number=103, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_enabled', full_name='RadioConfig.UserPreferences.serialplugin_enabled', index=25,
      number=120, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_echo', full_name='RadioConfig.UserPreferences.serialplugin_echo', index=26,
      number=121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_rxd', full_name='RadioConfig.UserPreferences.serialplugin_rxd', index=27,
      number=122, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_txd', full_name='RadioConfig.UserPreferences.serialplugin_txd', index=28,
      number=123, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_timeout', full_name='RadioConfig.UserPreferences.serialplugin_timeout', index=29,
      number=124, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serialplugin_mode', full_name='RadioConfig.UserPreferences.serialplugin_mode', index=30,
      number=125, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_enabled', full_name='RadioConfig.UserPreferences.ext_notification_plugin_enabled', index=31,
      number=126, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_output_ms', full_name='RadioConfig.UserPreferences.ext_notification_plugin_output_ms', index=32,
      number=127, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_output', full_name='RadioConfig.UserPreferences.ext_notification_plugin_output', index=33,
      number=128, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_active', full_name='RadioConfig.UserPreferences.ext_notification_plugin_active', index=34,
      number=129, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_alert_message', full_name='RadioConfig.UserPreferences.ext_notification_plugin_alert_message', index=35,
      number=130, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ext_notification_plugin_alert_bell', full_name='RadioConfig.UserPreferences.ext_notification_plugin_alert_bell', index=36,
      number=131, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_test_plugin_enabled', full_name='RadioConfig.UserPreferences.range_test_plugin_enabled', index=37,
      number=132, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_test_plugin_sender', full_name='RadioConfig.UserPreferences.range_test_plugin_sender', index=38,
      number=133, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_test_plugin_save', full_name='RadioConfig.UserPreferences.range_test_plugin_save', index=39,
      number=134, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store_forward_plugin_enabled', full_name='RadioConfig.UserPreferences.store_forward_plugin_enabled', index=40,
      number=148, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='store_forward_plugin_records', full_name='RadioConfig.UserPreferences.store_forward_plugin_records', index=41,
      number=137, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_measurement_enabled', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_measurement_enabled', index=42,
      number=140, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_screen_enabled', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_screen_enabled', index=43,
      number=141, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_read_error_count_threshold', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_read_error_count_threshold', index=44,
      number=142, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_update_interval', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_update_interval', index=45,
      number=143, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_recovery_interval', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_recovery_interval', index=46,
      number=144, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_display_farenheit', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_display_farenheit', index=47,
      number=145, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_sensor_type', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_sensor_type', index=48,
      number=146, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='environmental_measurement_plugin_sensor_pin', full_name='RadioConfig.UserPreferences.environmental_measurement_plugin_sensor_pin', index=49,
      number=147, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=1987,
)

_RADIOCONFIG = _descriptor.Descriptor(
  name='RadioConfig',
  full_name='RadioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preferences', full_name='RadioConfig.preferences', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RADIOCONFIG_USERPREFERENCES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=1987,
)

_RADIOCONFIG_USERPREFERENCES.fields_by_name['region'].enum_type = _REGIONCODE
_RADIOCONFIG_USERPREFERENCES.fields_by_name['charge_current'].enum_type = _CHARGECURRENT
_RADIOCONFIG_USERPREFERENCES.fields_by_name['location_share'].enum_type = _LOCATIONSHARING
_RADIOCONFIG_USERPREFERENCES.fields_by_name['gps_operation'].enum_type = _GPSOPERATION
_RADIOCONFIG_USERPREFERENCES.fields_by_name['environmental_measurement_plugin_sensor_type'].enum_type = _RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE
_RADIOCONFIG_USERPREFERENCES.containing_type = _RADIOCONFIG
_RADIOCONFIG_USERPREFERENCES_ENVIRONMENTALMEASUREMENTSENSORTYPE.containing_type = _RADIOCONFIG_USERPREFERENCES
_RADIOCONFIG.fields_by_name['preferences'].message_type = _RADIOCONFIG_USERPREFERENCES
DESCRIPTOR.message_types_by_name['RadioConfig'] = _RADIOCONFIG
DESCRIPTOR.enum_types_by_name['RegionCode'] = _REGIONCODE
DESCRIPTOR.enum_types_by_name['ChargeCurrent'] = _CHARGECURRENT
DESCRIPTOR.enum_types_by_name['GpsOperation'] = _GPSOPERATION
DESCRIPTOR.enum_types_by_name['LocationSharing'] = _LOCATIONSHARING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RadioConfig = _reflection.GeneratedProtocolMessageType('RadioConfig', (_message.Message,), {

  'UserPreferences' : _reflection.GeneratedProtocolMessageType('UserPreferences', (_message.Message,), {
    'DESCRIPTOR' : _RADIOCONFIG_USERPREFERENCES,
    '__module__' : 'radioconfig_pb2'
    # @@protoc_insertion_point(class_scope:RadioConfig.UserPreferences)
    })
  ,
  'DESCRIPTOR' : _RADIOCONFIG,
  '__module__' : 'radioconfig_pb2'
  # @@protoc_insertion_point(class_scope:RadioConfig)
  })
_sym_db.RegisterMessage(RadioConfig)
_sym_db.RegisterMessage(RadioConfig.UserPreferences)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
