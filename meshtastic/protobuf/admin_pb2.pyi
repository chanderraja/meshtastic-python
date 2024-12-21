"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import meshtastic.protobuf.channel_pb2
import meshtastic.protobuf.config_pb2
import meshtastic.protobuf.connection_status_pb2
import meshtastic.protobuf.device_ui_pb2
import meshtastic.protobuf.mesh_pb2
import meshtastic.protobuf.module_config_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AdminMessage(google.protobuf.message.Message):
    """
    This message is handled by the Admin module and is responsible for all settings/channel read/write operations.
    This message is used to do settings operations to both remote AND local nodes.
    (Prior to 1.2 these operations were done via special ToRadio operations)
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ConfigType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ConfigTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AdminMessage._ConfigType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DEVICE_CONFIG: AdminMessage._ConfigType.ValueType  # 0
        """
        TODO: REPLACE
        """
        POSITION_CONFIG: AdminMessage._ConfigType.ValueType  # 1
        """
        TODO: REPLACE
        """
        POWER_CONFIG: AdminMessage._ConfigType.ValueType  # 2
        """
        TODO: REPLACE
        """
        NETWORK_CONFIG: AdminMessage._ConfigType.ValueType  # 3
        """
        TODO: REPLACE
        """
        DISPLAY_CONFIG: AdminMessage._ConfigType.ValueType  # 4
        """
        TODO: REPLACE
        """
        LORA_CONFIG: AdminMessage._ConfigType.ValueType  # 5
        """
        TODO: REPLACE
        """
        BLUETOOTH_CONFIG: AdminMessage._ConfigType.ValueType  # 6
        """
        TODO: REPLACE
        """
        SECURITY_CONFIG: AdminMessage._ConfigType.ValueType  # 7
        """
        TODO: REPLACE
        """
        SESSIONKEY_CONFIG: AdminMessage._ConfigType.ValueType  # 8
        """"""
        DEVICEUI_CONFIG: AdminMessage._ConfigType.ValueType  # 9
        """
        device-ui config
        """

    class ConfigType(_ConfigType, metaclass=_ConfigTypeEnumTypeWrapper):
        """
        TODO: REPLACE
        """

    DEVICE_CONFIG: AdminMessage.ConfigType.ValueType  # 0
    """
    TODO: REPLACE
    """
    POSITION_CONFIG: AdminMessage.ConfigType.ValueType  # 1
    """
    TODO: REPLACE
    """
    POWER_CONFIG: AdminMessage.ConfigType.ValueType  # 2
    """
    TODO: REPLACE
    """
    NETWORK_CONFIG: AdminMessage.ConfigType.ValueType  # 3
    """
    TODO: REPLACE
    """
    DISPLAY_CONFIG: AdminMessage.ConfigType.ValueType  # 4
    """
    TODO: REPLACE
    """
    LORA_CONFIG: AdminMessage.ConfigType.ValueType  # 5
    """
    TODO: REPLACE
    """
    BLUETOOTH_CONFIG: AdminMessage.ConfigType.ValueType  # 6
    """
    TODO: REPLACE
    """
    SECURITY_CONFIG: AdminMessage.ConfigType.ValueType  # 7
    """
    TODO: REPLACE
    """
    SESSIONKEY_CONFIG: AdminMessage.ConfigType.ValueType  # 8
    """"""
    DEVICEUI_CONFIG: AdminMessage.ConfigType.ValueType  # 9
    """
    device-ui config
    """

    class _ModuleConfigType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ModuleConfigTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AdminMessage._ModuleConfigType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MQTT_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 0
        """
        TODO: REPLACE
        """
        SERIAL_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 1
        """
        TODO: REPLACE
        """
        EXTNOTIF_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 2
        """
        TODO: REPLACE
        """
        STOREFORWARD_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 3
        """
        TODO: REPLACE
        """
        RANGETEST_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 4
        """
        TODO: REPLACE
        """
        TELEMETRY_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 5
        """
        TODO: REPLACE
        """
        CANNEDMSG_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 6
        """
        TODO: REPLACE
        """
        AUDIO_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 7
        """
        TODO: REPLACE
        """
        REMOTEHARDWARE_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 8
        """
        TODO: REPLACE
        """
        NEIGHBORINFO_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 9
        """
        TODO: REPLACE
        """
        AMBIENTLIGHTING_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 10
        """
        TODO: REPLACE
        """
        DETECTIONSENSOR_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 11
        """
        TODO: REPLACE
        """
        PAXCOUNTER_CONFIG: AdminMessage._ModuleConfigType.ValueType  # 12
        """
        TODO: REPLACE
        """

    class ModuleConfigType(_ModuleConfigType, metaclass=_ModuleConfigTypeEnumTypeWrapper):
        """
        TODO: REPLACE
        """

    MQTT_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 0
    """
    TODO: REPLACE
    """
    SERIAL_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 1
    """
    TODO: REPLACE
    """
    EXTNOTIF_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 2
    """
    TODO: REPLACE
    """
    STOREFORWARD_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 3
    """
    TODO: REPLACE
    """
    RANGETEST_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 4
    """
    TODO: REPLACE
    """
    TELEMETRY_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 5
    """
    TODO: REPLACE
    """
    CANNEDMSG_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 6
    """
    TODO: REPLACE
    """
    AUDIO_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 7
    """
    TODO: REPLACE
    """
    REMOTEHARDWARE_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 8
    """
    TODO: REPLACE
    """
    NEIGHBORINFO_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 9
    """
    TODO: REPLACE
    """
    AMBIENTLIGHTING_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 10
    """
    TODO: REPLACE
    """
    DETECTIONSENSOR_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 11
    """
    TODO: REPLACE
    """
    PAXCOUNTER_CONFIG: AdminMessage.ModuleConfigType.ValueType  # 12
    """
    TODO: REPLACE
    """

    SESSION_PASSKEY_FIELD_NUMBER: builtins.int
    GET_CHANNEL_REQUEST_FIELD_NUMBER: builtins.int
    GET_CHANNEL_RESPONSE_FIELD_NUMBER: builtins.int
    GET_OWNER_REQUEST_FIELD_NUMBER: builtins.int
    GET_OWNER_RESPONSE_FIELD_NUMBER: builtins.int
    GET_CONFIG_REQUEST_FIELD_NUMBER: builtins.int
    GET_CONFIG_RESPONSE_FIELD_NUMBER: builtins.int
    GET_MODULE_CONFIG_REQUEST_FIELD_NUMBER: builtins.int
    GET_MODULE_CONFIG_RESPONSE_FIELD_NUMBER: builtins.int
    GET_CANNED_MESSAGE_MODULE_MESSAGES_REQUEST_FIELD_NUMBER: builtins.int
    GET_CANNED_MESSAGE_MODULE_MESSAGES_RESPONSE_FIELD_NUMBER: builtins.int
    GET_DEVICE_METADATA_REQUEST_FIELD_NUMBER: builtins.int
    GET_DEVICE_METADATA_RESPONSE_FIELD_NUMBER: builtins.int
    GET_RINGTONE_REQUEST_FIELD_NUMBER: builtins.int
    GET_RINGTONE_RESPONSE_FIELD_NUMBER: builtins.int
    GET_DEVICE_CONNECTION_STATUS_REQUEST_FIELD_NUMBER: builtins.int
    GET_DEVICE_CONNECTION_STATUS_RESPONSE_FIELD_NUMBER: builtins.int
    SET_HAM_MODE_FIELD_NUMBER: builtins.int
    GET_NODE_REMOTE_HARDWARE_PINS_REQUEST_FIELD_NUMBER: builtins.int
    GET_NODE_REMOTE_HARDWARE_PINS_RESPONSE_FIELD_NUMBER: builtins.int
    ENTER_DFU_MODE_REQUEST_FIELD_NUMBER: builtins.int
    DELETE_FILE_REQUEST_FIELD_NUMBER: builtins.int
    SET_SCALE_FIELD_NUMBER: builtins.int
    SET_OWNER_FIELD_NUMBER: builtins.int
    SET_CHANNEL_FIELD_NUMBER: builtins.int
    SET_CONFIG_FIELD_NUMBER: builtins.int
    SET_MODULE_CONFIG_FIELD_NUMBER: builtins.int
    SET_CANNED_MESSAGE_MODULE_MESSAGES_FIELD_NUMBER: builtins.int
    SET_RINGTONE_MESSAGE_FIELD_NUMBER: builtins.int
    REMOVE_BY_NODENUM_FIELD_NUMBER: builtins.int
    SET_FAVORITE_NODE_FIELD_NUMBER: builtins.int
    REMOVE_FAVORITE_NODE_FIELD_NUMBER: builtins.int
    SET_FIXED_POSITION_FIELD_NUMBER: builtins.int
    REMOVE_FIXED_POSITION_FIELD_NUMBER: builtins.int
    SET_TIME_ONLY_FIELD_NUMBER: builtins.int
    GET_UI_CONFIG_REQUEST_FIELD_NUMBER: builtins.int
    GET_UI_CONFIG_RESPONSE_FIELD_NUMBER: builtins.int
    STORE_UI_CONFIG_FIELD_NUMBER: builtins.int
    SET_IGNORED_NODE_FIELD_NUMBER: builtins.int
    REMOVE_IGNORED_NODE_FIELD_NUMBER: builtins.int
    BEGIN_EDIT_SETTINGS_FIELD_NUMBER: builtins.int
    COMMIT_EDIT_SETTINGS_FIELD_NUMBER: builtins.int
    FACTORY_RESET_DEVICE_FIELD_NUMBER: builtins.int
    REBOOT_OTA_SECONDS_FIELD_NUMBER: builtins.int
    EXIT_SIMULATOR_FIELD_NUMBER: builtins.int
    REBOOT_SECONDS_FIELD_NUMBER: builtins.int
    SHUTDOWN_SECONDS_FIELD_NUMBER: builtins.int
    FACTORY_RESET_CONFIG_FIELD_NUMBER: builtins.int
    NODEDB_RESET_FIELD_NUMBER: builtins.int
    session_passkey: builtins.bytes
    """
    The node generates this key and sends it with any get_x_response packets.
    The client MUST include the same key with any set_x commands. Key expires after 300 seconds.
    Prevents replay attacks for admin messages.
    """
    get_channel_request: builtins.int
    """
    Send the specified channel in the response to this message
    NOTE: This field is sent with the channel index + 1 (to ensure we never try to send 'zero' - which protobufs treats as not present)
    """
    get_owner_request: builtins.bool
    """
    Send the current owner data in the response to this message.
    """
    get_config_request: global___AdminMessage.ConfigType.ValueType
    """
    Ask for the following config data to be sent
    """
    get_module_config_request: global___AdminMessage.ModuleConfigType.ValueType
    """
    Ask for the following config data to be sent
    """
    get_canned_message_module_messages_request: builtins.bool
    """
    Get the Canned Message Module messages in the response to this message.
    """
    get_canned_message_module_messages_response: builtins.str
    """
    Get the Canned Message Module messages in the response to this message.
    """
    get_device_metadata_request: builtins.bool
    """
    Request the node to send device metadata (firmware, protobuf version, etc)
    """
    get_ringtone_request: builtins.bool
    """
    Get the Ringtone in the response to this message.
    """
    get_ringtone_response: builtins.str
    """
    Get the Ringtone in the response to this message.
    """
    get_device_connection_status_request: builtins.bool
    """
    Request the node to send it's connection status
    """
    get_node_remote_hardware_pins_request: builtins.bool
    """
    Get the mesh's nodes with their available gpio pins for RemoteHardware module use
    """
    enter_dfu_mode_request: builtins.bool
    """
    Enter (UF2) DFU mode
    Only implemented on NRF52 currently
    """
    delete_file_request: builtins.str
    """
    Delete the file by the specified path from the device
    """
    set_scale: builtins.int
    """
    Set zero and offset for scale chips
    """
    set_canned_message_module_messages: builtins.str
    """
    Set the Canned Message Module messages text.
    """
    set_ringtone_message: builtins.str
    """
    Set the ringtone for ExternalNotification.
    """
    remove_by_nodenum: builtins.int
    """
    Remove the node by the specified node-num from the NodeDB on the device
    """
    set_favorite_node: builtins.int
    """
    Set specified node-num to be favorited on the NodeDB on the device
    """
    remove_favorite_node: builtins.int
    """
    Set specified node-num to be un-favorited on the NodeDB on the device
    """
    remove_fixed_position: builtins.bool
    """
    Clear fixed position coordinates and then set position.fixed_position = false
    """
    set_time_only: builtins.int
    """
    Set time only on the node
    Convenience method to set the time on the node (as Net quality) without any other position data
    """
    get_ui_config_request: builtins.bool
    """
    Tell the node to send the stored ui data.
    """
    set_ignored_node: builtins.int
    """
    Set specified node-num to be ignored on the NodeDB on the device
    """
    remove_ignored_node: builtins.int
    """
    Set specified node-num to be un-ignored on the NodeDB on the device
    """
    begin_edit_settings: builtins.bool
    """
    Begins an edit transaction for config, module config, owner, and channel settings changes
    This will delay the standard *implicit* save to the file system and subsequent reboot behavior until committed (commit_edit_settings)
    """
    commit_edit_settings: builtins.bool
    """
    Commits an open transaction for any edits made to config, module config, owner, and channel settings
    """
    factory_reset_device: builtins.int
    """
    Tell the node to factory reset config everything; all device state and configuration will be returned to factory defaults and BLE bonds will be cleared.
    """
    reboot_ota_seconds: builtins.int
    """
    Tell the node to reboot into the OTA Firmware in this many seconds (or <0 to cancel reboot)
    Only Implemented for ESP32 Devices. This needs to be issued to send a new main firmware via bluetooth.
    """
    exit_simulator: builtins.bool
    """
    This message is only supported for the simulator Portduino build.
    If received the simulator will exit successfully.
    """
    reboot_seconds: builtins.int
    """
    Tell the node to reboot in this many seconds (or <0 to cancel reboot)
    """
    shutdown_seconds: builtins.int
    """
    Tell the node to shutdown in this many seconds (or <0 to cancel shutdown)
    """
    factory_reset_config: builtins.int
    """
    Tell the node to factory reset config; all device state and configuration will be returned to factory defaults; BLE bonds will be preserved.
    """
    nodedb_reset: builtins.int
    """
    Tell the node to reset the nodedb.
    """
    @property
    def get_channel_response(self) -> meshtastic.protobuf.channel_pb2.Channel:
        """
        TODO: REPLACE
        """

    @property
    def get_owner_response(self) -> meshtastic.protobuf.mesh_pb2.User:
        """
        TODO: REPLACE
        """

    @property
    def get_config_response(self) -> meshtastic.protobuf.config_pb2.Config:
        """
        Send the current Config in the response to this message.
        """

    @property
    def get_module_config_response(self) -> meshtastic.protobuf.module_config_pb2.ModuleConfig:
        """
        Send the current Config in the response to this message.
        """

    @property
    def get_device_metadata_response(self) -> meshtastic.protobuf.mesh_pb2.DeviceMetadata:
        """
        Device metadata response
        """

    @property
    def get_device_connection_status_response(self) -> meshtastic.protobuf.connection_status_pb2.DeviceConnectionStatus:
        """
        Device connection status response
        """

    @property
    def set_ham_mode(self) -> global___HamParameters:
        """
        Setup a node for licensed amateur (ham) radio operation
        """

    @property
    def get_node_remote_hardware_pins_response(self) -> global___NodeRemoteHardwarePinsResponse:
        """
        Respond with the mesh's nodes with their available gpio pins for RemoteHardware module use
        """

    @property
    def set_owner(self) -> meshtastic.protobuf.mesh_pb2.User:
        """
        Set the owner for this node
        """

    @property
    def set_channel(self) -> meshtastic.protobuf.channel_pb2.Channel:
        """
        Set channels (using the new API).
        A special channel is the "primary channel".
        The other records are secondary channels.
        Note: only one channel can be marked as primary.
        If the client sets a particular channel to be primary, the previous channel will be set to SECONDARY automatically.
        """

    @property
    def set_config(self) -> meshtastic.protobuf.config_pb2.Config:
        """
        Set the current Config
        """

    @property
    def set_module_config(self) -> meshtastic.protobuf.module_config_pb2.ModuleConfig:
        """
        Set the current Config
        """

    @property
    def set_fixed_position(self) -> meshtastic.protobuf.mesh_pb2.Position:
        """
        Set fixed position data on the node and then set the position.fixed_position = true
        """

    @property
    def get_ui_config_response(self) -> meshtastic.protobuf.device_ui_pb2.DeviceUIConfig:
        """
        Reply stored device ui data.
        """

    @property
    def store_ui_config(self) -> meshtastic.protobuf.device_ui_pb2.DeviceUIConfig:
        """
        Tell the node to store UI data persistently.
        """

    def __init__(
        self,
        *,
        session_passkey: builtins.bytes = ...,
        get_channel_request: builtins.int = ...,
        get_channel_response: meshtastic.protobuf.channel_pb2.Channel | None = ...,
        get_owner_request: builtins.bool = ...,
        get_owner_response: meshtastic.protobuf.mesh_pb2.User | None = ...,
        get_config_request: global___AdminMessage.ConfigType.ValueType = ...,
        get_config_response: meshtastic.protobuf.config_pb2.Config | None = ...,
        get_module_config_request: global___AdminMessage.ModuleConfigType.ValueType = ...,
        get_module_config_response: meshtastic.protobuf.module_config_pb2.ModuleConfig | None = ...,
        get_canned_message_module_messages_request: builtins.bool = ...,
        get_canned_message_module_messages_response: builtins.str = ...,
        get_device_metadata_request: builtins.bool = ...,
        get_device_metadata_response: meshtastic.protobuf.mesh_pb2.DeviceMetadata | None = ...,
        get_ringtone_request: builtins.bool = ...,
        get_ringtone_response: builtins.str = ...,
        get_device_connection_status_request: builtins.bool = ...,
        get_device_connection_status_response: meshtastic.protobuf.connection_status_pb2.DeviceConnectionStatus | None = ...,
        set_ham_mode: global___HamParameters | None = ...,
        get_node_remote_hardware_pins_request: builtins.bool = ...,
        get_node_remote_hardware_pins_response: global___NodeRemoteHardwarePinsResponse | None = ...,
        enter_dfu_mode_request: builtins.bool = ...,
        delete_file_request: builtins.str = ...,
        set_scale: builtins.int = ...,
        set_owner: meshtastic.protobuf.mesh_pb2.User | None = ...,
        set_channel: meshtastic.protobuf.channel_pb2.Channel | None = ...,
        set_config: meshtastic.protobuf.config_pb2.Config | None = ...,
        set_module_config: meshtastic.protobuf.module_config_pb2.ModuleConfig | None = ...,
        set_canned_message_module_messages: builtins.str = ...,
        set_ringtone_message: builtins.str = ...,
        remove_by_nodenum: builtins.int = ...,
        set_favorite_node: builtins.int = ...,
        remove_favorite_node: builtins.int = ...,
        set_fixed_position: meshtastic.protobuf.mesh_pb2.Position | None = ...,
        remove_fixed_position: builtins.bool = ...,
        set_time_only: builtins.int = ...,
        get_ui_config_request: builtins.bool = ...,
        get_ui_config_response: meshtastic.protobuf.device_ui_pb2.DeviceUIConfig | None = ...,
        store_ui_config: meshtastic.protobuf.device_ui_pb2.DeviceUIConfig | None = ...,
        set_ignored_node: builtins.int = ...,
        remove_ignored_node: builtins.int = ...,
        begin_edit_settings: builtins.bool = ...,
        commit_edit_settings: builtins.bool = ...,
        factory_reset_device: builtins.int = ...,
        reboot_ota_seconds: builtins.int = ...,
        exit_simulator: builtins.bool = ...,
        reboot_seconds: builtins.int = ...,
        shutdown_seconds: builtins.int = ...,
        factory_reset_config: builtins.int = ...,
        nodedb_reset: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["begin_edit_settings", b"begin_edit_settings", "commit_edit_settings", b"commit_edit_settings", "delete_file_request", b"delete_file_request", "enter_dfu_mode_request", b"enter_dfu_mode_request", "exit_simulator", b"exit_simulator", "factory_reset_config", b"factory_reset_config", "factory_reset_device", b"factory_reset_device", "get_canned_message_module_messages_request", b"get_canned_message_module_messages_request", "get_canned_message_module_messages_response", b"get_canned_message_module_messages_response", "get_channel_request", b"get_channel_request", "get_channel_response", b"get_channel_response", "get_config_request", b"get_config_request", "get_config_response", b"get_config_response", "get_device_connection_status_request", b"get_device_connection_status_request", "get_device_connection_status_response", b"get_device_connection_status_response", "get_device_metadata_request", b"get_device_metadata_request", "get_device_metadata_response", b"get_device_metadata_response", "get_module_config_request", b"get_module_config_request", "get_module_config_response", b"get_module_config_response", "get_node_remote_hardware_pins_request", b"get_node_remote_hardware_pins_request", "get_node_remote_hardware_pins_response", b"get_node_remote_hardware_pins_response", "get_owner_request", b"get_owner_request", "get_owner_response", b"get_owner_response", "get_ringtone_request", b"get_ringtone_request", "get_ringtone_response", b"get_ringtone_response", "get_ui_config_request", b"get_ui_config_request", "get_ui_config_response", b"get_ui_config_response", "nodedb_reset", b"nodedb_reset", "payload_variant", b"payload_variant", "reboot_ota_seconds", b"reboot_ota_seconds", "reboot_seconds", b"reboot_seconds", "remove_by_nodenum", b"remove_by_nodenum", "remove_favorite_node", b"remove_favorite_node", "remove_fixed_position", b"remove_fixed_position", "remove_ignored_node", b"remove_ignored_node", "set_canned_message_module_messages", b"set_canned_message_module_messages", "set_channel", b"set_channel", "set_config", b"set_config", "set_favorite_node", b"set_favorite_node", "set_fixed_position", b"set_fixed_position", "set_ham_mode", b"set_ham_mode", "set_ignored_node", b"set_ignored_node", "set_module_config", b"set_module_config", "set_owner", b"set_owner", "set_ringtone_message", b"set_ringtone_message", "set_scale", b"set_scale", "set_time_only", b"set_time_only", "shutdown_seconds", b"shutdown_seconds", "store_ui_config", b"store_ui_config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["begin_edit_settings", b"begin_edit_settings", "commit_edit_settings", b"commit_edit_settings", "delete_file_request", b"delete_file_request", "enter_dfu_mode_request", b"enter_dfu_mode_request", "exit_simulator", b"exit_simulator", "factory_reset_config", b"factory_reset_config", "factory_reset_device", b"factory_reset_device", "get_canned_message_module_messages_request", b"get_canned_message_module_messages_request", "get_canned_message_module_messages_response", b"get_canned_message_module_messages_response", "get_channel_request", b"get_channel_request", "get_channel_response", b"get_channel_response", "get_config_request", b"get_config_request", "get_config_response", b"get_config_response", "get_device_connection_status_request", b"get_device_connection_status_request", "get_device_connection_status_response", b"get_device_connection_status_response", "get_device_metadata_request", b"get_device_metadata_request", "get_device_metadata_response", b"get_device_metadata_response", "get_module_config_request", b"get_module_config_request", "get_module_config_response", b"get_module_config_response", "get_node_remote_hardware_pins_request", b"get_node_remote_hardware_pins_request", "get_node_remote_hardware_pins_response", b"get_node_remote_hardware_pins_response", "get_owner_request", b"get_owner_request", "get_owner_response", b"get_owner_response", "get_ringtone_request", b"get_ringtone_request", "get_ringtone_response", b"get_ringtone_response", "get_ui_config_request", b"get_ui_config_request", "get_ui_config_response", b"get_ui_config_response", "nodedb_reset", b"nodedb_reset", "payload_variant", b"payload_variant", "reboot_ota_seconds", b"reboot_ota_seconds", "reboot_seconds", b"reboot_seconds", "remove_by_nodenum", b"remove_by_nodenum", "remove_favorite_node", b"remove_favorite_node", "remove_fixed_position", b"remove_fixed_position", "remove_ignored_node", b"remove_ignored_node", "session_passkey", b"session_passkey", "set_canned_message_module_messages", b"set_canned_message_module_messages", "set_channel", b"set_channel", "set_config", b"set_config", "set_favorite_node", b"set_favorite_node", "set_fixed_position", b"set_fixed_position", "set_ham_mode", b"set_ham_mode", "set_ignored_node", b"set_ignored_node", "set_module_config", b"set_module_config", "set_owner", b"set_owner", "set_ringtone_message", b"set_ringtone_message", "set_scale", b"set_scale", "set_time_only", b"set_time_only", "shutdown_seconds", b"shutdown_seconds", "store_ui_config", b"store_ui_config"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["payload_variant", b"payload_variant"]) -> typing.Literal["get_channel_request", "get_channel_response", "get_owner_request", "get_owner_response", "get_config_request", "get_config_response", "get_module_config_request", "get_module_config_response", "get_canned_message_module_messages_request", "get_canned_message_module_messages_response", "get_device_metadata_request", "get_device_metadata_response", "get_ringtone_request", "get_ringtone_response", "get_device_connection_status_request", "get_device_connection_status_response", "set_ham_mode", "get_node_remote_hardware_pins_request", "get_node_remote_hardware_pins_response", "enter_dfu_mode_request", "delete_file_request", "set_scale", "set_owner", "set_channel", "set_config", "set_module_config", "set_canned_message_module_messages", "set_ringtone_message", "remove_by_nodenum", "set_favorite_node", "remove_favorite_node", "set_fixed_position", "remove_fixed_position", "set_time_only", "get_ui_config_request", "get_ui_config_response", "store_ui_config", "set_ignored_node", "remove_ignored_node", "begin_edit_settings", "commit_edit_settings", "factory_reset_device", "reboot_ota_seconds", "exit_simulator", "reboot_seconds", "shutdown_seconds", "factory_reset_config", "nodedb_reset"] | None: ...

global___AdminMessage = AdminMessage

@typing.final
class HamParameters(google.protobuf.message.Message):
    """
    Parameters for setting up Meshtastic for ameteur radio usage
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CALL_SIGN_FIELD_NUMBER: builtins.int
    TX_POWER_FIELD_NUMBER: builtins.int
    FREQUENCY_FIELD_NUMBER: builtins.int
    SHORT_NAME_FIELD_NUMBER: builtins.int
    call_sign: builtins.str
    """
    Amateur radio call sign, eg. KD2ABC
    """
    tx_power: builtins.int
    """
    Transmit power in dBm at the LoRA transceiver, not including any amplification
    """
    frequency: builtins.float
    """
    The selected frequency of LoRA operation
    Please respect your local laws, regulations, and band plans.
    Ensure your radio is capable of operating of the selected frequency before setting this.
    """
    short_name: builtins.str
    """
    Optional short name of user
    """
    def __init__(
        self,
        *,
        call_sign: builtins.str = ...,
        tx_power: builtins.int = ...,
        frequency: builtins.float = ...,
        short_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["call_sign", b"call_sign", "frequency", b"frequency", "short_name", b"short_name", "tx_power", b"tx_power"]) -> None: ...

global___HamParameters = HamParameters

@typing.final
class NodeRemoteHardwarePinsResponse(google.protobuf.message.Message):
    """
    Response envelope for node_remote_hardware_pins
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NODE_REMOTE_HARDWARE_PINS_FIELD_NUMBER: builtins.int
    @property
    def node_remote_hardware_pins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[meshtastic.protobuf.mesh_pb2.NodeRemoteHardwarePin]:
        """
        Nodes and their respective remote hardware GPIO pins
        """

    def __init__(
        self,
        *,
        node_remote_hardware_pins: collections.abc.Iterable[meshtastic.protobuf.mesh_pb2.NodeRemoteHardwarePin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["node_remote_hardware_pins", b"node_remote_hardware_pins"]) -> None: ...

global___NodeRemoteHardwarePinsResponse = NodeRemoteHardwarePinsResponse
