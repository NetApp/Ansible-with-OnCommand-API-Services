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

    url_path+="export-rules"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if export_policy_key != None:
        if flag is 0:
            url_path+="?export_policy_key="+export_policy_key
            flag=1
        else:
            url_path+="&export_policy_key="+export_policy_key
    if rule_index != None:
        if flag is 0:
            url_path+="?rule_index="+rule_index
            flag=1
        else:
            url_path+="&rule_index="+rule_index
    if client_match != None:
        if flag is 0:
            url_path+="?client_match="+client_match
            flag=1
        else:
            url_path+="&client_match="+client_match
    if access_protocol != None:
        if flag is 0:
            url_path+="?access_protocol="+access_protocol
            flag=1
        else:
            url_path+="&access_protocol="+access_protocol
    if ro_rule != None:
        if flag is 0:
            url_path+="?ro_rule="+ro_rule
            flag=1
        else:
            url_path+="&ro_rule="+ro_rule
    if rw_rule != None:
        if flag is 0:
            url_path+="?rw_rule="+rw_rule
            flag=1
        else:
            url_path+="&rw_rule="+rw_rule
    if super_user_security != None:
        if flag is 0:
            url_path+="?super_user_security="+super_user_security
            flag=1
        else:
            url_path+="&super_user_security="+super_user_security
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
    url_path+="export-rules"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (export_policy_key != None) & (export_policy_key != key):
        payload['export_policy_key']=export_policy_key
    if (rule_index != None) & (rule_index != key):
        payload['rule_index']=rule_index
    if (client_match != None) & (client_match != key):
        payload['client_match']=client_match
    if (access_protocol != None) & (access_protocol != key):
        payload['access_protocol']=access_protocol
    if (ro_rule != None) & (ro_rule != key):
        payload['ro_rule']=ro_rule
    if (rw_rule != None) & (rw_rule != key):
        payload['rw_rule']=rw_rule
    if (super_user_security != None) & (super_user_security != key):
        payload['super_user_security']=super_user_security
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
    url_path+="export-rules/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (export_policy_key != None) & (export_policy_key != key):
        payload['export_policy_key']=export_policy_key
    if (rule_index != None) & (rule_index != key):
        payload['rule_index']=rule_index
    if (client_match != None) & (client_match != key):
        payload['client_match']=client_match
    if (access_protocol != None) & (access_protocol != key):
        payload['access_protocol']=access_protocol
    if (ro_rule != None) & (ro_rule != key):
        payload['ro_rule']=ro_rule
    if (rw_rule != None) & (rw_rule != key):
        payload['rw_rule']=rw_rule
    if (super_user_security != None) & (super_user_security != key):
        payload['super_user_security']=super_user_security
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
    url_path+="export-rules/"

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
                "export_policy_key" : {"required": False, "type": "str"},
                "rule_index" : {"required": False, "type": "str"},
                "client_match" : {"required": False, "type": "str"},
                "access_protocol" : {"required": False, "type": "str"},
                "ro_rule" : {"required": False, "type": "str"},
                "rw_rule" : {"required": False, "type": "str"},
                "super_user_security" : {"required": False, "type": "str"},
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
        global export_policy_key
        export_policy_key = module.params["export_policy_key"]
        global rule_index
        rule_index = module.params["rule_index"]
        global client_match
        client_match = module.params["client_match"]
        global access_protocol
        access_protocol = module.params["access_protocol"]
        global ro_rule
        ro_rule = module.params["ro_rule"]
        global rw_rule
        rw_rule = module.params["rw_rule"]
        global super_user_security
        super_user_security = module.params["super_user_security"]
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
