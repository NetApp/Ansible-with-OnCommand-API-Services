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

    url_path+="snap-mirror-policies"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if name != None:
        if flag is 0:
            url_path+="?name="+name
            flag=1
        else:
            url_path+="&name="+name
    if comment != None:
        if flag is 0:
            url_path+="?comment="+comment
            flag=1
        else:
            url_path+="&comment="+comment
    if create_snapshot != None:
        if flag is 0:
            url_path+="?create_snapshot="+create_snapshot
            flag=1
        else:
            url_path+="&create_snapshot="+create_snapshot
    if ignore_access_time != None:
        if flag is 0:
            url_path+="?ignore_access_time="+ignore_access_time
            flag=1
        else:
            url_path+="&ignore_access_time="+ignore_access_time
    if is_network_compression_enabled != None:
        if flag is 0:
            url_path+="?is_network_compression_enabled="+is_network_compression_enabled
            flag=1
        else:
            url_path+="&is_network_compression_enabled="+is_network_compression_enabled
    if restart != None:
        if flag is 0:
            url_path+="?restart="+restart
            flag=1
        else:
            url_path+="&restart="+restart
    if total_keep != None:
        if flag is 0:
            url_path+="?total_keep="+total_keep
            flag=1
        else:
            url_path+="&total_keep="+total_keep
    if transfer_priority != None:
        if flag is 0:
            url_path+="?transfer_priority="+transfer_priority
            flag=1
        else:
            url_path+="&transfer_priority="+transfer_priority
    if tries != None:
        if flag is 0:
            url_path+="?tries="+tries
            flag=1
        else:
            url_path+="&tries="+tries
    if type != None:
        if flag is 0:
            url_path+="?type="+type
            flag=1
        else:
            url_path+="&type="+type
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
    url_path+="snap-mirror-policies"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (name != None) & (name != key):
        payload['name']=name
    if (comment != None) & (comment != key):
        payload['comment']=comment
    if (create_snapshot != None) & (create_snapshot != key):
        payload['create_snapshot']=create_snapshot
    if (ignore_access_time != None) & (ignore_access_time != key):
        payload['ignore_access_time']=ignore_access_time
    if (is_network_compression_enabled != None) & (is_network_compression_enabled != key):
        payload['is_network_compression_enabled']=is_network_compression_enabled
    if (restart != None) & (restart != key):
        payload['restart']=restart
    if (total_keep != None) & (total_keep != key):
        payload['total_keep']=total_keep
    if (transfer_priority != None) & (transfer_priority != key):
        payload['transfer_priority']=transfer_priority
    if (tries != None) & (tries != key):
        payload['tries']=tries
    if (type != None) & (type != key):
        payload['type']=type
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
    url_path+="snap-mirror-policies/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (name != None) & (name != key):
        payload['name']=name
    if (comment != None) & (comment != key):
        payload['comment']=comment
    if (create_snapshot != None) & (create_snapshot != key):
        payload['create_snapshot']=create_snapshot
    if (ignore_access_time != None) & (ignore_access_time != key):
        payload['ignore_access_time']=ignore_access_time
    if (is_network_compression_enabled != None) & (is_network_compression_enabled != key):
        payload['is_network_compression_enabled']=is_network_compression_enabled
    if (restart != None) & (restart != key):
        payload['restart']=restart
    if (total_keep != None) & (total_keep != key):
        payload['total_keep']=total_keep
    if (transfer_priority != None) & (transfer_priority != key):
        payload['transfer_priority']=transfer_priority
    if (tries != None) & (tries != key):
        payload['tries']=tries
    if (type != None) & (type != key):
        payload['type']=type
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
    url_path+="snap-mirror-policies/"

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
                "storage_vm_key" : {"required": False, "type": "str"},
                "name" : {"required": False, "type": "str"},
                "comment" : {"required": False, "type": "str"},
                "create_snapshot" : {"required": False, "type": "str"},
                "ignore_access_time" : {"required": False, "type": "str"},
                "is_network_compression_enabled" : {"required": False, "type": "str"},
                "restart" : {"required": False, "type": "str"},
                "total_keep" : {"required": False, "type": "str"},
                "transfer_priority" : {"required": False, "type": "str"},
                "tries" : {"required": False, "type": "str"},
                "type" : {"required": False, "type": "str"},
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
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global name
        name = module.params["name"]
        global comment
        comment = module.params["comment"]
        global create_snapshot
        create_snapshot = module.params["create_snapshot"]
        global ignore_access_time
        ignore_access_time = module.params["ignore_access_time"]
        global is_network_compression_enabled
        is_network_compression_enabled = module.params["is_network_compression_enabled"]
        global restart
        restart = module.params["restart"]
        global total_keep
        total_keep = module.params["total_keep"]
        global transfer_priority
        transfer_priority = module.params["transfer_priority"]
        global tries
        tries = module.params["tries"]
        global type
        type = module.params["type"]
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
