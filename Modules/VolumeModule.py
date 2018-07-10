#============================================================
#
#
# Copyright (c) 2017 NetApp, Inc. All rights reserved.
# Specifications subject to change without notice.
#
# This sample code is provided AS IS, with no support or
# warranties of any kind, including but not limited to
# warranties of merchantability or fitness of any kind,
# expressed or implied.
#
# Min Python Version = python 2.7
#
#============================================================


#!/usr/bin/python

from ansible.module_utils.basic import *

import requests
import warnings
import sys
import json
import time
warnings.filterwarnings("ignore")


def get():
    url_path        = "/api/" + api_version + "/ontap/"

    flag=0

    url_path+="volumes"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if name != None:
        if flag is 0:
            url_path+="?name="+name
            flag=1
        else:
            url_path+="&name="+name
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if aggregate_key != None:
        if flag is 0:
            url_path+="?aggregate_key="+aggregate_key
            flag=1
        else:
            url_path+="&aggregate_key="+aggregate_key
    if aggregate_keys != None:
        if flag is 0:
            url_path+="?aggregate_keys="+aggregate_keys
            flag=1
        else:
            url_path+="&aggregate_keys="+aggregate_keys
    if export_policy_key != None:
        if flag is 0:
            url_path+="?export_policy_key="+export_policy_key
            flag=1
        else:
            url_path+="&export_policy_key="+export_policy_key
    if clone_parent_key != None:
        if flag is 0:
            url_path+="?clone_parent_key="+clone_parent_key
            flag=1
        else:
            url_path+="&clone_parent_key="+clone_parent_key
    if flex_cache_origin_key != None:
        if flag is 0:
            url_path+="?flex_cache_origin_key="+flex_cache_origin_key
            flag=1
        else:
            url_path+="&flex_cache_origin_key="+flex_cache_origin_key
    if snapshot_policy_key != None:
        if flag is 0:
            url_path+="?snapshot_policy_key="+snapshot_policy_key
            flag=1
        else:
            url_path+="&snapshot_policy_key="+snapshot_policy_key
    if sis_policy_key != None:
        if flag is 0:
            url_path+="?sis_policy_key="+sis_policy_key
            flag=1
        else:
            url_path+="&sis_policy_key="+sis_policy_key
    if qos_policy_group_key != None:
        if flag is 0:
            url_path+="?qos_policy_group_key="+qos_policy_group_key
            flag=1
        else:
            url_path+="&qos_policy_group_key="+qos_policy_group_key
    if instance_uuid != None:
        if flag is 0:
            url_path+="?instance_uuid="+instance_uuid
            flag=1
        else:
            url_path+="&instance_uuid="+instance_uuid
    if size != None:
        if flag is 0:
            url_path+="?size="+size
            flag=1
        else:
            url_path+="&size="+size
    if size_total != None:
        if flag is 0:
            url_path+="?size_total="+size_total
            flag=1
        else:
            url_path+="&size_total="+size_total
    if size_used != None:
        if flag is 0:
            url_path+="?size_used="+size_used
            flag=1
        else:
            url_path+="&size_used="+size_used
    if size_used_percent != None:
        if flag is 0:
            url_path+="?size_used_percent="+size_used_percent
            flag=1
        else:
            url_path+="&size_used_percent="+size_used_percent
    if size_avail != None:
        if flag is 0:
            url_path+="?size_avail="+size_avail
            flag=1
        else:
            url_path+="&size_avail="+size_avail
    if size_avail_percent != None:
        if flag is 0:
            url_path+="?size_avail_percent="+size_avail_percent
            flag=1
        else:
            url_path+="&size_avail_percent="+size_avail_percent
    if is_storage_vm_root != None:
        if flag is 0:
            url_path+="?is_storage_vm_root="+is_storage_vm_root
            flag=1
        else:
            url_path+="&is_storage_vm_root="+is_storage_vm_root
    if state != None:
        if flag is 0:
            url_path+="?state="+state
            flag=1
        else:
            url_path+="&state="+state
    if junction_path != None:
        if flag is 0:
            url_path+="?junction_path="+junction_path
            flag=1
        else:
            url_path+="&junction_path="+junction_path
    if is_junction_active != None:
        if flag is 0:
            url_path+="?is_junction_active="+is_junction_active
            flag=1
        else:
            url_path+="&is_junction_active="+is_junction_active
    if junction_parent_key != None:
        if flag is 0:
            url_path+="?junction_parent_key="+junction_parent_key
            flag=1
        else:
            url_path+="&junction_parent_key="+junction_parent_key
    if style != None:
        if flag is 0:
            url_path+="?style="+style
            flag=1
        else:
            url_path+="&style="+style
    if derived_style != None:
        if flag is 0:
            url_path+="?derived_style="+derived_style
            flag=1
        else:
            url_path+="&derived_style="+derived_style
    if is_sis_volume != None:
        if flag is 0:
            url_path+="?is_sis_volume="+is_sis_volume
            flag=1
        else:
            url_path+="&is_sis_volume="+is_sis_volume
    if is_data_protection_mirror != None:
        if flag is 0:
            url_path+="?is_data_protection_mirror="+is_data_protection_mirror
            flag=1
        else:
            url_path+="&is_data_protection_mirror="+is_data_protection_mirror
    if is_load_sharing_mirror != None:
        if flag is 0:
            url_path+="?is_load_sharing_mirror="+is_load_sharing_mirror
            flag=1
        else:
            url_path+="&is_load_sharing_mirror="+is_load_sharing_mirror
    if is_move_mirror != None:
        if flag is 0:
            url_path+="?is_move_mirror="+is_move_mirror
            flag=1
        else:
            url_path+="&is_move_mirror="+is_move_mirror
    if is_replica_volume != None:
        if flag is 0:
            url_path+="?is_replica_volume="+is_replica_volume
            flag=1
        else:
            url_path+="&is_replica_volume="+is_replica_volume
    if is_space_guarantee_enabled != None:
        if flag is 0:
            url_path+="?is_space_guarantee_enabled="+is_space_guarantee_enabled
            flag=1
        else:
            url_path+="&is_space_guarantee_enabled="+is_space_guarantee_enabled
    if vm_align_sector != None:
        if flag is 0:
            url_path+="?vm_align_sector="+vm_align_sector
            flag=1
        else:
            url_path+="&vm_align_sector="+vm_align_sector
    if vm_align_suffix != None:
        if flag is 0:
            url_path+="?vm_align_suffix="+vm_align_suffix
            flag=1
        else:
            url_path+="&vm_align_suffix="+vm_align_suffix
    if overwrite_reserve != None:
        if flag is 0:
            url_path+="?overwrite_reserve="+overwrite_reserve
            flag=1
        else:
            url_path+="&overwrite_reserve="+overwrite_reserve
    if overwrite_reserve_required != None:
        if flag is 0:
            url_path+="?overwrite_reserve_required="+overwrite_reserve_required
            flag=1
        else:
            url_path+="&overwrite_reserve_required="+overwrite_reserve_required
    if overwrite_reserve_used != None:
        if flag is 0:
            url_path+="?overwrite_reserve_used="+overwrite_reserve_used
            flag=1
        else:
            url_path+="&overwrite_reserve_used="+overwrite_reserve_used
    if overwrite_reserve_avail != None:
        if flag is 0:
            url_path+="?overwrite_reserve_avail="+overwrite_reserve_avail
            flag=1
        else:
            url_path+="&overwrite_reserve_avail="+overwrite_reserve_avail
    if overwrite_reserve_actual_used != None:
        if flag is 0:
            url_path+="?overwrite_reserve_actual_used="+overwrite_reserve_actual_used
            flag=1
        else:
            url_path+="&overwrite_reserve_actual_used="+overwrite_reserve_actual_used
    if snapshot_reserve_size != None:
        if flag is 0:
            url_path+="?snapshot_reserve_size="+snapshot_reserve_size
            flag=1
        else:
            url_path+="&snapshot_reserve_size="+snapshot_reserve_size
    if percentage_snapshot_reserve != None:
        if flag is 0:
            url_path+="?percentage_snapshot_reserve="+percentage_snapshot_reserve
            flag=1
        else:
            url_path+="&percentage_snapshot_reserve="+percentage_snapshot_reserve
    if size_used_by_snapshots != None:
        if flag is 0:
            url_path+="?size_used_by_snapshots="+size_used_by_snapshots
            flag=1
        else:
            url_path+="&size_used_by_snapshots="+size_used_by_snapshots
    if percentage_snapshot_reserve_used != None:
        if flag is 0:
            url_path+="?percentage_snapshot_reserve_used="+percentage_snapshot_reserve_used
            flag=1
        else:
            url_path+="&percentage_snapshot_reserve_used="+percentage_snapshot_reserve_used
    if size_available_for_snapshot != None:
        if flag is 0:
            url_path+="?size_available_for_snapshot="+size_available_for_snapshot
            flag=1
        else:
            url_path+="&size_available_for_snapshot="+size_available_for_snapshot
    if percentage_fractional_reserve != None:
        if flag is 0:
            url_path+="?percentage_fractional_reserve="+percentage_fractional_reserve
            flag=1
        else:
            url_path+="&percentage_fractional_reserve="+percentage_fractional_reserve
    if deduplication_space_saved != None:
        if flag is 0:
            url_path+="?deduplication_space_saved="+deduplication_space_saved
            flag=1
        else:
            url_path+="&deduplication_space_saved="+deduplication_space_saved
    if compression_space_saved != None:
        if flag is 0:
            url_path+="?compression_space_saved="+compression_space_saved
            flag=1
        else:
            url_path+="&compression_space_saved="+compression_space_saved
    if security_style != None:
        if flag is 0:
            url_path+="?security_style="+security_style
            flag=1
        else:
            url_path+="&security_style="+security_style
    if hybrid_cache_eligibility != None:
        if flag is 0:
            url_path+="?hybrid_cache_eligibility="+hybrid_cache_eligibility
            flag=1
        else:
            url_path+="&hybrid_cache_eligibility="+hybrid_cache_eligibility
    if inode_files_used != None:
        if flag is 0:
            url_path+="?inode_files_used="+inode_files_used
            flag=1
        else:
            url_path+="&inode_files_used="+inode_files_used
    if inode_files_total != None:
        if flag is 0:
            url_path+="?inode_files_total="+inode_files_total
            flag=1
        else:
            url_path+="&inode_files_total="+inode_files_total
    if inode_block_type != None:
        if flag is 0:
            url_path+="?inode_block_type="+inode_block_type
            flag=1
        else:
            url_path+="&inode_block_type="+inode_block_type
    if quota_committed != None:
        if flag is 0:
            url_path+="?quota_committed="+quota_committed
            flag=1
        else:
            url_path+="&quota_committed="+quota_committed
    if quota_over_committed != None:
        if flag is 0:
            url_path+="?quota_over_committed="+quota_over_committed
            flag=1
        else:
            url_path+="&quota_over_committed="+quota_over_committed
    if quota_status != None:
        if flag is 0:
            url_path+="?quota_status="+quota_status
            flag=1
        else:
            url_path+="&quota_status="+quota_status
    if flex_cache_min_reserve != None:
        if flag is 0:
            url_path+="?flex_cache_min_reserve="+flex_cache_min_reserve
            flag=1
        else:
            url_path+="&flex_cache_min_reserve="+flex_cache_min_reserve
    if space_guarantee != None:
        if flag is 0:
            url_path+="?space_guarantee="+space_guarantee
            flag=1
        else:
            url_path+="&space_guarantee="+space_guarantee
    if is_snapshot_clone_dependency_enabled != None:
        if flag is 0:
            url_path+="?is_snapshot_clone_dependency_enabled="+is_snapshot_clone_dependency_enabled
            flag=1
        else:
            url_path+="&is_snapshot_clone_dependency_enabled="+is_snapshot_clone_dependency_enabled
    if is_i2p_enabled != None:
        if flag is 0:
            url_path+="?is_i2p_enabled="+is_i2p_enabled
            flag=1
        else:
            url_path+="&is_i2p_enabled="+is_i2p_enabled
    if is_auto_snapshots_enabled != None:
        if flag is 0:
            url_path+="?is_auto_snapshots_enabled="+is_auto_snapshots_enabled
            flag=1
        else:
            url_path+="&is_auto_snapshots_enabled="+is_auto_snapshots_enabled
    if is_snap_dir_access_enabled != None:
        if flag is 0:
            url_path+="?is_snap_dir_access_enabled="+is_snap_dir_access_enabled
            flag=1
        else:
            url_path+="&is_snap_dir_access_enabled="+is_snap_dir_access_enabled
    if language_code != None:
        if flag is 0:
            url_path+="?language_code="+language_code
            flag=1
        else:
            url_path+="&language_code="+language_code
    if vol_type != None:
        if flag is 0:
            url_path+="?vol_type="+vol_type
            flag=1
        else:
            url_path+="&vol_type="+vol_type
    if space_mgmt_option_try_first != None:
        if flag is 0:
            url_path+="?space_mgmt_option_try_first="+space_mgmt_option_try_first
            flag=1
        else:
            url_path+="&space_mgmt_option_try_first="+space_mgmt_option_try_first
    if auto_size_mode != None:
        if flag is 0:
            url_path+="?auto_size_mode="+auto_size_mode
            flag=1
        else:
            url_path+="&auto_size_mode="+auto_size_mode
    if auto_size_maximum_size != None:
        if flag is 0:
            url_path+="?auto_size_maximum_size="+auto_size_maximum_size
            flag=1
        else:
            url_path+="&auto_size_maximum_size="+auto_size_maximum_size
    if auto_size_increment_size != None:
        if flag is 0:
            url_path+="?auto_size_increment_size="+auto_size_increment_size
            flag=1
        else:
            url_path+="&auto_size_increment_size="+auto_size_increment_size
    if is_atime_update_enabled != None:
        if flag is 0:
            url_path+="?is_atime_update_enabled="+is_atime_update_enabled
            flag=1
        else:
            url_path+="&is_atime_update_enabled="+is_atime_update_enabled
    if is_create_ucode_enabled != None:
        if flag is 0:
            url_path+="?is_create_ucode_enabled="+is_create_ucode_enabled
            flag=1
        else:
            url_path+="&is_create_ucode_enabled="+is_create_ucode_enabled
    if is_convert_ucode_enabled != None:
        if flag is 0:
            url_path+="?is_convert_ucode_enabled="+is_convert_ucode_enabled
            flag=1
        else:
            url_path+="&is_convert_ucode_enabled="+is_convert_ucode_enabled
    if is_snapshot_auto_delete_enabled != None:
        if flag is 0:
            url_path+="?is_snapshot_auto_delete_enabled="+is_snapshot_auto_delete_enabled
            flag=1
        else:
            url_path+="&is_snapshot_auto_delete_enabled="+is_snapshot_auto_delete_enabled
    if snapshot_auto_delete_commitment != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_commitment="+snapshot_auto_delete_commitment
            flag=1
        else:
            url_path+="&snapshot_auto_delete_commitment="+snapshot_auto_delete_commitment
    if snapshot_auto_delete_delete_order != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_delete_order="+snapshot_auto_delete_delete_order
            flag=1
        else:
            url_path+="&snapshot_auto_delete_delete_order="+snapshot_auto_delete_delete_order
    if snapshot_auto_delete_defer_delete != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_defer_delete="+snapshot_auto_delete_defer_delete
            flag=1
        else:
            url_path+="&snapshot_auto_delete_defer_delete="+snapshot_auto_delete_defer_delete
    if snapshot_auto_delete_target_free_space != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_target_free_space="+snapshot_auto_delete_target_free_space
            flag=1
        else:
            url_path+="&snapshot_auto_delete_target_free_space="+snapshot_auto_delete_target_free_space
    if snapshot_auto_delete_trigger != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_trigger="+snapshot_auto_delete_trigger
            flag=1
        else:
            url_path+="&snapshot_auto_delete_trigger="+snapshot_auto_delete_trigger
    if snapshot_auto_delete_prefix != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_prefix="+snapshot_auto_delete_prefix
            flag=1
        else:
            url_path+="&snapshot_auto_delete_prefix="+snapshot_auto_delete_prefix
    if snapshot_auto_delete_destroy_list != None:
        if flag is 0:
            url_path+="?snapshot_auto_delete_destroy_list="+snapshot_auto_delete_destroy_list
            flag=1
        else:
            url_path+="&snapshot_auto_delete_destroy_list="+snapshot_auto_delete_destroy_list
    if oldest_snapshot_timestamp != None:
        if flag is 0:
            url_path+="?oldest_snapshot_timestamp="+oldest_snapshot_timestamp
            flag=1
        else:
            url_path+="&oldest_snapshot_timestamp="+oldest_snapshot_timestamp
    if sis_status != None:
        if flag is 0:
            url_path+="?sis_status="+sis_status
            flag=1
        else:
            url_path+="&sis_status="+sis_status
    if sis_state != None:
        if flag is 0:
            url_path+="?sis_state="+sis_state
            flag=1
        else:
            url_path+="&sis_state="+sis_state
    if sis_progress != None:
        if flag is 0:
            url_path+="?sis_progress="+sis_progress
            flag=1
        else:
            url_path+="&sis_progress="+sis_progress
    if sis_type != None:
        if flag is 0:
            url_path+="?sis_type="+sis_type
            flag=1
        else:
            url_path+="&sis_type="+sis_type
    if sis_schedule != None:
        if flag is 0:
            url_path+="?sis_schedule="+sis_schedule
            flag=1
        else:
            url_path+="&sis_schedule="+sis_schedule
    if sis_last_op_begin_timestamp != None:
        if flag is 0:
            url_path+="?sis_last_op_begin_timestamp="+sis_last_op_begin_timestamp
            flag=1
        else:
            url_path+="&sis_last_op_begin_timestamp="+sis_last_op_begin_timestamp
    if sis_last_op_end_timestamp != None:
        if flag is 0:
            url_path+="?sis_last_op_end_timestamp="+sis_last_op_end_timestamp
            flag=1
        else:
            url_path+="&sis_last_op_end_timestamp="+sis_last_op_end_timestamp
    if sis_last_op_error != None:
        if flag is 0:
            url_path+="?sis_last_op_error="+sis_last_op_error
            flag=1
        else:
            url_path+="&sis_last_op_error="+sis_last_op_error
    if sis_last_op_state != None:
        if flag is 0:
            url_path+="?sis_last_op_state="+sis_last_op_state
            flag=1
        else:
            url_path+="&sis_last_op_state="+sis_last_op_state
    if sis_last_op_size != None:
        if flag is 0:
            url_path+="?sis_last_op_size="+sis_last_op_size
            flag=1
        else:
            url_path+="&sis_last_op_size="+sis_last_op_size
    if is_sis_compression_enabled != None:
        if flag is 0:
            url_path+="?is_sis_compression_enabled="+is_sis_compression_enabled
            flag=1
        else:
            url_path+="&is_sis_compression_enabled="+is_sis_compression_enabled
    if is_sis_inline_compression_enabled != None:
        if flag is 0:
            url_path+="?is_sis_inline_compression_enabled="+is_sis_inline_compression_enabled
            flag=1
        else:
            url_path+="&is_sis_inline_compression_enabled="+is_sis_inline_compression_enabled
    if is_sis_inline_dedupe_enabled != None:
        if flag is 0:
            url_path+="?is_sis_inline_dedupe_enabled="+is_sis_inline_dedupe_enabled
            flag=1
        else:
            url_path+="&is_sis_inline_dedupe_enabled="+is_sis_inline_dedupe_enabled
    if percentage_deduplication_space_saved != None:
        if flag is 0:
            url_path+="?percentage_deduplication_space_saved="+percentage_deduplication_space_saved
            flag=1
        else:
            url_path+="&percentage_deduplication_space_saved="+percentage_deduplication_space_saved
    if percentage_compression_space_saved != None:
        if flag is 0:
            url_path+="?percentage_compression_space_saved="+percentage_compression_space_saved
            flag=1
        else:
            url_path+="&percentage_compression_space_saved="+percentage_compression_space_saved
    if security_user_id != None:
        if flag is 0:
            url_path+="?security_user_id="+security_user_id
            flag=1
        else:
            url_path+="&security_user_id="+security_user_id
    if security_group_id != None:
        if flag is 0:
            url_path+="?security_group_id="+security_group_id
            flag=1
        else:
            url_path+="&security_group_id="+security_group_id
    if security_permissions != None:
        if flag is 0:
            url_path+="?security_permissions="+security_permissions
            flag=1
        else:
            url_path+="&security_permissions="+security_permissions
    if sortBy != None:
        if flag is 0:
            url_path+="?sortBy="+sortBy
            flag=1
        else:
            url_path+="&sortBy="+sortBy
    if maxRecords != None:
        if flag is 0:
            url_path+="?maxRecords="+maxRecords
            flag=1
        else:
            url_path+="&maxRecords="+maxRecords
    if nextTag != None:
        if flag is 0:
            url_path+="?nextTag="+nextTag
            flag=1
        else:
            url_path+="&nextTag="+nextTag
    response=http_request_for_get(url_path)
    json_response=response.json()
    return json_response

