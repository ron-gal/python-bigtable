# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bigtable/v2/data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dgoogle/bigtable/v2/data.proto\x12\x12google.bigtable.v2\"@\n\x03Row\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12,\n\x08\x66\x61milies\x18\x02 \x03(\x0b\x32\x1a.google.bigtable.v2.Family\"C\n\x06\x46\x61mily\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x07\x63olumns\x18\x02 \x03(\x0b\x32\x1a.google.bigtable.v2.Column\"D\n\x06\x43olumn\x12\x11\n\tqualifier\x18\x01 \x01(\x0c\x12\'\n\x05\x63\x65lls\x18\x02 \x03(\x0b\x32\x18.google.bigtable.v2.Cell\"?\n\x04\x43\x65ll\x12\x18\n\x10timestamp_micros\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x0e\n\x06labels\x18\x03 \x03(\t\"\x8a\x01\n\x08RowRange\x12\x1a\n\x10start_key_closed\x18\x01 \x01(\x0cH\x00\x12\x18\n\x0estart_key_open\x18\x02 \x01(\x0cH\x00\x12\x16\n\x0c\x65nd_key_open\x18\x03 \x01(\x0cH\x01\x12\x18\n\x0e\x65nd_key_closed\x18\x04 \x01(\x0cH\x01\x42\x0b\n\tstart_keyB\t\n\x07\x65nd_key\"L\n\x06RowSet\x12\x10\n\x08row_keys\x18\x01 \x03(\x0c\x12\x30\n\nrow_ranges\x18\x02 \x03(\x0b\x32\x1c.google.bigtable.v2.RowRange\"\xc6\x01\n\x0b\x43olumnRange\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x12 \n\x16start_qualifier_closed\x18\x02 \x01(\x0cH\x00\x12\x1e\n\x14start_qualifier_open\x18\x03 \x01(\x0cH\x00\x12\x1e\n\x14\x65nd_qualifier_closed\x18\x04 \x01(\x0cH\x01\x12\x1c\n\x12\x65nd_qualifier_open\x18\x05 \x01(\x0cH\x01\x42\x11\n\x0fstart_qualifierB\x0f\n\rend_qualifier\"N\n\x0eTimestampRange\x12\x1e\n\x16start_timestamp_micros\x18\x01 \x01(\x03\x12\x1c\n\x14\x65nd_timestamp_micros\x18\x02 \x01(\x03\"\x98\x01\n\nValueRange\x12\x1c\n\x12start_value_closed\x18\x01 \x01(\x0cH\x00\x12\x1a\n\x10start_value_open\x18\x02 \x01(\x0cH\x00\x12\x1a\n\x10\x65nd_value_closed\x18\x03 \x01(\x0cH\x01\x12\x18\n\x0e\x65nd_value_open\x18\x04 \x01(\x0cH\x01\x42\r\n\x0bstart_valueB\x0b\n\tend_value\"\xdf\x08\n\tRowFilter\x12\x34\n\x05\x63hain\x18\x01 \x01(\x0b\x32#.google.bigtable.v2.RowFilter.ChainH\x00\x12>\n\ninterleave\x18\x02 \x01(\x0b\x32(.google.bigtable.v2.RowFilter.InterleaveH\x00\x12<\n\tcondition\x18\x03 \x01(\x0b\x32\'.google.bigtable.v2.RowFilter.ConditionH\x00\x12\x0e\n\x04sink\x18\x10 \x01(\x08H\x00\x12\x19\n\x0fpass_all_filter\x18\x11 \x01(\x08H\x00\x12\x1a\n\x10\x62lock_all_filter\x18\x12 \x01(\x08H\x00\x12\x1e\n\x14row_key_regex_filter\x18\x04 \x01(\x0cH\x00\x12\x1b\n\x11row_sample_filter\x18\x0e \x01(\x01H\x00\x12\"\n\x18\x66\x61mily_name_regex_filter\x18\x05 \x01(\tH\x00\x12\'\n\x1d\x63olumn_qualifier_regex_filter\x18\x06 \x01(\x0cH\x00\x12>\n\x13\x63olumn_range_filter\x18\x07 \x01(\x0b\x32\x1f.google.bigtable.v2.ColumnRangeH\x00\x12\x44\n\x16timestamp_range_filter\x18\x08 \x01(\x0b\x32\".google.bigtable.v2.TimestampRangeH\x00\x12\x1c\n\x12value_regex_filter\x18\t \x01(\x0cH\x00\x12<\n\x12value_range_filter\x18\x0f \x01(\x0b\x32\x1e.google.bigtable.v2.ValueRangeH\x00\x12%\n\x1b\x63\x65lls_per_row_offset_filter\x18\n \x01(\x05H\x00\x12$\n\x1a\x63\x65lls_per_row_limit_filter\x18\x0b \x01(\x05H\x00\x12\'\n\x1d\x63\x65lls_per_column_limit_filter\x18\x0c \x01(\x05H\x00\x12!\n\x17strip_value_transformer\x18\r \x01(\x08H\x00\x12!\n\x17\x61pply_label_transformer\x18\x13 \x01(\tH\x00\x1a\x37\n\x05\x43hain\x12.\n\x07\x66ilters\x18\x01 \x03(\x0b\x32\x1d.google.bigtable.v2.RowFilter\x1a<\n\nInterleave\x12.\n\x07\x66ilters\x18\x01 \x03(\x0b\x32\x1d.google.bigtable.v2.RowFilter\x1a\xad\x01\n\tCondition\x12\x37\n\x10predicate_filter\x18\x01 \x01(\x0b\x32\x1d.google.bigtable.v2.RowFilter\x12\x32\n\x0btrue_filter\x18\x02 \x01(\x0b\x32\x1d.google.bigtable.v2.RowFilter\x12\x33\n\x0c\x66\x61lse_filter\x18\x03 \x01(\x0b\x32\x1d.google.bigtable.v2.RowFilterB\x08\n\x06\x66ilter\"\xc9\x04\n\x08Mutation\x12\x38\n\x08set_cell\x18\x01 \x01(\x0b\x32$.google.bigtable.v2.Mutation.SetCellH\x00\x12K\n\x12\x64\x65lete_from_column\x18\x02 \x01(\x0b\x32-.google.bigtable.v2.Mutation.DeleteFromColumnH\x00\x12K\n\x12\x64\x65lete_from_family\x18\x03 \x01(\x0b\x32-.google.bigtable.v2.Mutation.DeleteFromFamilyH\x00\x12\x45\n\x0f\x64\x65lete_from_row\x18\x04 \x01(\x0b\x32*.google.bigtable.v2.Mutation.DeleteFromRowH\x00\x1a\x61\n\x07SetCell\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x12\x18\n\x10\x63olumn_qualifier\x18\x02 \x01(\x0c\x12\x18\n\x10timestamp_micros\x18\x03 \x01(\x03\x12\r\n\x05value\x18\x04 \x01(\x0c\x1ay\n\x10\x44\x65leteFromColumn\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x12\x18\n\x10\x63olumn_qualifier\x18\x02 \x01(\x0c\x12\x36\n\ntime_range\x18\x03 \x01(\x0b\x32\".google.bigtable.v2.TimestampRange\x1a\'\n\x10\x44\x65leteFromFamily\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x1a\x0f\n\rDeleteFromRowB\n\n\x08mutation\"\x80\x01\n\x13ReadModifyWriteRule\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x01(\t\x12\x18\n\x10\x63olumn_qualifier\x18\x02 \x01(\x0c\x12\x16\n\x0c\x61ppend_value\x18\x03 \x01(\x0cH\x00\x12\x1a\n\x10increment_amount\x18\x04 \x01(\x03H\x00\x42\x06\n\x04rule\"B\n\x0fStreamPartition\x12/\n\trow_range\x18\x01 \x01(\x0b\x32\x1c.google.bigtable.v2.RowRange\"W\n\x18StreamContinuationTokens\x12;\n\x06tokens\x18\x01 \x03(\x0b\x32+.google.bigtable.v2.StreamContinuationToken\"`\n\x17StreamContinuationToken\x12\x36\n\tpartition\x18\x01 \x01(\x0b\x32#.google.bigtable.v2.StreamPartition\x12\r\n\x05token\x18\x02 \x01(\tB\xb5\x01\n\x16\x63om.google.bigtable.v2B\tDataProtoP\x01Z:google.golang.org/genproto/googleapis/bigtable/v2;bigtable\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.v2.data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.google.bigtable.v2B\tDataProtoP\001Z:google.golang.org/genproto/googleapis/bigtable/v2;bigtable\252\002\030Google.Cloud.Bigtable.V2\312\002\030Google\\Cloud\\Bigtable\\V2\352\002\033Google::Cloud::Bigtable::V2'
  _ROW._serialized_start=53
  _ROW._serialized_end=117
  _FAMILY._serialized_start=119
  _FAMILY._serialized_end=186
  _COLUMN._serialized_start=188
  _COLUMN._serialized_end=256
  _CELL._serialized_start=258
  _CELL._serialized_end=321
  _ROWRANGE._serialized_start=324
  _ROWRANGE._serialized_end=462
  _ROWSET._serialized_start=464
  _ROWSET._serialized_end=540
  _COLUMNRANGE._serialized_start=543
  _COLUMNRANGE._serialized_end=741
  _TIMESTAMPRANGE._serialized_start=743
  _TIMESTAMPRANGE._serialized_end=821
  _VALUERANGE._serialized_start=824
  _VALUERANGE._serialized_end=976
  _ROWFILTER._serialized_start=979
  _ROWFILTER._serialized_end=2098
  _ROWFILTER_CHAIN._serialized_start=1795
  _ROWFILTER_CHAIN._serialized_end=1850
  _ROWFILTER_INTERLEAVE._serialized_start=1852
  _ROWFILTER_INTERLEAVE._serialized_end=1912
  _ROWFILTER_CONDITION._serialized_start=1915
  _ROWFILTER_CONDITION._serialized_end=2088
  _MUTATION._serialized_start=2101
  _MUTATION._serialized_end=2686
  _MUTATION_SETCELL._serialized_start=2396
  _MUTATION_SETCELL._serialized_end=2493
  _MUTATION_DELETEFROMCOLUMN._serialized_start=2495
  _MUTATION_DELETEFROMCOLUMN._serialized_end=2616
  _MUTATION_DELETEFROMFAMILY._serialized_start=2618
  _MUTATION_DELETEFROMFAMILY._serialized_end=2657
  _MUTATION_DELETEFROMROW._serialized_start=2659
  _MUTATION_DELETEFROMROW._serialized_end=2674
  _READMODIFYWRITERULE._serialized_start=2689
  _READMODIFYWRITERULE._serialized_end=2817
  _STREAMPARTITION._serialized_start=2819
  _STREAMPARTITION._serialized_end=2885
  _STREAMCONTINUATIONTOKENS._serialized_start=2887
  _STREAMCONTINUATIONTOKENS._serialized_end=2974
  _STREAMCONTINUATIONTOKEN._serialized_start=2976
  _STREAMCONTINUATIONTOKEN._serialized_end=3072
# @@protoc_insertion_point(module_scope)
