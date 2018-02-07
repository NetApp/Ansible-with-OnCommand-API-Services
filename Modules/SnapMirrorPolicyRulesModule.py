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
    url_path        = "/api/2.0/ontap/"

    flag=0

    url_path+="snap-mirror-policy-rules"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if snap_mirror_policy_key != None:
        if flag is 0:
            url_path+="?snap_mirror_policy_key="+snap_mirror_policy_key
            flag=1
        else:
            url_path+="&snap_mirror_policy_key="+snap_mirror_policy_key
    if keep != None:
        if flag is 0:
            url_path+="?keep="+keep
            flag=1
        else:
            url_path+="&keep="+keep
    if preserve != None:
        if flag is 0:
            url_path+="?preserve="+preserve
            flag=1
        else:
            url_path+="&preserve="+preserve
    if snap_mirror_label != None:
        if flag is 0:
            url_path+="?snap_mirror_label="+snap_mirror_label
            flag=1
        else:
            url_path+="&snap_mirror_label="+snap_mirror_label
    if warn != None:
        if flag is 0:
            url_path+="?warn="+warn
            flag=1
        else:
            url_path+="&warn="+warn
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
    url_path        = "/api/2.0/ontap/"
    url_path+="snap-mirror-policy-rules"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (snap_mirror_policy_key != None) & (snap_mirror_policy_key != key):
        payload['snap_mirror_policy_key']=snap_mirror_policy_key
    if (keep != None) & (keep != key):
        payload['keep']=keep
    if (preserve != None) & (preserve != key):
        payload['preserve']=preserve
    if (snap_mirror_label != None) & (snap_mirror_label != key):
        payload['snap_mirror_label']=snap_mirror_label
    if (warn != None) & (warn != key):
        payload['warn']=warn
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
    url_path        = "/api/2.0/ontap/"
    url_path+="snap-mirror-policy-rules/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (snap_mirror_policy_key != None) & (snap_mirror_policy_key != key):
        payload['snap_mirror_policy_key']=snap_mirror_policy_key
    if (keep != None) & (keep != key):
        payload['keep']=keep
    if (preserve != None) & (preserve != key):
        payload['preserve']=preserve
    if (snap_mirror_label != None) & (snap_mirror_label != key):
        payload['snap_mirror_label']=snap_mirror_label
    if (warn != None) & (warn != key):
        payload['warn']=warn
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
    url_path        = "/api/2.0/ontap/"
    url_path+="snap-mirror-policy-rules/"

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
                "key" : {"required": False, "type": "str"},
                "snap_mirror_policy_key" : {"required": False, "type": "str"},
                "keep" : {"required": False, "type": "str"},
                "preserve" : {"required": False, "type": "str"},
                "snap_mirror_label" : {"required": False, "type": "str"},
                "warn" : {"required": False, "type": "str"},
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

        global lun_key
        global nfs_share_key
        global cifs_share_key
        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]

        # Properties details
        global key
        key = module.params["key"]
        global snap_mirror_policy_key
        snap_mirror_policy_key = module.params["snap_mirror_policy_key"]
        global keep
        keep = module.params["keep"]
        global preserve
        preserve = module.params["preserve"]
        global snap_mirror_label
        snap_mirror_label = module.params["snap_mirror_label"]
        global warn
        warn = module.params["warn"]
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