def post():
    url_path        = "/api/" + api_version + "/ontap/"
    url_path+="volumes"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (aggregate_keys != None) & (aggregate_keys != key):
        payload['aggregate_keys']=aggregate_keys
    if (export_policy_key != None) & (export_policy_key != key):
        payload['export_policy_key']=export_policy_key
    if (clone_parent_key != None) & (clone_parent_key != key):
        payload['clone_parent_key']=clone_parent_key
    if (flex_cache_origin_key != None) & (flex_cache_origin_key != key):
        payload['flex_cache_origin_key']=flex_cache_origin_key
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
    if (sis_policy_key != None) & (sis_policy_key != key):
        payload['sis_policy_key']=sis_policy_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (instance_uuid != None) & (instance_uuid != key):
        payload['instance_uuid']=instance_uuid
    if (size != None) & (size != key):
        payload['size']=size
    if (size_total != None) & (size_total != key):
        payload['size_total']=size_total
    if (size_used != None) & (size_used != key):
        payload['size_used']=size_used
    if (size_used_percent != None) & (size_used_percent != key):
        payload['size_used_percent']=size_used_percent
    if (size_avail != None) & (size_avail != key):
        payload['size_avail']=size_avail
    if (size_avail_percent != None) & (size_avail_percent != key):
        payload['size_avail_percent']=size_avail_percent
    if (is_storage_vm_root != None) & (is_storage_vm_root != key):
        payload['is_storage_vm_root']=is_storage_vm_root
    if (state != None) & (state != key):
        payload['state']=state
    if (junction_path != None) & (junction_path != key):
        payload['junction_path']=junction_path
    if (is_junction_active != None) & (is_junction_active != key):
        payload['is_junction_active']=is_junction_active
    if (junction_parent_key != None) & (junction_parent_key != key):
        payload['junction_parent_key']=junction_parent_key
    if (style != None) & (style != key):
        payload['style']=style
    if (derived_style != None) & (derived_style != key):
        payload['derived_style']=derived_style
    if (is_sis_volume != None) & (is_sis_volume != key):
        payload['is_sis_volume']=is_sis_volume
    if (is_data_protection_mirror != None) & (is_data_protection_mirror != key):
        payload['is_data_protection_mirror']=is_data_protection_mirror
    if (is_load_sharing_mirror != None) & (is_load_sharing_mirror != key):
        payload['is_load_sharing_mirror']=is_load_sharing_mirror
    if (is_move_mirror != None) & (is_move_mirror != key):
        payload['is_move_mirror']=is_move_mirror
    if (is_replica_volume != None) & (is_replica_volume != key):
        payload['is_replica_volume']=is_replica_volume
    if (is_space_guarantee_enabled != None) & (is_space_guarantee_enabled != key):
        payload['is_space_guarantee_enabled']=is_space_guarantee_enabled
    if (vm_align_sector != None) & (vm_align_sector != key):
        payload['vm_align_sector']=vm_align_sector
    if (vm_align_suffix != None) & (vm_align_suffix != key):
        payload['vm_align_suffix']=vm_align_suffix
    if (overwrite_reserve != None) & (overwrite_reserve != key):
        payload['overwrite_reserve']=overwrite_reserve
    if (overwrite_reserve_required != None) & (overwrite_reserve_required != key):
        payload['overwrite_reserve_required']=overwrite_reserve_required
    if (overwrite_reserve_used != None) & (overwrite_reserve_used != key):
        payload['overwrite_reserve_used']=overwrite_reserve_used
    if (overwrite_reserve_avail != None) & (overwrite_reserve_avail != key):
        payload['overwrite_reserve_avail']=overwrite_reserve_avail
    if (overwrite_reserve_actual_used != None) & (overwrite_reserve_actual_used != key):
        payload['overwrite_reserve_actual_used']=overwrite_reserve_actual_used
    if (snapshot_reserve_size != None) & (snapshot_reserve_size != key):
        payload['snapshot_reserve_size']=snapshot_reserve_size
    if (percentage_snapshot_reserve != None) & (percentage_snapshot_reserve != key):
        payload['percentage_snapshot_reserve']=percentage_snapshot_reserve
    if (size_used_by_snapshots != None) & (size_used_by_snapshots != key):
        payload['size_used_by_snapshots']=size_used_by_snapshots
    if (percentage_snapshot_reserve_used != None) & (percentage_snapshot_reserve_used != key):
        payload['percentage_snapshot_reserve_used']=percentage_snapshot_reserve_used
    if (size_available_for_snapshot != None) & (size_available_for_snapshot != key):
        payload['size_available_for_snapshot']=size_available_for_snapshot
    if (percentage_fractional_reserve != None) & (percentage_fractional_reserve != key):
        payload['percentage_fractional_reserve']=percentage_fractional_reserve
    if (deduplication_space_saved != None) & (deduplication_space_saved != key):
        payload['deduplication_space_saved']=deduplication_space_saved
    if (compression_space_saved != None) & (compression_space_saved != key):
        payload['compression_space_saved']=compression_space_saved
    if (security_style != None) & (security_style != key):
        payload['security_style']=security_style
    if (hybrid_cache_eligibility != None) & (hybrid_cache_eligibility != key):
        payload['hybrid_cache_eligibility']=hybrid_cache_eligibility
    if (inode_files_used != None) & (inode_files_used != key):
        payload['inode_files_used']=inode_files_used
    if (inode_files_total != None) & (inode_files_total != key):
        payload['inode_files_total']=inode_files_total
    if (inode_block_type != None) & (inode_block_type != key):
        payload['inode_block_type']=inode_block_type
    if (quota_committed != None) & (quota_committed != key):
        payload['quota_committed']=quota_committed
    if (quota_over_committed != None) & (quota_over_committed != key):
        payload['quota_over_committed']=quota_over_committed
    if (quota_status != None) & (quota_status != key):
        payload['quota_status']=quota_status
    if (flex_cache_min_reserve != None) & (flex_cache_min_reserve != key):
        payload['flex_cache_min_reserve']=flex_cache_min_reserve
    if (space_guarantee != None) & (space_guarantee != key):
        payload['space_guarantee']=space_guarantee
    if (is_snapshot_clone_dependency_enabled != None) & (is_snapshot_clone_dependency_enabled != key):
        payload['is_snapshot_clone_dependency_enabled']=is_snapshot_clone_dependency_enabled
    if (is_i2p_enabled != None) & (is_i2p_enabled != key):
        payload['is_i2p_enabled']=is_i2p_enabled
    if (is_auto_snapshots_enabled != None) & (is_auto_snapshots_enabled != key):
        payload['is_auto_snapshots_enabled']=is_auto_snapshots_enabled
    if (is_snap_dir_access_enabled != None) & (is_snap_dir_access_enabled != key):
        payload['is_snap_dir_access_enabled']=is_snap_dir_access_enabled
    if (language_code != None) & (language_code != key):
        payload['language_code']=language_code
    if (vol_type != None) & (vol_type != key):
        payload['vol_type']=vol_type
    if (space_mgmt_option_try_first != None) & (space_mgmt_option_try_first != key):
        payload['space_mgmt_option_try_first']=space_mgmt_option_try_first
    if (auto_size_mode != None) & (auto_size_mode != key):
        payload['auto_size_mode']=auto_size_mode
    if (auto_size_maximum_size != None) & (auto_size_maximum_size != key):
        payload['auto_size_maximum_size']=auto_size_maximum_size
    if (auto_size_increment_size != None) & (auto_size_increment_size != key):
        payload['auto_size_increment_size']=auto_size_increment_size
    if (is_atime_update_enabled != None) & (is_atime_update_enabled != key):
        payload['is_atime_update_enabled']=is_atime_update_enabled
    if (is_create_ucode_enabled != None) & (is_create_ucode_enabled != key):
        payload['is_create_ucode_enabled']=is_create_ucode_enabled
    if (is_convert_ucode_enabled != None) & (is_convert_ucode_enabled != key):
        payload['is_convert_ucode_enabled']=is_convert_ucode_enabled
    if (is_snapshot_auto_delete_enabled != None) & (is_snapshot_auto_delete_enabled != key):
        payload['is_snapshot_auto_delete_enabled']=is_snapshot_auto_delete_enabled
    if (snapshot_auto_delete_commitment != None) & (snapshot_auto_delete_commitment != key):
        payload['snapshot_auto_delete_commitment']=snapshot_auto_delete_commitment
    if (snapshot_auto_delete_delete_order != None) & (snapshot_auto_delete_delete_order != key):
        payload['snapshot_auto_delete_delete_order']=snapshot_auto_delete_delete_order
    if (snapshot_auto_delete_defer_delete != None) & (snapshot_auto_delete_defer_delete != key):
        payload['snapshot_auto_delete_defer_delete']=snapshot_auto_delete_defer_delete
    if (snapshot_auto_delete_target_free_space != None) & (snapshot_auto_delete_target_free_space != key):
        payload['snapshot_auto_delete_target_free_space']=snapshot_auto_delete_target_free_space
    if (snapshot_auto_delete_trigger != None) & (snapshot_auto_delete_trigger != key):
        payload['snapshot_auto_delete_trigger']=snapshot_auto_delete_trigger
    if (snapshot_auto_delete_prefix != None) & (snapshot_auto_delete_prefix != key):
        payload['snapshot_auto_delete_prefix']=snapshot_auto_delete_prefix
    if (snapshot_auto_delete_destroy_list != None) & (snapshot_auto_delete_destroy_list != key):
        payload['snapshot_auto_delete_destroy_list']=snapshot_auto_delete_destroy_list
    if (oldest_snapshot_timestamp != None) & (oldest_snapshot_timestamp != key):
        payload['oldest_snapshot_timestamp']=oldest_snapshot_timestamp
    if (sis_status != None) & (sis_status != key):
        payload['sis_status']=sis_status
    if (sis_state != None) & (sis_state != key):
        payload['sis_state']=sis_state
    if (sis_progress != None) & (sis_progress != key):
        payload['sis_progress']=sis_progress
    if (sis_type != None) & (sis_type != key):
        payload['sis_type']=sis_type
    if (sis_schedule != None) & (sis_schedule != key):
        payload['sis_schedule']=sis_schedule
    if (sis_last_op_begin_timestamp != None) & (sis_last_op_begin_timestamp != key):
        payload['sis_last_op_begin_timestamp']=sis_last_op_begin_timestamp
    if (sis_last_op_end_timestamp != None) & (sis_last_op_end_timestamp != key):
        payload['sis_last_op_end_timestamp']=sis_last_op_end_timestamp
    if (sis_last_op_error != None) & (sis_last_op_error != key):
        payload['sis_last_op_error']=sis_last_op_error
    if (sis_last_op_state != None) & (sis_last_op_state != key):
        payload['sis_last_op_state']=sis_last_op_state
    if (sis_last_op_size != None) & (sis_last_op_size != key):
        payload['sis_last_op_size']=sis_last_op_size
    if (is_sis_compression_enabled != None) & (is_sis_compression_enabled != key):
        payload['is_sis_compression_enabled']=is_sis_compression_enabled
    if (is_sis_inline_compression_enabled != None) & (is_sis_inline_compression_enabled != key):
        payload['is_sis_inline_compression_enabled']=is_sis_inline_compression_enabled
    if (is_sis_inline_dedupe_enabled != None) & (is_sis_inline_dedupe_enabled != key):
        payload['is_sis_inline_dedupe_enabled']=is_sis_inline_dedupe_enabled
    if (percentage_deduplication_space_saved != None) & (percentage_deduplication_space_saved != key):
        payload['percentage_deduplication_space_saved']=percentage_deduplication_space_saved
    if (percentage_compression_space_saved != None) & (percentage_compression_space_saved != key):
        payload['percentage_compression_space_saved']=percentage_compression_space_saved
    if (security_user_id != None) & (security_user_id != key):
        payload['security_user_id']=security_user_id
    if (security_group_id != None) & (security_group_id != key):
        payload['security_group_id']=security_group_id
    if (security_permissions != None) & (security_permissions != key):
        payload['security_permissions']=security_permissions
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.headers
    return json_response

