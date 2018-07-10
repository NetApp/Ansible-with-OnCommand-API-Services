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

    url_path+="disks"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_pool_key != None:
        if flag is 0:
            url_path+="?storage_pool_key="+storage_pool_key
            flag=1
        else:
            url_path+="&storage_pool_key="+storage_pool_key
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if name != None:
        if flag is 0:
            url_path+="?name="+name
            flag=1
        else:
            url_path+="&name="+name
    if uid != None:
        if flag is 0:
            url_path+="?uid="+uid
            flag=1
        else:
            url_path+="&uid="+uid
    if home_node_key != None:
        if flag is 0:
            url_path+="?home_node_key="+home_node_key
            flag=1
        else:
            url_path+="&home_node_key="+home_node_key
    if owner_node_key != None:
        if flag is 0:
            url_path+="?owner_node_key="+owner_node_key
            flag=1
        else:
            url_path+="&owner_node_key="+owner_node_key
    if partitioning_type != None:
        if flag is 0:
            url_path+="?partitioning_type="+partitioning_type
            flag=1
        else:
            url_path+="&partitioning_type="+partitioning_type
    if interface_type != None:
        if flag is 0:
            url_path+="?interface_type="+interface_type
            flag=1
        else:
            url_path+="&interface_type="+interface_type
    if effective_interface_type != None:
        if flag is 0:
            url_path+="?effective_interface_type="+effective_interface_type
            flag=1
        else:
            url_path+="&effective_interface_type="+effective_interface_type
    if model != None:
        if flag is 0:
            url_path+="?model="+model
            flag=1
        else:
            url_path+="&model="+model
    if firmware_revision != None:
        if flag is 0:
            url_path+="?firmware_revision="+firmware_revision
            flag=1
        else:
            url_path+="&firmware_revision="+firmware_revision
    if rpm != None:
        if flag is 0:
            url_path+="?rpm="+rpm
            flag=1
        else:
            url_path+="&rpm="+rpm
    if serial_number != None:
        if flag is 0:
            url_path+="?serial_number="+serial_number
            flag=1
        else:
            url_path+="&serial_number="+serial_number
    if shelf != None:
        if flag is 0:
            url_path+="?shelf="+shelf
            flag=1
        else:
            url_path+="&shelf="+shelf
    if shelf_bay != None:
        if flag is 0:
            url_path+="?shelf_bay="+shelf_bay
            flag=1
        else:
            url_path+="&shelf_bay="+shelf_bay
    if vendor != None:
        if flag is 0:
            url_path+="?vendor="+vendor
            flag=1
        else:
            url_path+="&vendor="+vendor
    if container_type != None:
        if flag is 0:
            url_path+="?container_type="+container_type
            flag=1
        else:
            url_path+="&container_type="+container_type
    if is_failed != None:
        if flag is 0:
            url_path+="?is_failed="+is_failed
            flag=1
        else:
            url_path+="&is_failed="+is_failed
    if physical_blocks != None:
        if flag is 0:
            url_path+="?physical_blocks="+physical_blocks
            flag=1
        else:
            url_path+="&physical_blocks="+physical_blocks
    if raid_position != None:
        if flag is 0:
            url_path+="?raid_position="+raid_position
            flag=1
        else:
            url_path+="&raid_position="+raid_position
    if is_virtual != None:
        if flag is 0:
            url_path+="?is_virtual="+is_virtual
            flag=1
        else:
            url_path+="&is_virtual="+is_virtual
    if usable_data_size != None:
        if flag is 0:
            url_path+="?usable_data_size="+usable_data_size
            flag=1
        else:
            url_path+="&usable_data_size="+usable_data_size
    if usable_root_size != None:
        if flag is 0:
            url_path+="?usable_root_size="+usable_root_size
            flag=1
        else:
            url_path+="&usable_root_size="+usable_root_size
    if bytes_per_sector != None:
        if flag is 0:
            url_path+="?bytes_per_sector="+bytes_per_sector
            flag=1
        else:
            url_path+="&bytes_per_sector="+bytes_per_sector
    if used_blocks != None:
        if flag is 0:
            url_path+="?used_blocks="+used_blocks
            flag=1
        else:
            url_path+="&used_blocks="+used_blocks
    if used_bytes != None:
        if flag is 0:
            url_path+="?used_bytes="+used_bytes
            flag=1
        else:
            url_path+="&used_bytes="+used_bytes
    if total_bytes != None:
        if flag is 0:
            url_path+="?total_bytes="+total_bytes
            flag=1
        else:
            url_path+="&total_bytes="+total_bytes
    if is_zeroed != None:
        if flag is 0:
            url_path+="?is_zeroed="+is_zeroed
            flag=1
        else:
            url_path+="&is_zeroed="+is_zeroed
    if pool != None:
        if flag is 0:
            url_path+="?pool="+pool
            flag=1
        else:
            url_path+="&pool="+pool
    if checksum_compatibility != None:
        if flag is 0:
            url_path+="?checksum_compatibility="+checksum_compatibility
            flag=1
        else:
            url_path+="&checksum_compatibility="+checksum_compatibility
    if is_offline != None:
        if flag is 0:
            url_path+="?is_offline="+is_offline
            flag=1
        else:
            url_path+="&is_offline="+is_offline
    if is_prefailed != None:
        if flag is 0:
            url_path+="?is_prefailed="+is_prefailed
            flag=1
        else:
            url_path+="&is_prefailed="+is_prefailed
    if is_shared != None:
        if flag is 0:
            url_path+="?is_shared="+is_shared
            flag=1
        else:
            url_path+="&is_shared="+is_shared
    if is_local_attach != None:
        if flag is 0:
            url_path+="?is_local_attach="+is_local_attach
            flag=1
        else:
            url_path+="&is_local_attach="+is_local_attach
    if capacity_sectors != None:
        if flag is 0:
            url_path+="?capacity_sectors="+capacity_sectors
            flag=1
        else:
            url_path+="&capacity_sectors="+capacity_sectors
    if right_size_sectors != None:
        if flag is 0:
            url_path+="?right_size_sectors="+right_size_sectors
            flag=1
        else:
            url_path+="&right_size_sectors="+right_size_sectors
    if percent_spares_consumed != None:
        if flag is 0:
            url_path+="?percent_spares_consumed="+percent_spares_consumed
            flag=1
        else:
            url_path+="&percent_spares_consumed="+percent_spares_consumed
    if is_in_fdr != None:
        if flag is 0:
            url_path+="?is_in_fdr="+is_in_fdr
            flag=1
        else:
            url_path+="&is_in_fdr="+is_in_fdr
    if failed_reason != None:
        if flag is 0:
            url_path+="?failed_reason="+failed_reason
            flag=1
        else:
            url_path+="&failed_reason="+failed_reason
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
    url_path+="disks"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (name != None) & (name != key):
        payload['name']=name
    if (uid != None) & (uid != key):
        payload['uid']=uid
    if (home_node_key != None) & (home_node_key != key):
        payload['home_node_key']=home_node_key
    if (owner_node_key != None) & (owner_node_key != key):
        payload['owner_node_key']=owner_node_key
    if (partitioning_type != None) & (partitioning_type != key):
        payload['partitioning_type']=partitioning_type
    if (interface_type != None) & (interface_type != key):
        payload['interface_type']=interface_type
    if (effective_interface_type != None) & (effective_interface_type != key):
        payload['effective_interface_type']=effective_interface_type
    if (model != None) & (model != key):
        payload['model']=model
    if (firmware_revision != None) & (firmware_revision != key):
        payload['firmware_revision']=firmware_revision
    if (rpm != None) & (rpm != key):
        payload['rpm']=rpm
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (shelf != None) & (shelf != key):
        payload['shelf']=shelf
    if (shelf_bay != None) & (shelf_bay != key):
        payload['shelf_bay']=shelf_bay
    if (vendor != None) & (vendor != key):
        payload['vendor']=vendor
    if (container_type != None) & (container_type != key):
        payload['container_type']=container_type
    if (is_failed != None) & (is_failed != key):
        payload['is_failed']=is_failed
    if (physical_blocks != None) & (physical_blocks != key):
        payload['physical_blocks']=physical_blocks
    if (raid_position != None) & (raid_position != key):
        payload['raid_position']=raid_position
    if (is_virtual != None) & (is_virtual != key):
        payload['is_virtual']=is_virtual
    if (usable_data_size != None) & (usable_data_size != key):
        payload['usable_data_size']=usable_data_size
    if (usable_root_size != None) & (usable_root_size != key):
        payload['usable_root_size']=usable_root_size
    if (bytes_per_sector != None) & (bytes_per_sector != key):
        payload['bytes_per_sector']=bytes_per_sector
    if (used_blocks != None) & (used_blocks != key):
        payload['used_blocks']=used_blocks
    if (used_bytes != None) & (used_bytes != key):
        payload['used_bytes']=used_bytes
    if (total_bytes != None) & (total_bytes != key):
        payload['total_bytes']=total_bytes
    if (is_zeroed != None) & (is_zeroed != key):
        payload['is_zeroed']=is_zeroed
    if (pool != None) & (pool != key):
        payload['pool']=pool
    if (checksum_compatibility != None) & (checksum_compatibility != key):
        payload['checksum_compatibility']=checksum_compatibility
    if (is_offline != None) & (is_offline != key):
        payload['is_offline']=is_offline
    if (is_prefailed != None) & (is_prefailed != key):
        payload['is_prefailed']=is_prefailed
    if (is_shared != None) & (is_shared != key):
        payload['is_shared']=is_shared
    if (is_local_attach != None) & (is_local_attach != key):
        payload['is_local_attach']=is_local_attach
    if (capacity_sectors != None) & (capacity_sectors != key):
        payload['capacity_sectors']=capacity_sectors
    if (right_size_sectors != None) & (right_size_sectors != key):
        payload['right_size_sectors']=right_size_sectors
    if (percent_spares_consumed != None) & (percent_spares_consumed != key):
        payload['percent_spares_consumed']=percent_spares_consumed
    if (is_in_fdr != None) & (is_in_fdr != key):
        payload['is_in_fdr']=is_in_fdr
    if (failed_reason != None) & (failed_reason != key):
        payload['failed_reason']=failed_reason
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
    url_path+="disks/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_pool_key != None) & (storage_pool_key != key):
        payload['storage_pool_key']=storage_pool_key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (name != None) & (name != key):
        payload['name']=name
    if (uid != None) & (uid != key):
        payload['uid']=uid
    if (home_node_key != None) & (home_node_key != key):
        payload['home_node_key']=home_node_key
    if (owner_node_key != None) & (owner_node_key != key):
        payload['owner_node_key']=owner_node_key
    if (partitioning_type != None) & (partitioning_type != key):
        payload['partitioning_type']=partitioning_type
    if (interface_type != None) & (interface_type != key):
        payload['interface_type']=interface_type
    if (effective_interface_type != None) & (effective_interface_type != key):
        payload['effective_interface_type']=effective_interface_type
    if (model != None) & (model != key):
        payload['model']=model
    if (firmware_revision != None) & (firmware_revision != key):
        payload['firmware_revision']=firmware_revision
    if (rpm != None) & (rpm != key):
        payload['rpm']=rpm
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (shelf != None) & (shelf != key):
        payload['shelf']=shelf
    if (shelf_bay != None) & (shelf_bay != key):
        payload['shelf_bay']=shelf_bay
    if (vendor != None) & (vendor != key):
        payload['vendor']=vendor
    if (container_type != None) & (container_type != key):
        payload['container_type']=container_type
    if (is_failed != None) & (is_failed != key):
        payload['is_failed']=is_failed
    if (physical_blocks != None) & (physical_blocks != key):
        payload['physical_blocks']=physical_blocks
    if (raid_position != None) & (raid_position != key):
        payload['raid_position']=raid_position
    if (is_virtual != None) & (is_virtual != key):
        payload['is_virtual']=is_virtual
    if (usable_data_size != None) & (usable_data_size != key):
        payload['usable_data_size']=usable_data_size
    if (usable_root_size != None) & (usable_root_size != key):
        payload['usable_root_size']=usable_root_size
    if (bytes_per_sector != None) & (bytes_per_sector != key):
        payload['bytes_per_sector']=bytes_per_sector
    if (used_blocks != None) & (used_blocks != key):
        payload['used_blocks']=used_blocks
    if (used_bytes != None) & (used_bytes != key):
        payload['used_bytes']=used_bytes
    if (total_bytes != None) & (total_bytes != key):
        payload['total_bytes']=total_bytes
    if (is_zeroed != None) & (is_zeroed != key):
        payload['is_zeroed']=is_zeroed
    if (pool != None) & (pool != key):
        payload['pool']=pool
    if (checksum_compatibility != None) & (checksum_compatibility != key):
        payload['checksum_compatibility']=checksum_compatibility
    if (is_offline != None) & (is_offline != key):
        payload['is_offline']=is_offline
    if (is_prefailed != None) & (is_prefailed != key):
        payload['is_prefailed']=is_prefailed
    if (is_shared != None) & (is_shared != key):
        payload['is_shared']=is_shared
    if (is_local_attach != None) & (is_local_attach != key):
        payload['is_local_attach']=is_local_attach
    if (capacity_sectors != None) & (capacity_sectors != key):
        payload['capacity_sectors']=capacity_sectors
    if (right_size_sectors != None) & (right_size_sectors != key):
        payload['right_size_sectors']=right_size_sectors
    if (percent_spares_consumed != None) & (percent_spares_consumed != key):
        payload['percent_spares_consumed']=percent_spares_consumed
    if (is_in_fdr != None) & (is_in_fdr != key):
        payload['is_in_fdr']=is_in_fdr
    if (failed_reason != None) & (failed_reason != key):
        payload['failed_reason']=failed_reason
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
    url_path+="disks/"

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
                "storage_pool_key" : {"required": False, "type": "str"},
                "cluster_key" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "uid" : {"required": False, "type": "str"},
                "home_node_key" : {"required": False, "type": "str"},
                "owner_node_key" : {"required": False, "type": "str"},
                "partitioning_type" : {"required": False, "type": "str"},
                "interface_type" : {"required": False, "type": "str"},
                "effective_interface_type" : {"required": False, "type": "str"},
                "model" : {"required": False, "type": "str"},
                "firmware_revision" : {"required": False, "type": "str"},
                "rpm" : {"required": False, "type": "str"},
                "serial_number" : {"required": False, "type": "str"},
                "shelf" : {"required": False, "type": "str"},
                "shelf_bay" : {"required": False, "type": "str"},
                "vendor" : {"required": False, "type": "str"},
                "container_type" : {"required": False, "type": "str"},
                "is_failed" : {"required": False, "type": "str"},
                "physical_blocks" : {"required": False, "type": "str"},
                "raid_position" : {"required": False, "type": "str"},
                "is_virtual" : {"required": False, "type": "str"},
                "usable_data_size" : {"required": False, "type": "str"},
                "usable_root_size" : {"required": False, "type": "str"},
                "bytes_per_sector" : {"required": False, "type": "str"},
                "used_blocks" : {"required": False, "type": "str"},
                "used_bytes" : {"required": False, "type": "str"},
                "total_bytes" : {"required": False, "type": "str"},
                "is_zeroed" : {"required": False, "type": "str"},
                "pool" : {"required": False, "type": "str"},
                "checksum_compatibility" : {"required": False, "type": "str"},
                "is_offline" : {"required": False, "type": "str"},
                "is_prefailed" : {"required": False, "type": "str"},
                "is_shared" : {"required": False, "type": "str"},
                "is_local_attach" : {"required": False, "type": "str"},
                "capacity_sectors" : {"required": False, "type": "str"},
                "right_size_sectors" : {"required": False, "type": "str"},
                "percent_spares_consumed" : {"required": False, "type": "str"},
                "is_in_fdr" : {"required": False, "type": "str"},
                "failed_reason" : {"required": False, "type": "str"},
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
        global storage_pool_key
        storage_pool_key = module.params["storage_pool_key"]
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global name
        name = module.params["name"]
        global uid
        uid = module.params["uid"]
        global home_node_key
        home_node_key = module.params["home_node_key"]
        global owner_node_key
        owner_node_key = module.params["owner_node_key"]
        global partitioning_type
        partitioning_type = module.params["partitioning_type"]
        global interface_type
        interface_type = module.params["interface_type"]
        global effective_interface_type
        effective_interface_type = module.params["effective_interface_type"]
        global model
        model = module.params["model"]
        global firmware_revision
        firmware_revision = module.params["firmware_revision"]
        global rpm
        rpm = module.params["rpm"]
        global serial_number
        serial_number = module.params["serial_number"]
        global shelf
        shelf = module.params["shelf"]
        global shelf_bay
        shelf_bay = module.params["shelf_bay"]
        global vendor
        vendor = module.params["vendor"]
        global container_type
        container_type = module.params["container_type"]
        global is_failed
        is_failed = module.params["is_failed"]
        global physical_blocks
        physical_blocks = module.params["physical_blocks"]
        global raid_position
        raid_position = module.params["raid_position"]
        global is_virtual
        is_virtual = module.params["is_virtual"]
        global usable_data_size
        usable_data_size = module.params["usable_data_size"]
        global usable_root_size
        usable_root_size = module.params["usable_root_size"]
        global bytes_per_sector
        bytes_per_sector = module.params["bytes_per_sector"]
        global used_blocks
        used_blocks = module.params["used_blocks"]
        global used_bytes
        used_bytes = module.params["used_bytes"]
        global total_bytes
        total_bytes = module.params["total_bytes"]
        global is_zeroed
        is_zeroed = module.params["is_zeroed"]
        global pool
        pool = module.params["pool"]
        global checksum_compatibility
        checksum_compatibility = module.params["checksum_compatibility"]
        global is_offline
        is_offline = module.params["is_offline"]
        global is_prefailed
        is_prefailed = module.params["is_prefailed"]
        global is_shared
        is_shared = module.params["is_shared"]
        global is_local_attach
        is_local_attach = module.params["is_local_attach"]
        global capacity_sectors
        capacity_sectors = module.params["capacity_sectors"]
        global right_size_sectors
        right_size_sectors = module.params["right_size_sectors"]
        global percent_spares_consumed
        percent_spares_consumed = module.params["percent_spares_consumed"]
        global is_in_fdr
        is_in_fdr = module.params["is_in_fdr"]
        global failed_reason
        failed_reason = module.params["failed_reason"]
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
