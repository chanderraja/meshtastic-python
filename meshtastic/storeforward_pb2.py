# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/storeforward.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dmeshtastic/storeforward.proto\"\xf0\x06\n\x0fStoreAndForward\x12,\n\x02rr\x18\x01 \x01(\x0e\x32 .StoreAndForward.RequestResponse\x12,\n\x05stats\x18\x02 \x01(\x0b\x32\x1b.StoreAndForward.StatisticsH\x00\x12+\n\x07history\x18\x03 \x01(\x0b\x32\x18.StoreAndForward.HistoryH\x00\x12/\n\theartbeat\x18\x04 \x01(\x0b\x32\x1a.StoreAndForward.HeartbeatH\x00\x12\x0e\n\x04text\x18\x05 \x01(\x0cH\x00\x1a\xcd\x01\n\nStatistics\x12\x16\n\x0emessages_total\x18\x01 \x01(\r\x12\x16\n\x0emessages_saved\x18\x02 \x01(\r\x12\x14\n\x0cmessages_max\x18\x03 \x01(\r\x12\x0f\n\x07up_time\x18\x04 \x01(\r\x12\x10\n\x08requests\x18\x05 \x01(\r\x12\x18\n\x10requests_history\x18\x06 \x01(\r\x12\x11\n\theartbeat\x18\x07 \x01(\x08\x12\x12\n\nreturn_max\x18\x08 \x01(\r\x12\x15\n\rreturn_window\x18\t \x01(\r\x1aI\n\x07History\x12\x18\n\x10history_messages\x18\x01 \x01(\r\x12\x0e\n\x06window\x18\x02 \x01(\r\x12\x14\n\x0clast_request\x18\x03 \x01(\r\x1a.\n\tHeartbeat\x12\x0e\n\x06period\x18\x01 \x01(\r\x12\x11\n\tsecondary\x18\x02 \x01(\r\"\xbc\x02\n\x0fRequestResponse\x12\t\n\x05UNSET\x10\x00\x12\x10\n\x0cROUTER_ERROR\x10\x01\x12\x14\n\x10ROUTER_HEARTBEAT\x10\x02\x12\x0f\n\x0bROUTER_PING\x10\x03\x12\x0f\n\x0bROUTER_PONG\x10\x04\x12\x0f\n\x0bROUTER_BUSY\x10\x05\x12\x12\n\x0eROUTER_HISTORY\x10\x06\x12\x10\n\x0cROUTER_STATS\x10\x07\x12\x16\n\x12ROUTER_TEXT_DIRECT\x10\x08\x12\x19\n\x15ROUTER_TEXT_BROADCAST\x10\t\x12\x10\n\x0c\x43LIENT_ERROR\x10@\x12\x12\n\x0e\x43LIENT_HISTORY\x10\x41\x12\x10\n\x0c\x43LIENT_STATS\x10\x42\x12\x0f\n\x0b\x43LIENT_PING\x10\x43\x12\x0f\n\x0b\x43LIENT_PONG\x10\x44\x12\x10\n\x0c\x43LIENT_ABORT\x10jB\t\n\x07variantBj\n\x13\x63om.geeksville.meshB\x15StoreAndForwardProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.storeforward_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\025StoreAndForwardProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _STOREANDFORWARD._serialized_start=34
  _STOREANDFORWARD._serialized_end=914
  _STOREANDFORWARD_STATISTICS._serialized_start=256
  _STOREANDFORWARD_STATISTICS._serialized_end=461
  _STOREANDFORWARD_HISTORY._serialized_start=463
  _STOREANDFORWARD_HISTORY._serialized_end=536
  _STOREANDFORWARD_HEARTBEAT._serialized_start=538
  _STOREANDFORWARD_HEARTBEAT._serialized_end=584
  _STOREANDFORWARD_REQUESTRESPONSE._serialized_start=587
  _STOREANDFORWARD_REQUESTRESPONSE._serialized_end=903
# @@protoc_insertion_point(module_scope)
