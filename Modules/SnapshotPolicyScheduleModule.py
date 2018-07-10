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

    url_path+="snapshot-policy-schedules"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if snapshot_policy_key != None:
        if flag is 0:
            url_path+="?snapshot_policy_key="+snapshot_policy_key
            flag=1
        else:
            url_path+="&snapshot_policy_key="+snapshot_policy_key
    if job_schedule_key != None:
        if flag is 0:
            url_path+="?job_schedule_key="+job_schedule_key
            flag=1
        else:
            url_path+="&job_schedule_key="+job_schedule_key
    if prefix != None:
        if flag is 0:
            url_path+="?prefix="+prefix
            flag=1
        else:
            url_path+="&prefix="+prefix
    if snap_mirror_label != None:
        if flag is 0:
            url_path+="?snap_mirror_label="+snap_mirror_label
            flag=1
        else:
            url_path+="&snap_mirror_label="+snap_mirror_label
    if count != None:
        if flag is 0:
            url_path+="?count="+count
            flag=1
        else:
            url_path+="&count="+count
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
    url_path+="snapshot-policy-schedules"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
    if (job_schedule_key != None) & (job_schedule_key != key):
        payload['job_schedule_key']=job_schedule_key
    if (prefix != None) & (prefix != key):
        payload['prefix']=prefix
    if (snap_mirror_label != None) & (snap_mirror_label != key):
        payload['snap_mirror_label']=snap_mirror_label
    if (count != None) & (count != key):
        payload['count']=count
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
    url_path+="snapshot-policy-schedules/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
    if (job_schedule_key != None) & (job_schedule_key != key):
        payload['job_schedule_key']=job_schedule_key
    if (prefix != None) & (prefix != key):
        payload['prefix']=prefix
    if (snap_mirror_label != None) & (snap_mirror_label != key):
        payload['snap_mirror_label']=snap_mirror_label
    if (count != None) & (count != key):
        payload['count']=count
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
    url_path+="snapshot-policy-schedules/"

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
                "snapshot_policy_key" : {"required": False, "type": "str"},
                "job_schedule_key" : {"required": False, "type": "str"},
                "prefix" : {"required": False, "type": "str"},
                "snap_mirror_label" : {"required": False, "type": "str"},
                "count" : {"required": False, "type": "str"},
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
        global snapshot_policy_key
        snapshot_policy_key = module.params["snapshot_policy_key"]
        global job_schedule_key
        job_schedule_key = module.params["job_schedule_key"]
        global prefix
        prefix = module.params["prefix"]
        global snap_mirror_label
        snap_mirror_label = module.params["snap_mirror_label"]
        global count
        count = module.params["count"]
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
