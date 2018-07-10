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

    url_path+="aggregates"

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
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if node_key != None:
        if flag is 0:
            url_path+="?node_key="+node_key
            flag=1
        else:
            url_path+="&node_key="+node_key
    if is_hybrid != None:
        if flag is 0:
            url_path+="?is_hybrid="+is_hybrid
            flag=1
        else:
            url_path+="&is_hybrid="+is_hybrid
    if is_hybrid_enabled != None:
        if flag is 0:
            url_path+="?is_hybrid_enabled="+is_hybrid_enabled
            flag=1
        else:
            url_path+="&is_hybrid_enabled="+is_hybrid_enabled
    if is_snaplock != None:
        if flag is 0:
            url_path+="?is_snaplock="+is_snaplock
            flag=1
        else:
            url_path+="&is_snaplock="+is_snaplock
    if snaplock_type != None:
        if flag is 0:
            url_path+="?snaplock_type="+snaplock_type
            flag=1
        else:
            url_path+="&snaplock_type="+snaplock_type
    if uses_shared_disks != None:
        if flag is 0:
            url_path+="?uses_shared_disks="+uses_shared_disks
            flag=1
        else:
            url_path+="&uses_shared_disks="+uses_shared_disks
    if state != None:
        if flag is 0:
            url_path+="?state="+state
            flag=1
        else:
            url_path+="&state="+state
    if aggregate_type != None:
        if flag is 0:
            url_path+="?aggregate_type="+aggregate_type
            flag=1
        else:
            url_path+="&aggregate_type="+aggregate_type
    if snapshot_size_total != None:
        if flag is 0:
            url_path+="?snapshot_size_total="+snapshot_size_total
            flag=1
        else:
            url_path+="&snapshot_size_total="+snapshot_size_total
    if snapshot_size_used != None:
        if flag is 0:
            url_path+="?snapshot_size_used="+snapshot_size_used
            flag=1
        else:
            url_path+="&snapshot_size_used="+snapshot_size_used
    if snapshot_size_avail != None:
        if flag is 0:
            url_path+="?snapshot_size_avail="+snapshot_size_avail
            flag=1
        else:
            url_path+="&snapshot_size_avail="+snapshot_size_avail
    if hybrid_cache_size_total != None:
        if flag is 0:
            url_path+="?hybrid_cache_size_total="+hybrid_cache_size_total
            flag=1
        else:
            url_path+="&hybrid_cache_size_total="+hybrid_cache_size_total
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
    if total_committed != None:
        if flag is 0:
            url_path+="?total_committed="+total_committed
            flag=1
        else:
            url_path+="&total_committed="+total_committed
    if total_reserved_space != None:
        if flag is 0:
            url_path+="?total_reserved_space="+total_reserved_space
            flag=1
        else:
            url_path+="&total_reserved_space="+total_reserved_space
    if raid_status != None:
        if flag is 0:
            url_path+="?raid_status="+raid_status
            flag=1
        else:
            url_path+="&raid_status="+raid_status
    if raid_type != None:
        if flag is 0:
            url_path+="?raid_type="+raid_type
            flag=1
        else:
            url_path+="&raid_type="+raid_type
    if mirror_status != None:
        if flag is 0:
            url_path+="?mirror_status="+mirror_status
            flag=1
        else:
            url_path+="&mirror_status="+mirror_status
    if block_type != None:
        if flag is 0:
            url_path+="?block_type="+block_type
            flag=1
        else:
            url_path+="&block_type="+block_type
    if volume_dedupe_space_savings != None:
        if flag is 0:
            url_path+="?volume_dedupe_space_savings="+volume_dedupe_space_savings
            flag=1
        else:
            url_path+="&volume_dedupe_space_savings="+volume_dedupe_space_savings
    if volume_compression_space_savings != None:
        if flag is 0:
            url_path+="?volume_compression_space_savings="+volume_compression_space_savings
            flag=1
        else:
            url_path+="&volume_compression_space_savings="+volume_compression_space_savings
    if raid_size != None:
        if flag is 0:
            url_path+="?raid_size="+raid_size
            flag=1
        else:
            url_path+="&raid_size="+raid_size
    if has_local_root != None:
        if flag is 0:
            url_path+="?has_local_root="+has_local_root
            flag=1
        else:
            url_path+="&has_local_root="+has_local_root
    if has_partner_root != None:
        if flag is 0:
            url_path+="?has_partner_root="+has_partner_root
            flag=1
        else:
            url_path+="&has_partner_root="+has_partner_root
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
    url_path+="aggregates"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (is_hybrid != None) & (is_hybrid != key):
        payload['is_hybrid']=is_hybrid
    if (is_hybrid_enabled != None) & (is_hybrid_enabled != key):
        payload['is_hybrid_enabled']=is_hybrid_enabled
    if (is_snaplock != None) & (is_snaplock != key):
        payload['is_snaplock']=is_snaplock
    if (snaplock_type != None) & (snaplock_type != key):
        payload['snaplock_type']=snaplock_type
    if (uses_shared_disks != None) & (uses_shared_disks != key):
        payload['uses_shared_disks']=uses_shared_disks
    if (state != None) & (state != key):
        payload['state']=state
    if (aggregate_type != None) & (aggregate_type != key):
        payload['aggregate_type']=aggregate_type
    if (snapshot_size_total != None) & (snapshot_size_total != key):
        payload['snapshot_size_total']=snapshot_size_total
    if (snapshot_size_used != None) & (snapshot_size_used != key):
        payload['snapshot_size_used']=snapshot_size_used
    if (snapshot_size_avail != None) & (snapshot_size_avail != key):
        payload['snapshot_size_avail']=snapshot_size_avail
    if (hybrid_cache_size_total != None) & (hybrid_cache_size_total != key):
        payload['hybrid_cache_size_total']=hybrid_cache_size_total
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
    if (total_committed != None) & (total_committed != key):
        payload['total_committed']=total_committed
    if (total_reserved_space != None) & (total_reserved_space != key):
        payload['total_reserved_space']=total_reserved_space
    if (raid_status != None) & (raid_status != key):
        payload['raid_status']=raid_status
    if (raid_type != None) & (raid_type != key):
        payload['raid_type']=raid_type
    if (mirror_status != None) & (mirror_status != key):
        payload['mirror_status']=mirror_status
    if (block_type != None) & (block_type != key):
        payload['block_type']=block_type
    if (volume_dedupe_space_savings != None) & (volume_dedupe_space_savings != key):
        payload['volume_dedupe_space_savings']=volume_dedupe_space_savings
    if (volume_compression_space_savings != None) & (volume_compression_space_savings != key):
        payload['volume_compression_space_savings']=volume_compression_space_savings
    if (raid_size != None) & (raid_size != key):
        payload['raid_size']=raid_size
    if (has_local_root != None) & (has_local_root != key):
        payload['has_local_root']=has_local_root
    if (has_partner_root != None) & (has_partner_root != key):
        payload['has_partner_root']=has_partner_root
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
    url_path+="aggregates/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (is_hybrid != None) & (is_hybrid != key):
        payload['is_hybrid']=is_hybrid
    if (is_hybrid_enabled != None) & (is_hybrid_enabled != key):
        payload['is_hybrid_enabled']=is_hybrid_enabled
    if (is_snaplock != None) & (is_snaplock != key):
        payload['is_snaplock']=is_snaplock
    if (snaplock_type != None) & (snaplock_type != key):
        payload['snaplock_type']=snaplock_type
    if (uses_shared_disks != None) & (uses_shared_disks != key):
        payload['uses_shared_disks']=uses_shared_disks
    if (state != None) & (state != key):
        payload['state']=state
    if (aggregate_type != None) & (aggregate_type != key):
        payload['aggregate_type']=aggregate_type
    if (snapshot_size_total != None) & (snapshot_size_total != key):
        payload['snapshot_size_total']=snapshot_size_total
    if (snapshot_size_used != None) & (snapshot_size_used != key):
        payload['snapshot_size_used']=snapshot_size_used
    if (snapshot_size_avail != None) & (snapshot_size_avail != key):
        payload['snapshot_size_avail']=snapshot_size_avail
    if (hybrid_cache_size_total != None) & (hybrid_cache_size_total != key):
        payload['hybrid_cache_size_total']=hybrid_cache_size_total
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
    if (total_committed != None) & (total_committed != key):
        payload['total_committed']=total_committed
    if (total_reserved_space != None) & (total_reserved_space != key):
        payload['total_reserved_space']=total_reserved_space
    if (raid_status != None) & (raid_status != key):
        payload['raid_status']=raid_status
    if (raid_type != None) & (raid_type != key):
        payload['raid_type']=raid_type
    if (mirror_status != None) & (mirror_status != key):
        payload['mirror_status']=mirror_status
    if (block_type != None) & (block_type != key):
        payload['block_type']=block_type
    if (volume_dedupe_space_savings != None) & (volume_dedupe_space_savings != key):
        payload['volume_dedupe_space_savings']=volume_dedupe_space_savings
    if (volume_compression_space_savings != None) & (volume_compression_space_savings != key):
        payload['volume_compression_space_savings']=volume_compression_space_savings
    if (raid_size != None) & (raid_size != key):
        payload['raid_size']=raid_size
    if (has_local_root != None) & (has_local_root != key):
        payload['has_local_root']=has_local_root
    if (has_partner_root != None) & (has_partner_root != key):
        payload['has_partner_root']=has_partner_root
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
    url_path+="aggregates/"

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
                "cluster_key" : {"required": False, "type": "str"},
                "node_key" : {"required": False, "type": "str"},
                "is_hybrid" : {"required": False, "type": "str"},
                "is_hybrid_enabled" : {"required": False, "type": "str"},
                "is_snaplock" : {"required": False, "type": "str"},
                "snaplock_type" : {"required": False, "type": "str"},
                "uses_shared_disks" : {"required": False, "type": "str"},
                "state" : {"required": False, "type": "str"},
                "aggregate_type" : {"required": False, "type": "str"},
                "snapshot_size_total" : {"required": False, "type": "str"},
                "snapshot_size_used" : {"required": False, "type": "str"},
                "snapshot_size_avail" : {"required": False, "type": "str"},
                "hybrid_cache_size_total" : {"required": False, "type": "str"},
                "size_total" : {"required": False, "type": "str"},
                "size_used" : {"required": False, "type": "str"},
                "size_used_percent" : {"required": False, "type": "str"},
                "size_avail" : {"required": False, "type": "str"},
                "size_avail_percent" : {"required": False, "type": "str"},
                "total_committed" : {"required": False, "type": "str"},
                "total_reserved_space" : {"required": False, "type": "str"},
                "raid_status" : {"required": False, "type": "str"},
                "raid_type" : {"required": False, "type": "str"},
                "mirror_status" : {"required": False, "type": "str"},
                "block_type" : {"required": False, "type": "str"},
                "volume_dedupe_space_savings" : {"required": False, "type": "str"},
                "volume_compression_space_savings" : {"required": False, "type": "str"},
                "raid_size" : {"required": False, "type": "str"},
                "has_local_root" : {"required": False, "type": "str"},
                "has_partner_root" : {"required": False, "type": "str"},
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
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global node_key
        node_key = module.params["node_key"]
        global is_hybrid
        is_hybrid = module.params["is_hybrid"]
        global is_hybrid_enabled
        is_hybrid_enabled = module.params["is_hybrid_enabled"]
        global is_snaplock
        is_snaplock = module.params["is_snaplock"]
        global snaplock_type
        snaplock_type = module.params["snaplock_type"]
        global uses_shared_disks
        uses_shared_disks = module.params["uses_shared_disks"]
        global state
        state = module.params["state"]
        global aggregate_type
        aggregate_type = module.params["aggregate_type"]
        global snapshot_size_total
        snapshot_size_total = module.params["snapshot_size_total"]
        global snapshot_size_used
        snapshot_size_used = module.params["snapshot_size_used"]
        global snapshot_size_avail
        snapshot_size_avail = module.params["snapshot_size_avail"]
        global hybrid_cache_size_total
        hybrid_cache_size_total = module.params["hybrid_cache_size_total"]
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
        global total_committed
        total_committed = module.params["total_committed"]
        global total_reserved_space
        total_reserved_space = module.params["total_reserved_space"]
        global raid_status
        raid_status = module.params["raid_status"]
        global raid_type
        raid_type = module.params["raid_type"]
        global mirror_status
        mirror_status = module.params["mirror_status"]
        global block_type
        block_type = module.params["block_type"]
        global volume_dedupe_space_savings
        volume_dedupe_space_savings = module.params["volume_dedupe_space_savings"]
        global volume_compression_space_savings
        volume_compression_space_savings = module.params["volume_compression_space_savings"]
        global raid_size
        raid_size = module.params["raid_size"]
        global has_local_root
        has_local_root = module.params["has_local_root"]
        global has_partner_root
        has_partner_root = module.params["has_partner_root"]
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
