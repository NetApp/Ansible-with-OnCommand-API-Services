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

    url_path+="snap-mirrors"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_vm_snap_mirror_key != None:
        if flag is 0:
            url_path+="?storage_vm_snap_mirror_key="+storage_vm_snap_mirror_key
            flag=1
        else:
            url_path+="&storage_vm_snap_mirror_key="+storage_vm_snap_mirror_key
    if destination_volume_key != None:
        if flag is 0:
            url_path+="?destination_volume_key="+destination_volume_key
            flag=1
        else:
            url_path+="&destination_volume_key="+destination_volume_key
    if destination_storage_vm_key != None:
        if flag is 0:
            url_path+="?destination_storage_vm_key="+destination_storage_vm_key
            flag=1
        else:
            url_path+="&destination_storage_vm_key="+destination_storage_vm_key
    if destination_location != None:
        if flag is 0:
            url_path+="?destination_location="+destination_location
            flag=1
        else:
            url_path+="&destination_location="+destination_location
    if source_volume_key != None:
        if flag is 0:
            url_path+="?source_volume_key="+source_volume_key
            flag=1
        else:
            url_path+="&source_volume_key="+source_volume_key
    if source_storage_vm_key != None:
        if flag is 0:
            url_path+="?source_storage_vm_key="+source_storage_vm_key
            flag=1
        else:
            url_path+="&source_storage_vm_key="+source_storage_vm_key
    if source_location != None:
        if flag is 0:
            url_path+="?source_location="+source_location
            flag=1
        else:
            url_path+="&source_location="+source_location
    if mirror_state != None:
        if flag is 0:
            url_path+="?mirror_state="+mirror_state
            flag=1
        else:
            url_path+="&mirror_state="+mirror_state
    if network_compression_ratio != None:
        if flag is 0:
            url_path+="?network_compression_ratio="+network_compression_ratio
            flag=1
        else:
            url_path+="&network_compression_ratio="+network_compression_ratio
    if snap_mirror_policy_key != None:
        if flag is 0:
            url_path+="?snap_mirror_policy_key="+snap_mirror_policy_key
            flag=1
        else:
            url_path+="&snap_mirror_policy_key="+snap_mirror_policy_key
    if is_healthy != None:
        if flag is 0:
            url_path+="?is_healthy="+is_healthy
            flag=1
        else:
            url_path+="&is_healthy="+is_healthy
    if max_transfer_rate != None:
        if flag is 0:
            url_path+="?max_transfer_rate="+max_transfer_rate
            flag=1
        else:
            url_path+="&max_transfer_rate="+max_transfer_rate
    if relationship_type != None:
        if flag is 0:
            url_path+="?relationship_type="+relationship_type
            flag=1
        else:
            url_path+="&relationship_type="+relationship_type
    if tries != None:
        if flag is 0:
            url_path+="?tries="+tries
            flag=1
        else:
            url_path+="&tries="+tries
    if unhealthy_reason != None:
        if flag is 0:
            url_path+="?unhealthy_reason="+unhealthy_reason
            flag=1
        else:
            url_path+="&unhealthy_reason="+unhealthy_reason
    if lag_time != None:
        if flag is 0:
            url_path+="?lag_time="+lag_time
            flag=1
        else:
            url_path+="&lag_time="+lag_time
    if last_transfer_duration != None:
        if flag is 0:
            url_path+="?last_transfer_duration="+last_transfer_duration
            flag=1
        else:
            url_path+="&last_transfer_duration="+last_transfer_duration
    if last_transfer_end_timestamp != None:
        if flag is 0:
            url_path+="?last_transfer_end_timestamp="+last_transfer_end_timestamp
            flag=1
        else:
            url_path+="&last_transfer_end_timestamp="+last_transfer_end_timestamp
    if last_transfer_error != None:
        if flag is 0:
            url_path+="?last_transfer_error="+last_transfer_error
            flag=1
        else:
            url_path+="&last_transfer_error="+last_transfer_error
    if last_transfer_error_codes != None:
        if flag is 0:
            url_path+="?last_transfer_error_codes="+last_transfer_error_codes
            flag=1
        else:
            url_path+="&last_transfer_error_codes="+last_transfer_error_codes
    if last_transfer_network_compression_ratio != None:
        if flag is 0:
            url_path+="?last_transfer_network_compression_ratio="+last_transfer_network_compression_ratio
            flag=1
        else:
            url_path+="&last_transfer_network_compression_ratio="+last_transfer_network_compression_ratio
    if last_transfer_type != None:
        if flag is 0:
            url_path+="?last_transfer_type="+last_transfer_type
            flag=1
        else:
            url_path+="&last_transfer_type="+last_transfer_type
    if last_transfer_size != None:
        if flag is 0:
            url_path+="?last_transfer_size="+last_transfer_size
            flag=1
        else:
            url_path+="&last_transfer_size="+last_transfer_size
    if relationship_control_plane != None:
        if flag is 0:
            url_path+="?relationship_control_plane="+relationship_control_plane
            flag=1
        else:
            url_path+="&relationship_control_plane="+relationship_control_plane
    if relationship_identifier != None:
        if flag is 0:
            url_path+="?relationship_identifier="+relationship_identifier
            flag=1
        else:
            url_path+="&relationship_identifier="+relationship_identifier
    if job_schedule_key != None:
        if flag is 0:
            url_path+="?job_schedule_key="+job_schedule_key
            flag=1
        else:
            url_path+="&job_schedule_key="+job_schedule_key
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
    url_path+="snap-mirrors"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_snap_mirror_key != None) & (storage_vm_snap_mirror_key != key):
        payload['storage_vm_snap_mirror_key']=storage_vm_snap_mirror_key
    if (destination_volume_key != None) & (destination_volume_key != key):
        payload['destination_volume_key']=destination_volume_key
    if (destination_storage_vm_key != None) & (destination_storage_vm_key != key):
        payload['destination_storage_vm_key']=destination_storage_vm_key
    if (destination_location != None) & (destination_location != key):
        payload['destination_location']=destination_location
    if (source_volume_key != None) & (source_volume_key != key):
        payload['source_volume_key']=source_volume_key
    if (source_storage_vm_key != None) & (source_storage_vm_key != key):
        payload['source_storage_vm_key']=source_storage_vm_key
    if (source_location != None) & (source_location != key):
        payload['source_location']=source_location
    if (mirror_state != None) & (mirror_state != key):
        payload['mirror_state']=mirror_state
    if (network_compression_ratio != None) & (network_compression_ratio != key):
        payload['network_compression_ratio']=network_compression_ratio
    if (snap_mirror_policy_key != None) & (snap_mirror_policy_key != key):
        payload['snap_mirror_policy_key']=snap_mirror_policy_key
    if (is_healthy != None) & (is_healthy != key):
        payload['is_healthy']=is_healthy
    if (max_transfer_rate != None) & (max_transfer_rate != key):
        payload['max_transfer_rate']=max_transfer_rate
    if (relationship_type != None) & (relationship_type != key):
        payload['relationship_type']=relationship_type
    if (tries != None) & (tries != key):
        payload['tries']=tries
    if (unhealthy_reason != None) & (unhealthy_reason != key):
        payload['unhealthy_reason']=unhealthy_reason
    if (lag_time != None) & (lag_time != key):
        payload['lag_time']=lag_time
    if (last_transfer_duration != None) & (last_transfer_duration != key):
        payload['last_transfer_duration']=last_transfer_duration
    if (last_transfer_end_timestamp != None) & (last_transfer_end_timestamp != key):
        payload['last_transfer_end_timestamp']=last_transfer_end_timestamp
    if (last_transfer_error != None) & (last_transfer_error != key):
        payload['last_transfer_error']=last_transfer_error
    if (last_transfer_error_codes != None) & (last_transfer_error_codes != key):
        payload['last_transfer_error_codes']=last_transfer_error_codes
    if (last_transfer_network_compression_ratio != None) & (last_transfer_network_compression_ratio != key):
        payload['last_transfer_network_compression_ratio']=last_transfer_network_compression_ratio
    if (last_transfer_type != None) & (last_transfer_type != key):
        payload['last_transfer_type']=last_transfer_type
    if (last_transfer_size != None) & (last_transfer_size != key):
        payload['last_transfer_size']=last_transfer_size
    if (relationship_control_plane != None) & (relationship_control_plane != key):
        payload['relationship_control_plane']=relationship_control_plane
    if (relationship_identifier != None) & (relationship_identifier != key):
        payload['relationship_identifier']=relationship_identifier
    if (job_schedule_key != None) & (job_schedule_key != key):
        payload['job_schedule_key']=job_schedule_key
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
    url_path+="snap-mirrors/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_snap_mirror_key != None) & (storage_vm_snap_mirror_key != key):
        payload['storage_vm_snap_mirror_key']=storage_vm_snap_mirror_key
    if (destination_volume_key != None) & (destination_volume_key != key):
        payload['destination_volume_key']=destination_volume_key
    if (destination_storage_vm_key != None) & (destination_storage_vm_key != key):
        payload['destination_storage_vm_key']=destination_storage_vm_key
    if (destination_location != None) & (destination_location != key):
        payload['destination_location']=destination_location
    if (source_volume_key != None) & (source_volume_key != key):
        payload['source_volume_key']=source_volume_key
    if (source_storage_vm_key != None) & (source_storage_vm_key != key):
        payload['source_storage_vm_key']=source_storage_vm_key
    if (source_location != None) & (source_location != key):
        payload['source_location']=source_location
    if (mirror_state != None) & (mirror_state != key):
        payload['mirror_state']=mirror_state
    if (network_compression_ratio != None) & (network_compression_ratio != key):
        payload['network_compression_ratio']=network_compression_ratio
    if (snap_mirror_policy_key != None) & (snap_mirror_policy_key != key):
        payload['snap_mirror_policy_key']=snap_mirror_policy_key
    if (is_healthy != None) & (is_healthy != key):
        payload['is_healthy']=is_healthy
    if (max_transfer_rate != None) & (max_transfer_rate != key):
        payload['max_transfer_rate']=max_transfer_rate
    if (relationship_type != None) & (relationship_type != key):
        payload['relationship_type']=relationship_type
    if (tries != None) & (tries != key):
        payload['tries']=tries
    if (unhealthy_reason != None) & (unhealthy_reason != key):
        payload['unhealthy_reason']=unhealthy_reason
    if (lag_time != None) & (lag_time != key):
        payload['lag_time']=lag_time
    if (last_transfer_duration != None) & (last_transfer_duration != key):
        payload['last_transfer_duration']=last_transfer_duration
    if (last_transfer_end_timestamp != None) & (last_transfer_end_timestamp != key):
        payload['last_transfer_end_timestamp']=last_transfer_end_timestamp
    if (last_transfer_error != None) & (last_transfer_error != key):
        payload['last_transfer_error']=last_transfer_error
    if (last_transfer_error_codes != None) & (last_transfer_error_codes != key):
        payload['last_transfer_error_codes']=last_transfer_error_codes
    if (last_transfer_network_compression_ratio != None) & (last_transfer_network_compression_ratio != key):
        payload['last_transfer_network_compression_ratio']=last_transfer_network_compression_ratio
    if (last_transfer_type != None) & (last_transfer_type != key):
        payload['last_transfer_type']=last_transfer_type
    if (last_transfer_size != None) & (last_transfer_size != key):
        payload['last_transfer_size']=last_transfer_size
    if (relationship_control_plane != None) & (relationship_control_plane != key):
        payload['relationship_control_plane']=relationship_control_plane
    if (relationship_identifier != None) & (relationship_identifier != key):
        payload['relationship_identifier']=relationship_identifier
    if (job_schedule_key != None) & (job_schedule_key != key):
        payload['job_schedule_key']=job_schedule_key
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
    url_path+="snap-mirrors/"

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
                "storage_vm_snap_mirror_key" : {"required": False, "type": "str"},
                "destination_volume_key" : {"required": False, "type": "str"},
                "destination_storage_vm_key" : {"required": False, "type": "str"},
                "destination_location" : {"required": False, "type": "str"},
                "source_volume_key" : {"required": False, "type": "str"},
                "source_storage_vm_key" : {"required": False, "type": "str"},
                "source_location" : {"required": False, "type": "str"},
                "mirror_state" : {"required": False, "type": "str"},
                "network_compression_ratio" : {"required": False, "type": "str"},
                "snap_mirror_policy_key" : {"required": False, "type": "str"},
                "is_healthy" : {"required": False, "type": "str"},
                "max_transfer_rate" : {"required": False, "type": "str"},
                "relationship_type" : {"required": False, "type": "str"},
                "tries" : {"required": False, "type": "str"},
                "unhealthy_reason" : {"required": False, "type": "str"},
                "lag_time" : {"required": False, "type": "str"},
                "last_transfer_duration" : {"required": False, "type": "str"},
                "last_transfer_end_timestamp" : {"required": False, "type": "str"},
                "last_transfer_error" : {"required": False, "type": "str"},
                "last_transfer_error_codes" : {"required": False, "type": "str"},
                "last_transfer_network_compression_ratio" : {"required": False, "type": "str"},
                "last_transfer_type" : {"required": False, "type": "str"},
                "last_transfer_size" : {"required": False, "type": "str"},
                "relationship_control_plane" : {"required": False, "type": "str"},
                "relationship_identifier" : {"required": False, "type": "str"},
                "job_schedule_key" : {"required": False, "type": "str"},
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
        global storage_vm_snap_mirror_key
        storage_vm_snap_mirror_key = module.params["storage_vm_snap_mirror_key"]
        global destination_volume_key
        destination_volume_key = module.params["destination_volume_key"]
        global destination_storage_vm_key
        destination_storage_vm_key = module.params["destination_storage_vm_key"]
        global destination_location
        destination_location = module.params["destination_location"]
        global source_volume_key
        source_volume_key = module.params["source_volume_key"]
        global source_storage_vm_key
        source_storage_vm_key = module.params["source_storage_vm_key"]
        global source_location
        source_location = module.params["source_location"]
        global mirror_state
        mirror_state = module.params["mirror_state"]
        global network_compression_ratio
        network_compression_ratio = module.params["network_compression_ratio"]
        global snap_mirror_policy_key
        snap_mirror_policy_key = module.params["snap_mirror_policy_key"]
        global is_healthy
        is_healthy = module.params["is_healthy"]
        global max_transfer_rate
        max_transfer_rate = module.params["max_transfer_rate"]
        global relationship_type
        relationship_type = module.params["relationship_type"]
        global tries
        tries = module.params["tries"]
        global unhealthy_reason
        unhealthy_reason = module.params["unhealthy_reason"]
        global lag_time
        lag_time = module.params["lag_time"]
        global last_transfer_duration
        last_transfer_duration = module.params["last_transfer_duration"]
        global last_transfer_end_timestamp
        last_transfer_end_timestamp = module.params["last_transfer_end_timestamp"]
        global last_transfer_error
        last_transfer_error = module.params["last_transfer_error"]
        global last_transfer_error_codes
        last_transfer_error_codes = module.params["last_transfer_error_codes"]
        global last_transfer_network_compression_ratio
        last_transfer_network_compression_ratio = module.params["last_transfer_network_compression_ratio"]
        global last_transfer_type
        last_transfer_type = module.params["last_transfer_type"]
        global last_transfer_size
        last_transfer_size = module.params["last_transfer_size"]
        global relationship_control_plane
        relationship_control_plane = module.params["relationship_control_plane"]
        global relationship_identifier
        relationship_identifier = module.params["relationship_identifier"]
        global job_schedule_key
        job_schedule_key = module.params["job_schedule_key"]
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
