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

    url_path+="fc-ports"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if node_key != None:
        if flag is 0:
            url_path+="?node_key="+node_key
            flag=1
        else:
            url_path+="&node_key="+node_key
    if wwnn != None:
        if flag is 0:
            url_path+="?wwnn="+wwnn
            flag=1
        else:
            url_path+="&wwnn="+wwnn
    if wwpn != None:
        if flag is 0:
            url_path+="?wwpn="+wwpn
            flag=1
        else:
            url_path+="&wwpn="+wwpn
    if adapter != None:
        if flag is 0:
            url_path+="?adapter="+adapter
            flag=1
        else:
            url_path+="&adapter="+adapter
    if fabric_established != None:
        if flag is 0:
            url_path+="?fabric_established="+fabric_established
            flag=1
        else:
            url_path+="&fabric_established="+fabric_established
    if firmware_rev != None:
        if flag is 0:
            url_path+="?firmware_rev="+firmware_rev
            flag=1
        else:
            url_path+="&firmware_rev="+firmware_rev
    if info_name != None:
        if flag is 0:
            url_path+="?info_name="+info_name
            flag=1
        else:
            url_path+="&info_name="+info_name
    if max_speed != None:
        if flag is 0:
            url_path+="?max_speed="+max_speed
            flag=1
        else:
            url_path+="&max_speed="+max_speed
    if speed != None:
        if flag is 0:
            url_path+="?speed="+speed
            flag=1
        else:
            url_path+="&speed="+speed
    if physical_protocol != None:
        if flag is 0:
            url_path+="?physical_protocol="+physical_protocol
            flag=1
        else:
            url_path+="&physical_protocol="+physical_protocol
    if state != None:
        if flag is 0:
            url_path+="?state="+state
            flag=1
        else:
            url_path+="&state="+state
    if status != None:
        if flag is 0:
            url_path+="?status="+status
            flag=1
        else:
            url_path+="&status="+status
    if switch_port != None:
        if flag is 0:
            url_path+="?switch_port="+switch_port
            flag=1
        else:
            url_path+="&switch_port="+switch_port
    if data_link_rate != None:
        if flag is 0:
            url_path+="?data_link_rate="+data_link_rate
            flag=1
        else:
            url_path+="&data_link_rate="+data_link_rate
    if media_type != None:
        if flag is 0:
            url_path+="?media_type="+media_type
            flag=1
        else:
            url_path+="&media_type="+media_type
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
    url_path+="fc-ports"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (wwnn != None) & (wwnn != key):
        payload['wwnn']=wwnn
    if (wwpn != None) & (wwpn != key):
        payload['wwpn']=wwpn
    if (adapter != None) & (adapter != key):
        payload['adapter']=adapter
    if (fabric_established != None) & (fabric_established != key):
        payload['fabric_established']=fabric_established
    if (firmware_rev != None) & (firmware_rev != key):
        payload['firmware_rev']=firmware_rev
    if (info_name != None) & (info_name != key):
        payload['info_name']=info_name
    if (max_speed != None) & (max_speed != key):
        payload['max_speed']=max_speed
    if (speed != None) & (speed != key):
        payload['speed']=speed
    if (physical_protocol != None) & (physical_protocol != key):
        payload['physical_protocol']=physical_protocol
    if (state != None) & (state != key):
        payload['state']=state
    if (status != None) & (status != key):
        payload['status']=status
    if (switch_port != None) & (switch_port != key):
        payload['switch_port']=switch_port
    if (data_link_rate != None) & (data_link_rate != key):
        payload['data_link_rate']=data_link_rate
    if (media_type != None) & (media_type != key):
        payload['media_type']=media_type
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
    url_path+="fc-ports/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (wwnn != None) & (wwnn != key):
        payload['wwnn']=wwnn
    if (wwpn != None) & (wwpn != key):
        payload['wwpn']=wwpn
    if (adapter != None) & (adapter != key):
        payload['adapter']=adapter
    if (fabric_established != None) & (fabric_established != key):
        payload['fabric_established']=fabric_established
    if (firmware_rev != None) & (firmware_rev != key):
        payload['firmware_rev']=firmware_rev
    if (info_name != None) & (info_name != key):
        payload['info_name']=info_name
    if (max_speed != None) & (max_speed != key):
        payload['max_speed']=max_speed
    if (speed != None) & (speed != key):
        payload['speed']=speed
    if (physical_protocol != None) & (physical_protocol != key):
        payload['physical_protocol']=physical_protocol
    if (state != None) & (state != key):
        payload['state']=state
    if (status != None) & (status != key):
        payload['status']=status
    if (switch_port != None) & (switch_port != key):
        payload['switch_port']=switch_port
    if (data_link_rate != None) & (data_link_rate != key):
        payload['data_link_rate']=data_link_rate
    if (media_type != None) & (media_type != key):
        payload['media_type']=media_type
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
    url_path+="fc-ports/"

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
                "node_key" : {"required": False, "type": "str"},
                "wwnn" : {"required": False, "type": "str"},
                "wwpn" : {"required": False, "type": "str"},
                "adapter" : {"required": False, "type": "str"},
                "fabric_established" : {"required": False, "type": "str"},
                "firmware_rev" : {"required": False, "type": "str"},
                "info_name" : {"required": False, "type": "str"},
                "max_speed" : {"required": False, "type": "str"},
                "speed" : {"required": False, "type": "str"},
                "physical_protocol" : {"required": False, "type": "str"},
                "state" : {"required": False, "type": "str"},
                "status" : {"required": False, "type": "str"},
                "switch_port" : {"required": False, "type": "str"},
                "data_link_rate" : {"required": False, "type": "str"},
                "media_type" : {"required": False, "type": "str"},
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
        global node_key
        node_key = module.params["node_key"]
        global wwnn
        wwnn = module.params["wwnn"]
        global wwpn
        wwpn = module.params["wwpn"]
        global adapter
        adapter = module.params["adapter"]
        global fabric_established
        fabric_established = module.params["fabric_established"]
        global firmware_rev
        firmware_rev = module.params["firmware_rev"]
        global info_name
        info_name = module.params["info_name"]
        global max_speed
        max_speed = module.params["max_speed"]
        global speed
        speed = module.params["speed"]
        global physical_protocol
        physical_protocol = module.params["physical_protocol"]
        global state
        state = module.params["state"]
        global status
        status = module.params["status"]
        global switch_port
        switch_port = module.params["switch_port"]
        global data_link_rate
        data_link_rate = module.params["data_link_rate"]
        global media_type
        media_type = module.params["media_type"]
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
