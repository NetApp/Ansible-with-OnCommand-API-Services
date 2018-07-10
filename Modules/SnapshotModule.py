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

    url_path+="snapshots"

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
    if snapmirror_label != None:
        if flag is 0:
            url_path+="?snapmirror_label="+snapmirror_label
            flag=1
        else:
            url_path+="&snapmirror_label="+snapmirror_label
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if volume_key != None:
        if flag is 0:
            url_path+="?volume_key="+volume_key
            flag=1
        else:
            url_path+="&volume_key="+volume_key
    if is_busy != None:
        if flag is 0:
            url_path+="?is_busy="+is_busy
            flag=1
        else:
            url_path+="&is_busy="+is_busy
    if access_timestamp != None:
        if flag is 0:
            url_path+="?access_timestamp="+access_timestamp
            flag=1
        else:
            url_path+="&access_timestamp="+access_timestamp
    if dependency != None:
        if flag is 0:
            url_path+="?dependency="+dependency
            flag=1
        else:
            url_path+="&dependency="+dependency
    if percentage_total_blocks != None:
        if flag is 0:
            url_path+="?percentage_total_blocks="+percentage_total_blocks
            flag=1
        else:
            url_path+="&percentage_total_blocks="+percentage_total_blocks
    if cumulative_percentage_total_blocks != None:
        if flag is 0:
            url_path+="?cumulative_percentage_total_blocks="+cumulative_percentage_total_blocks
            flag=1
        else:
            url_path+="&cumulative_percentage_total_blocks="+cumulative_percentage_total_blocks
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
    url_path+="snapshots"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (snapmirror_label != None) & (snapmirror_label != key):
        payload['snapmirror_label']=snapmirror_label
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (volume_key != None) & (volume_key != key):
        payload['volume_key']=volume_key
    if (is_busy != None) & (is_busy != key):
        payload['is_busy']=is_busy
    if (access_timestamp != None) & (access_timestamp != key):
        payload['access_timestamp']=access_timestamp
    if (dependency != None) & (dependency != key):
        payload['dependency']=dependency
    if (percentage_total_blocks != None) & (percentage_total_blocks != key):
        payload['percentage_total_blocks']=percentage_total_blocks
    if (cumulative_percentage_total_blocks != None) & (cumulative_percentage_total_blocks != key):
        payload['cumulative_percentage_total_blocks']=cumulative_percentage_total_blocks
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
    url_path+="snapshots/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (snapmirror_label != None) & (snapmirror_label != key):
        payload['snapmirror_label']=snapmirror_label
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (volume_key != None) & (volume_key != key):
        payload['volume_key']=volume_key
    if (is_busy != None) & (is_busy != key):
        payload['is_busy']=is_busy
    if (access_timestamp != None) & (access_timestamp != key):
        payload['access_timestamp']=access_timestamp
    if (dependency != None) & (dependency != key):
        payload['dependency']=dependency
    if (percentage_total_blocks != None) & (percentage_total_blocks != key):
        payload['percentage_total_blocks']=percentage_total_blocks
    if (cumulative_percentage_total_blocks != None) & (cumulative_percentage_total_blocks != key):
        payload['cumulative_percentage_total_blocks']=cumulative_percentage_total_blocks
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
    url_path+="snapshots/"

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
                "snapmirror_label" : {"required": False, "type": "str"},
                "storage_vm_key" : {"required": False, "type": "str"},
                "volume_key" : {"required": False, "type": "str"},
                "is_busy" : {"required": False, "type": "str"},
                "access_timestamp" : {"required": False, "type": "str"},
                "dependency" : {"required": False, "type": "str"},
                "percentage_total_blocks" : {"required": False, "type": "str"},
                "cumulative_percentage_total_blocks" : {"required": False, "type": "str"},
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
        global snapmirror_label
        snapmirror_label = module.params["snapmirror_label"]
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global volume_key
        volume_key = module.params["volume_key"]
        global is_busy
        is_busy = module.params["is_busy"]
        global access_timestamp
        access_timestamp = module.params["access_timestamp"]
        global dependency
        dependency = module.params["dependency"]
        global percentage_total_blocks
        percentage_total_blocks = module.params["percentage_total_blocks"]
        global cumulative_percentage_total_blocks
        cumulative_percentage_total_blocks = module.params["cumulative_percentage_total_blocks"]
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
