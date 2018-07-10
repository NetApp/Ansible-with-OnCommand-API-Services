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

    url_path+="luns"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if qtree_key != None:
        if flag is 0:
            url_path+="?qtree_key="+qtree_key
            flag=1
        else:
            url_path+="&qtree_key="+qtree_key
    if volume_key != None:
        if flag is 0:
            url_path+="?volume_key="+volume_key
            flag=1
        else:
            url_path+="&volume_key="+volume_key
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if qos_policy_group_key != None:
        if flag is 0:
            url_path+="?qos_policy_group_key="+qos_policy_group_key
            flag=1
        else:
            url_path+="&qos_policy_group_key="+qos_policy_group_key
    if path != None:
        if flag is 0:
            url_path+="?path="+path
            flag=1
        else:
            url_path+="&path="+path
    if is_online != None:
        if flag is 0:
            url_path+="?is_online="+is_online
            flag=1
        else:
            url_path+="&is_online="+is_online
    if size != None:
        if flag is 0:
            url_path+="?size="+size
            flag=1
        else:
            url_path+="&size="+size
    if size_used != None:
        if flag is 0:
            url_path+="?size_used="+size_used
            flag=1
        else:
            url_path+="&size_used="+size_used
    if is_space_reservation_enabled != None:
        if flag is 0:
            url_path+="?is_space_reservation_enabled="+is_space_reservation_enabled
            flag=1
        else:
            url_path+="&is_space_reservation_enabled="+is_space_reservation_enabled
    if is_space_alloc_enabled != None:
        if flag is 0:
            url_path+="?is_space_alloc_enabled="+is_space_alloc_enabled
            flag=1
        else:
            url_path+="&is_space_alloc_enabled="+is_space_alloc_enabled
    if is_mapped != None:
        if flag is 0:
            url_path+="?is_mapped="+is_mapped
            flag=1
        else:
            url_path+="&is_mapped="+is_mapped
    if serial_number != None:
        if flag is 0:
            url_path+="?serial_number="+serial_number
            flag=1
        else:
            url_path+="&serial_number="+serial_number
    if multi_protocol_type != None:
        if flag is 0:
            url_path+="?multi_protocol_type="+multi_protocol_type
            flag=1
        else:
            url_path+="&multi_protocol_type="+multi_protocol_type
    if alignment != None:
        if flag is 0:
            url_path+="?alignment="+alignment
            flag=1
        else:
            url_path+="&alignment="+alignment
    if prefix_size != None:
        if flag is 0:
            url_path+="?prefix_size="+prefix_size
            flag=1
        else:
            url_path+="&prefix_size="+prefix_size
    if suffix_size != None:
        if flag is 0:
            url_path+="?suffix_size="+suffix_size
            flag=1
        else:
            url_path+="&suffix_size="+suffix_size
    if lun_class != None:
        if flag is 0:
            url_path+="?lun_class="+lun_class
            flag=1
        else:
            url_path+="&lun_class="+lun_class
    if comment != None:
        if flag is 0:
            url_path+="?comment="+comment
            flag=1
        else:
            url_path+="&comment="+comment
    if name != None:
        if flag is 0:
            url_path+="?name="+name
            flag=1
        else:
            url_path+="&name="+name
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
    url_path+="luns"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (qtree_key != None) & (qtree_key != key):
        payload['qtree_key']=qtree_key
    if (volume_key != None) & (volume_key != key):
        payload['volume_key']=volume_key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (path != None) & (path != key):
        payload['path']=path
    if (is_online != None) & (is_online != key):
        payload['is_online']=is_online
    if (size != None) & (size != key):
        payload['size']=size
    if (size_used != None) & (size_used != key):
        payload['size_used']=size_used
    if (is_space_reservation_enabled != None) & (is_space_reservation_enabled != key):
        payload['is_space_reservation_enabled']=is_space_reservation_enabled
    if (is_space_alloc_enabled != None) & (is_space_alloc_enabled != key):
        payload['is_space_alloc_enabled']=is_space_alloc_enabled
    if (is_mapped != None) & (is_mapped != key):
        payload['is_mapped']=is_mapped
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (multi_protocol_type != None) & (multi_protocol_type != key):
        payload['multi_protocol_type']=multi_protocol_type
    if (alignment != None) & (alignment != key):
        payload['alignment']=alignment
    if (prefix_size != None) & (prefix_size != key):
        payload['prefix_size']=prefix_size
    if (suffix_size != None) & (suffix_size != key):
        payload['suffix_size']=suffix_size
    if (lun_class != None) & (lun_class != key):
        payload['lun_class']=lun_class
    if (comment != None) & (comment != key):
        payload['comment']=comment
    if (name != None) & (name != key):
        payload['name']=name
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
    url_path+="luns/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (qtree_key != None) & (qtree_key != key):
        payload['qtree_key']=qtree_key
    if (volume_key != None) & (volume_key != key):
        payload['volume_key']=volume_key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (path != None) & (path != key):
        payload['path']=path
    if (is_online != None) & (is_online != key):
        payload['is_online']=is_online
    if (size != None) & (size != key):
        payload['size']=size
    if (size_used != None) & (size_used != key):
        payload['size_used']=size_used
    if (is_space_reservation_enabled != None) & (is_space_reservation_enabled != key):
        payload['is_space_reservation_enabled']=is_space_reservation_enabled
    if (is_space_alloc_enabled != None) & (is_space_alloc_enabled != key):
        payload['is_space_alloc_enabled']=is_space_alloc_enabled
    if (is_mapped != None) & (is_mapped != key):
        payload['is_mapped']=is_mapped
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (multi_protocol_type != None) & (multi_protocol_type != key):
        payload['multi_protocol_type']=multi_protocol_type
    if (alignment != None) & (alignment != key):
        payload['alignment']=alignment
    if (prefix_size != None) & (prefix_size != key):
        payload['prefix_size']=prefix_size
    if (suffix_size != None) & (suffix_size != key):
        payload['suffix_size']=suffix_size
    if (lun_class != None) & (lun_class != key):
        payload['lun_class']=lun_class
    if (comment != None) & (comment != key):
        payload['comment']=comment
    if (name != None) & (name != key):
        payload['name']=name
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
    url_path+="luns/"

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
                "qtree_key" : {"required": False, "type": "str"},
                "volume_key" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "qos_policy_group_key" : {"required": False, "type": "str"},
                "path" : {"required": False, "type": "str"},
                "is_online" : {"required": False, "type": "str"},
                "size" : {"required": False, "type": "str"},
                "size_used" : {"required": False, "type": "str"},
                "is_space_reservation_enabled" : {"required": False, "type": "str"},
                "is_space_alloc_enabled" : {"required": False, "type": "str"},
                "is_mapped" : {"required": False, "type": "str"},
                "serial_number" : {"required": False, "type": "str"},
                "multi_protocol_type" : {"required": False, "type": "str"},
                "alignment" : {"required": False, "type": "str"},
                "prefix_size" : {"required": False, "type": "str"},
                "suffix_size" : {"required": False, "type": "str"},
                "lun_class" : {"required": False, "type": "str"},
                "comment" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
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
        global qtree_key
        qtree_key = module.params["qtree_key"]
        global volume_key
        volume_key = module.params["volume_key"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global qos_policy_group_key
        qos_policy_group_key = module.params["qos_policy_group_key"]
        global path
        path = module.params["path"]
        global is_online
        is_online = module.params["is_online"]
        global size
        size = module.params["size"]
        global size_used
        size_used = module.params["size_used"]
        global is_space_reservation_enabled
        is_space_reservation_enabled = module.params["is_space_reservation_enabled"]
        global is_space_alloc_enabled
        is_space_alloc_enabled = module.params["is_space_alloc_enabled"]
        global is_mapped
        is_mapped = module.params["is_mapped"]
        global serial_number
        serial_number = module.params["serial_number"]
        global multi_protocol_type
        multi_protocol_type = module.params["multi_protocol_type"]
        global alignment
        alignment = module.params["alignment"]
        global prefix_size
        prefix_size = module.params["prefix_size"]
        global suffix_size
        suffix_size = module.params["suffix_size"]
        global lun_class
        lun_class = module.params["lun_class"]
        global comment
        comment = module.params["comment"]
        global name
        name = module.params["name"]
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