def put():
    url_path        = "/api/" + api_version + "/ontap/"
    url_path+="volumes/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (aggregate_keys != None) & (aggregate_keys != key):
        payload['aggregate_keys']=aggregate_keys
    if (export_policy_key != None) & (export_policy_key != key):
        payload['export_policy_key']=export_policy_key
    if (clone_parent_key != None) & (clone_parent_key != key):
        payload['clone_parent_key']=clone_parent_key
    if (flex_cache_origin_key != None) & (flex_cache_origin_key != key):
        payload['flex_cache_origin_key']=flex_cache_origin_key
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
    if (sis_policy_key != None) & (sis_policy_key != key):
        payload['sis_policy_key']=sis_policy_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (instance_uuid != None) & (instance_uuid != key):
        payload['instance_uuid']=instance_uuid
    if (size != None) & (size != key):
        payload['size']=size
    if (size_total != None) & (size_total != key):
        payload['size_total']=size_total
    if (size_used != None) & (size_used != key):
        payload['size_used']=size_used
    if (size_used_percent != None) & (size_used_percent != key):
        payload['size_used_percent']=size_used_percent
    if (size_avail != None) & (size_avail != key):
        payload['size_avail']=size_avail
    if (size_avail_percent != None) & (size_avail_percent != key):
        payload['size_avail_percent']=size_avail_percent
    if (is_storage_vm_root != None) & (is_storage_vm_root != key):
        payload['is_storage_vm_root']=is_storage_vm_root
    if (state != None) & (state != key):
        payload['state']=state
    if (junction_path != None) & (junction_path != key):
        payload['junction_path']=junction_path
    if (is_junction_active != None) & (is_junction_active != key):
        payload['is_junction_active']=is_junction_active
    if (junction_parent_key != None) & (junction_parent_key != key):
        payload['junction_parent_key']=junction_parent_key
    if (style != None) & (style != key):
        payload['style']=style
    if (derived_style != None) & (derived_style != key):
        payload['derived_style']=derived_style
    if (is_sis_volume != None) & (is_sis_volume != key):
        payload['is_sis_volume']=is_sis_volume
    if (is_data_protection_mirror != None) & (is_data_protection_mirror != key):
        payload['is_data_protection_mirror']=is_data_protection_mirror
    if (is_load_sharing_mirror != None) & (is_load_sharing_mirror != key):
        payload['is_load_sharing_mirror']=is_load_sharing_mirror
    if (is_move_mirror != None) & (is_move_mirror != key):
        payload['is_move_mirror']=is_move_mirror
    if (is_replica_volume != None) & (is_replica_volume != key):
        payload['is_replica_volume']=is_replica_volume
    if (is_space_guarantee_enabled != None) & (is_space_guarantee_enabled != key):
        payload['is_space_guarantee_enabled']=is_space_guarantee_enabled
    if (vm_align_sector != None) & (vm_align_sector != key):
        payload['vm_align_sector']=vm_align_sector
    if (vm_align_suffix != None) & (vm_align_suffix != key):
        payload['vm_align_suffix']=vm_align_suffix
    if (overwrite_reserve != None) & (overwrite_reserve != key):
        payload['overwrite_reserve']=overwrite_reserve
    if (overwrite_reserve_required != None) & (overwrite_reserve_required != key):
        payload['overwrite_reserve_required']=overwrite_reserve_required
    if (overwrite_reserve_used != None) & (overwrite_reserve_used != key):
        payload['overwrite_reserve_used']=overwrite_reserve_used
    if (overwrite_reserve_avail != None) & (overwrite_reserve_avail != key):
        payload['overwrite_reserve_avail']=overwrite_reserve_avail
    if (overwrite_reserve_actual_used != None) & (overwrite_reserve_actual_used != key):
        payload['overwrite_reserve_actual_used']=overwrite_reserve_actual_used
    if (snapshot_reserve_size != None) & (snapshot_reserve_size != key):
        payload['snapshot_reserve_size']=snapshot_reserve_size
    if (percentage_snapshot_reserve != None) & (percentage_snapshot_reserve != key):
        payload['percentage_snapshot_reserve']=percentage_snapshot_reserve
    if (size_used_by_snapshots != None) & (size_used_by_snapshots != key):
        payload['size_used_by_snapshots']=size_used_by_snapshots
    if (percentage_snapshot_reserve_used != None) & (percentage_snapshot_reserve_used != key):
        payload['percentage_snapshot_reserve_used']=percentage_snapshot_reserve_used
    if (size_available_for_snapshot != None) & (size_available_for_snapshot != key):
        payload['size_available_for_snapshot']=size_available_for_snapshot
    if (percentage_fractional_reserve != None) & (percentage_fractional_reserve != key):
        payload['percentage_fractional_reserve']=percentage_fractional_reserve
    if (deduplication_space_saved != None) & (deduplication_space_saved != key):
        payload['deduplication_space_saved']=deduplication_space_saved
    if (compression_space_saved != None) & (compression_space_saved != key):
        payload['compression_space_saved']=compression_space_saved
    if (security_style != None) & (security_style != key):
        payload['security_style']=security_style
    if (hybrid_cache_eligibility != None) & (hybrid_cache_eligibility != key):
        payload['hybrid_cache_eligibility']=hybrid_cache_eligibility
    if (inode_files_used != None) & (inode_files_used != key):
        payload['inode_files_used']=inode_files_used
    if (inode_files_total != None) & (inode_files_total != key):
        payload['inode_files_total']=inode_files_total
    if (inode_block_type != None) & (inode_block_type != key):
        payload['inode_block_type']=inode_block_type
    if (quota_committed != None) & (quota_committed != key):
        payload['quota_committed']=quota_committed
    if (quota_over_committed != None) & (quota_over_committed != key):
        payload['quota_over_committed']=quota_over_committed
    if (quota_status != None) & (quota_status != key):
        payload['quota_status']=quota_status
    if (flex_cache_min_reserve != None) & (flex_cache_min_reserve != key):
        payload['flex_cache_min_reserve']=flex_cache_min_reserve
    if (space_guarantee != None) & (space_guarantee != key):
        payload['space_guarantee']=space_guarantee
    if (is_snapshot_clone_dependency_enabled != None) & (is_snapshot_clone_dependency_enabled != key):
        payload['is_snapshot_clone_dependency_enabled']=is_snapshot_clone_dependency_enabled
    if (is_i2p_enabled != None) & (is_i2p_enabled != key):
        payload['is_i2p_enabled']=is_i2p_enabled
    if (is_auto_snapshots_enabled != None) & (is_auto_snapshots_enabled != key):
        payload['is_auto_snapshots_enabled']=is_auto_snapshots_enabled
    if (is_snap_dir_access_enabled != None) & (is_snap_dir_access_enabled != key):
        payload['is_snap_dir_access_enabled']=is_snap_dir_access_enabled
    if (language_code != None) & (language_code != key):
        payload['language_code']=language_code
    if (vol_type != None) & (vol_type != key):
        payload['vol_type']=vol_type
    if (space_mgmt_option_try_first != None) & (space_mgmt_option_try_first != key):
        payload['space_mgmt_option_try_first']=space_mgmt_option_try_first
    if (auto_size_mode != None) & (auto_size_mode != key):
        payload['auto_size_mode']=auto_size_mode
    if (auto_size_maximum_size != None) & (auto_size_maximum_size != key):
        payload['auto_size_maximum_size']=auto_size_maximum_size
    if (auto_size_increment_size != None) & (auto_size_increment_size != key):
        payload['auto_size_increment_size']=auto_size_increment_size
    if (is_atime_update_enabled != None) & (is_atime_update_enabled != key):
        payload['is_atime_update_enabled']=is_atime_update_enabled
    if (is_create_ucode_enabled != None) & (is_create_ucode_enabled != key):
        payload['is_create_ucode_enabled']=is_create_ucode_enabled
    if (is_convert_ucode_enabled != None) & (is_convert_ucode_enabled != key):
        payload['is_convert_ucode_enabled']=is_convert_ucode_enabled
    if (is_snapshot_auto_delete_enabled != None) & (is_snapshot_auto_delete_enabled != key):
        payload['is_snapshot_auto_delete_enabled']=is_snapshot_auto_delete_enabled
    if (snapshot_auto_delete_commitment != None) & (snapshot_auto_delete_commitment != key):
        payload['snapshot_auto_delete_commitment']=snapshot_auto_delete_commitment
    if (snapshot_auto_delete_delete_order != None) & (snapshot_auto_delete_delete_order != key):
        payload['snapshot_auto_delete_delete_order']=snapshot_auto_delete_delete_order
    if (snapshot_auto_delete_defer_delete != None) & (snapshot_auto_delete_defer_delete != key):
        payload['snapshot_auto_delete_defer_delete']=snapshot_auto_delete_defer_delete
    if (snapshot_auto_delete_target_free_space != None) & (snapshot_auto_delete_target_free_space != key):
        payload['snapshot_auto_delete_target_free_space']=snapshot_auto_delete_target_free_space
    if (snapshot_auto_delete_trigger != None) & (snapshot_auto_delete_trigger != key):
        payload['snapshot_auto_delete_trigger']=snapshot_auto_delete_trigger
    if (snapshot_auto_delete_prefix != None) & (snapshot_auto_delete_prefix != key):
        payload['snapshot_auto_delete_prefix']=snapshot_auto_delete_prefix
    if (snapshot_auto_delete_destroy_list != None) & (snapshot_auto_delete_destroy_list != key):
        payload['snapshot_auto_delete_destroy_list']=snapshot_auto_delete_destroy_list
    if (oldest_snapshot_timestamp != None) & (oldest_snapshot_timestamp != key):
        payload['oldest_snapshot_timestamp']=oldest_snapshot_timestamp
    if (sis_status != None) & (sis_status != key):
        payload['sis_status']=sis_status
    if (sis_state != None) & (sis_state != key):
        payload['sis_state']=sis_state
    if (sis_progress != None) & (sis_progress != key):
        payload['sis_progress']=sis_progress
    if (sis_type != None) & (sis_type != key):
        payload['sis_type']=sis_type
    if (sis_schedule != None) & (sis_schedule != key):
        payload['sis_schedule']=sis_schedule
    if (sis_last_op_begin_timestamp != None) & (sis_last_op_begin_timestamp != key):
        payload['sis_last_op_begin_timestamp']=sis_last_op_begin_timestamp
    if (sis_last_op_end_timestamp != None) & (sis_last_op_end_timestamp != key):
        payload['sis_last_op_end_timestamp']=sis_last_op_end_timestamp
    if (sis_last_op_error != None) & (sis_last_op_error != key):
        payload['sis_last_op_error']=sis_last_op_error
    if (sis_last_op_state != None) & (sis_last_op_state != key):
        payload['sis_last_op_state']=sis_last_op_state
    if (sis_last_op_size != None) & (sis_last_op_size != key):
        payload['sis_last_op_size']=sis_last_op_size
    if (is_sis_compression_enabled != None) & (is_sis_compression_enabled != key):
        payload['is_sis_compression_enabled']=is_sis_compression_enabled
    if (is_sis_inline_compression_enabled != None) & (is_sis_inline_compression_enabled != key):
        payload['is_sis_inline_compression_enabled']=is_sis_inline_compression_enabled
    if (is_sis_inline_dedupe_enabled != None) & (is_sis_inline_dedupe_enabled != key):
        payload['is_sis_inline_dedupe_enabled']=is_sis_inline_dedupe_enabled
    if (percentage_deduplication_space_saved != None) & (percentage_deduplication_space_saved != key):
        payload['percentage_deduplication_space_saved']=percentage_deduplication_space_saved
    if (percentage_compression_space_saved != None) & (percentage_compression_space_saved != key):
        payload['percentage_compression_space_saved']=percentage_compression_space_saved
    if (security_user_id != None) & (security_user_id != key):
        payload['security_user_id']=security_user_id
    if (security_group_id != None) & (security_group_id != key):
        payload['security_group_id']=security_group_id
    if (security_permissions != None) & (security_permissions != key):
        payload['security_permissions']=security_permissions
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path        = "/api/" + api_version + "/ontap/"
    url_path+="volumes/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.headers
        return json_response
    else:
        return "Provide the object key for deletion"

def http_request_for_get(url_path,**payload):
	response = requests.get("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_put(url_path,**payload):
	response = requests.put("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_post(url_path,**payload):
	response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response

def http_request_for_delete(url_path,**payload):
	response = requests.delete("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
	return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": ['get', 'put', 'post', 'delete'],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "api_version" : {"required": False, "choices": [ '1.0', '2.0', '3.0', '4.0', '5.0' ], type: "str", "default": '2.0'},
                "key" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "aggregate_key" : {"required": False, "type": "str"},
                "aggregate_keys" : {"required": False, "type": "list"},
                "export_policy_key" : {"required": False, "type": "str"},
                "clone_parent_key" : {"required": False, "type": "str"},
                "flex_cache_origin_key" : {"required": False, "type": "str"},
                "snapshot_policy_key" : {"required": False, "type": "str"},
                "sis_policy_key" : {"required": False, "type": "str"},
                "qos_policy_group_key" : {"required": False, "type": "str"},
                "instance_uuid" : {"required": False, "type": "str"},
                "size" : {"required": False, "type": "str"},
                "size_total" : {"required": False, "type": "str"},
                "size_used" : {"required": False, "type": "str"},
                "size_used_percent" : {"required": False, "type": "str"},
                "size_avail" : {"required": False, "type": "str"},
                "size_avail_percent" : {"required": False, "type": "str"},
                "is_storage_vm_root" : {"required": False, "type": "str"},
                "state" : {"required": False, "type": "str"},
                "junction_path" : {"required": False, "type": "str"},
                "is_junction_active" : {"required": False, "type": "str"},
                "junction_parent_key" : {"required": False, "type": "str"},
                "style" : {"required": False, "type": "str"},
                "derived_style" : {"required": False, "type": "str"},
                "is_sis_volume" : {"required": False, "type": "str"},
                "is_data_protection_mirror" : {"required": False, "type": "str"},
                "is_load_sharing_mirror" : {"required": False, "type": "str"},
                "is_move_mirror" : {"required": False, "type": "str"},
                "is_replica_volume" : {"required": False, "type": "str"},
                "is_space_guarantee_enabled" : {"required": False, "type": "str"},
                "vm_align_sector" : {"required": False, "type": "str"},
                "vm_align_suffix" : {"required": False, "type": "str"},
                "overwrite_reserve" : {"required": False, "type": "str"},
                "overwrite_reserve_required" : {"required": False, "type": "str"},
                "overwrite_reserve_used" : {"required": False, "type": "str"},
                "overwrite_reserve_avail" : {"required": False, "type": "str"},
                "overwrite_reserve_actual_used" : {"required": False, "type": "str"},
                "snapshot_reserve_size" : {"required": False, "type": "str"},
                "percentage_snapshot_reserve" : {"required": False, "type": "str"},
                "size_used_by_snapshots" : {"required": False, "type": "str"},
                "percentage_snapshot_reserve_used" : {"required": False, "type": "str"},
                "size_available_for_snapshot" : {"required": False, "type": "str"},
                "percentage_fractional_reserve" : {"required": False, "type": "str"},
                "deduplication_space_saved" : {"required": False, "type": "str"},
                "compression_space_saved" : {"required": False, "type": "str"},
                "security_style" : {"required": False, "type": "str"},
                "hybrid_cache_eligibility" : {"required": False, "type": "str"},
                "inode_files_used" : {"required": False, "type": "str"},
                "inode_files_total" : {"required": False, "type": "str"},
                "inode_block_type" : {"required": False, "type": "str"},
                "quota_committed" : {"required": False, "type": "str"},
                "quota_over_committed" : {"required": False, "type": "str"},
                "quota_status" : {"required": False, "type": "str"},
                "flex_cache_min_reserve" : {"required": False, "type": "str"},
                "space_guarantee" : {"required": False, "type": "str"},
                "is_snapshot_clone_dependency_enabled" : {"required": False, "type": "str"},
                "is_i2p_enabled" : {"required": False, "type": "str"},
                "is_auto_snapshots_enabled" : {"required": False, "type": "str"},
                "is_snap_dir_access_enabled" : {"required": False, "type": "str"},
                "language_code" : {"required": False, "type": "str"},
                "vol_type" : {"required": False, "type": "str"},
                "space_mgmt_option_try_first" : {"required": False, "type": "str"},
                "auto_size_mode" : {"required": False, "type": "str"},
                "auto_size_maximum_size" : {"required": False, "type": "str"},
                "auto_size_increment_size" : {"required": False, "type": "str"},
                "is_atime_update_enabled" : {"required": False, "type": "str"},
                "is_create_ucode_enabled" : {"required": False, "type": "str"},
                "is_convert_ucode_enabled" : {"required": False, "type": "str"},
                "is_snapshot_auto_delete_enabled" : {"required": False, "type": "str"},
                "snapshot_auto_delete_commitment" : {"required": False, "type": "str"},
                "snapshot_auto_delete_delete_order" : {"required": False, "type": "str"},
                "snapshot_auto_delete_defer_delete" : {"required": False, "type": "str"},
                "snapshot_auto_delete_target_free_space" : {"required": False, "type": "str"},
                "snapshot_auto_delete_trigger" : {"required": False, "type": "str"},
                "snapshot_auto_delete_prefix" : {"required": False, "type": "str"},
                "snapshot_auto_delete_destroy_list" : {"required": False, "type": "str"},
                "oldest_snapshot_timestamp" : {"required": False, "type": "str"},
                "sis_status" : {"required": False, "type": "str"},
                "sis_state" : {"required": False, "type": "str"},
                "sis_progress" : {"required": False, "type": "str"},
                "sis_type" : {"required": False, "type": "str"},
                "sis_schedule" : {"required": False, "type": "str"},
                "sis_last_op_begin_timestamp" : {"required": False, "type": "str"},
                "sis_last_op_end_timestamp" : {"required": False, "type": "str"},
                "sis_last_op_error" : {"required": False, "type": "str"},
                "sis_last_op_state" : {"required": False, "type": "str"},
                "sis_last_op_size" : {"required": False, "type": "str"},
                "is_sis_compression_enabled" : {"required": False, "type": "str"},
                "is_sis_inline_compression_enabled" : {"required": False, "type": "str"},
                "is_sis_inline_dedupe_enabled" : {"required": False, "type": "str"},
                "percentage_deduplication_space_saved" : {"required": False, "type": "str"},
                "percentage_compression_space_saved" : {"required": False, "type": "str"},
                "security_user_id" : {"required": False, "type": "str"},
                "security_group_id" : {"required": False, "type": "str"},
                "security_permissions" : {"required": False, "type": "str"},
                "sortBy" : {"required": False, "type": "str"},
                "maxRecords" : {"required": False, "type": "str"},
                "nextTag" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global api_version

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]
        api_version             = module.params["api_version"]

        # Properties details
        global key
        key = module.params["key"]
        global name
        name = module.params["name"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global aggregate_key
        aggregate_key = module.params["aggregate_key"]
        global aggregate_keys
        aggregate_keys = module.params["aggregate_keys"]
        global export_policy_key
        export_policy_key = module.params["export_policy_key"]
        global clone_parent_key
        clone_parent_key = module.params["clone_parent_key"]
        global flex_cache_origin_key
        flex_cache_origin_key = module.params["flex_cache_origin_key"]
        global snapshot_policy_key
        snapshot_policy_key = module.params["snapshot_policy_key"]
        global sis_policy_key
        sis_policy_key = module.params["sis_policy_key"]
        global qos_policy_group_key
        qos_policy_group_key = module.params["qos_policy_group_key"]
        global instance_uuid
        instance_uuid = module.params["instance_uuid"]
        global size
        size = module.params["size"]
        global size_total
        size_total = module.params["size_total"]
        global size_used
        size_used = module.params["size_used"]
        global size_used_percent
        size_used_percent = module.params["size_used_percent"]
        global size_avail
        size_avail = module.params["size_avail"]
        global size_avail_percent
        size_avail_percent = module.params["size_avail_percent"]
        global is_storage_vm_root
        is_storage_vm_root = module.params["is_storage_vm_root"]
        global state
        state = module.params["state"]
        global junction_path
        junction_path = module.params["junction_path"]
        global is_junction_active
        is_junction_active = module.params["is_junction_active"]
        global junction_parent_key
        junction_parent_key = module.params["junction_parent_key"]
        global style
        style = module.params["style"]
        global derived_style
        derived_style = module.params["derived_style"]
        global is_sis_volume
        is_sis_volume = module.params["is_sis_volume"]
        global is_data_protection_mirror
        is_data_protection_mirror = module.params["is_data_protection_mirror"]
        global is_load_sharing_mirror
        is_load_sharing_mirror = module.params["is_load_sharing_mirror"]
        global is_move_mirror
        is_move_mirror = module.params["is_move_mirror"]
        global is_replica_volume
        is_replica_volume = module.params["is_replica_volume"]
        global is_space_guarantee_enabled
        is_space_guarantee_enabled = module.params["is_space_guarantee_enabled"]
        global vm_align_sector
        vm_align_sector = module.params["vm_align_sector"]
        global vm_align_suffix
        vm_align_suffix = module.params["vm_align_suffix"]
        global overwrite_reserve
        overwrite_reserve = module.params["overwrite_reserve"]
        global overwrite_reserve_required
        overwrite_reserve_required = module.params["overwrite_reserve_required"]
        global overwrite_reserve_used
        overwrite_reserve_used = module.params["overwrite_reserve_used"]
        global overwrite_reserve_avail
        overwrite_reserve_avail = module.params["overwrite_reserve_avail"]
        global overwrite_reserve_actual_used
        overwrite_reserve_actual_used = module.params["overwrite_reserve_actual_used"]
        global snapshot_reserve_size
        snapshot_reserve_size = module.params["snapshot_reserve_size"]
        global percentage_snapshot_reserve
        percentage_snapshot_reserve = module.params["percentage_snapshot_reserve"]
        global size_used_by_snapshots
        size_used_by_snapshots = module.params["size_used_by_snapshots"]
        global percentage_snapshot_reserve_used
        percentage_snapshot_reserve_used = module.params["percentage_snapshot_reserve_used"]
        global size_available_for_snapshot
        size_available_for_snapshot = module.params["size_available_for_snapshot"]
        global percentage_fractional_reserve
        percentage_fractional_reserve = module.params["percentage_fractional_reserve"]
        global deduplication_space_saved
        deduplication_space_saved = module.params["deduplication_space_saved"]
        global compression_space_saved
        compression_space_saved = module.params["compression_space_saved"]
        global security_style
        security_style = module.params["security_style"]
        global hybrid_cache_eligibility
        hybrid_cache_eligibility = module.params["hybrid_cache_eligibility"]
        global inode_files_used
        inode_files_used = module.params["inode_files_used"]
        global inode_files_total
        inode_files_total = module.params["inode_files_total"]
        global inode_block_type
        inode_block_type = module.params["inode_block_type"]
        global quota_committed
        quota_committed = module.params["quota_committed"]
        global quota_over_committed
        quota_over_committed = module.params["quota_over_committed"]
        global quota_status
        quota_status = module.params["quota_status"]
        global flex_cache_min_reserve
        flex_cache_min_reserve = module.params["flex_cache_min_reserve"]
        global space_guarantee
        space_guarantee = module.params["space_guarantee"]
        global is_snapshot_clone_dependency_enabled
        is_snapshot_clone_dependency_enabled = module.params["is_snapshot_clone_dependency_enabled"]
        global is_i2p_enabled
        is_i2p_enabled = module.params["is_i2p_enabled"]
        global is_auto_snapshots_enabled
        is_auto_snapshots_enabled = module.params["is_auto_snapshots_enabled"]
        global is_snap_dir_access_enabled
        is_snap_dir_access_enabled = module.params["is_snap_dir_access_enabled"]
        global language_code
        language_code = module.params["language_code"]
        global vol_type
        vol_type = module.params["vol_type"]
        global space_mgmt_option_try_first
        space_mgmt_option_try_first = module.params["space_mgmt_option_try_first"]
        global auto_size_mode
        auto_size_mode = module.params["auto_size_mode"]
        global auto_size_maximum_size
        auto_size_maximum_size = module.params["auto_size_maximum_size"]
        global auto_size_increment_size
        auto_size_increment_size = module.params["auto_size_increment_size"]
        global is_atime_update_enabled
        is_atime_update_enabled = module.params["is_atime_update_enabled"]
        global is_create_ucode_enabled
        is_create_ucode_enabled = module.params["is_create_ucode_enabled"]
        global is_convert_ucode_enabled
        is_convert_ucode_enabled = module.params["is_convert_ucode_enabled"]
        global is_snapshot_auto_delete_enabled
        is_snapshot_auto_delete_enabled = module.params["is_snapshot_auto_delete_enabled"]
        global snapshot_auto_delete_commitment
        snapshot_auto_delete_commitment = module.params["snapshot_auto_delete_commitment"]
        global snapshot_auto_delete_delete_order
        snapshot_auto_delete_delete_order = module.params["snapshot_auto_delete_delete_order"]
        global snapshot_auto_delete_defer_delete
        snapshot_auto_delete_defer_delete = module.params["snapshot_auto_delete_defer_delete"]
        global snapshot_auto_delete_target_free_space
        snapshot_auto_delete_target_free_space = module.params["snapshot_auto_delete_target_free_space"]
        global snapshot_auto_delete_trigger
        snapshot_auto_delete_trigger = module.params["snapshot_auto_delete_trigger"]
        global snapshot_auto_delete_prefix
        snapshot_auto_delete_prefix = module.params["snapshot_auto_delete_prefix"]
        global snapshot_auto_delete_destroy_list
        snapshot_auto_delete_destroy_list = module.params["snapshot_auto_delete_destroy_list"]
        global oldest_snapshot_timestamp
        oldest_snapshot_timestamp = module.params["oldest_snapshot_timestamp"]
        global sis_status
        sis_status = module.params["sis_status"]
        global sis_state
        sis_state = module.params["sis_state"]
        global sis_progress
        sis_progress = module.params["sis_progress"]
        global sis_type
        sis_type = module.params["sis_type"]
        global sis_schedule
        sis_schedule = module.params["sis_schedule"]
        global sis_last_op_begin_timestamp
        sis_last_op_begin_timestamp = module.params["sis_last_op_begin_timestamp"]
        global sis_last_op_end_timestamp
        sis_last_op_end_timestamp = module.params["sis_last_op_end_timestamp"]
        global sis_last_op_error
        sis_last_op_error = module.params["sis_last_op_error"]
        global sis_last_op_state
        sis_last_op_state = module.params["sis_last_op_state"]
        global sis_last_op_size
        sis_last_op_size = module.params["sis_last_op_size"]
        global is_sis_compression_enabled
        is_sis_compression_enabled = module.params["is_sis_compression_enabled"]
        global is_sis_inline_compression_enabled
        is_sis_inline_compression_enabled = module.params["is_sis_inline_compression_enabled"]
        global is_sis_inline_dedupe_enabled
        is_sis_inline_dedupe_enabled = module.params["is_sis_inline_dedupe_enabled"]
        global percentage_deduplication_space_saved
        percentage_deduplication_space_saved = module.params["percentage_deduplication_space_saved"]
        global percentage_compression_space_saved
        percentage_compression_space_saved = module.params["percentage_compression_space_saved"]
        global security_user_id
        security_user_id = module.params["security_user_id"]
        global security_group_id
        security_group_id = module.params["security_group_id"]
        global security_permissions
        security_permissions = module.params["security_permissions"]
        global sortBy
        sortBy = module.params["sortBy"]
        global maxRecords
        maxRecords = module.params["maxRecords"]
        global nextTag
        nextTag = module.params["nextTag"]

        global json_response

        # Actions
        if module.params["action"] == "get":
                result=get()
                module.exit_json(changed=False,meta=result)
        elif module.params["action"] == "put":
                result=put()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result['Location'].split("/jobs/")[1])


if __name__ == '__main__':
    main()
