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

    url_path+="application-records"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if record_name != None:
        if flag is 0:
            url_path+="?record_name="+record_name
            flag=1
        else:
            url_path+="&record_name="+record_name
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if hostname != None:
        if flag is 0:
            url_path+="?hostname="+hostname
            flag=1
        else:
            url_path+="&hostname="+hostname
    if url != None:
        if flag is 0:
            url_path+="?url="+url
            flag=1
        else:
            url_path+="&url="+url
    if system_id != None:
        if flag is 0:
            url_path+="?system_id="+system_id
            flag=1
        else:
            url_path+="&system_id="+system_id
    if version != None:
        if flag is 0:
            url_path+="?version="+version
            flag=1
        else:
            url_path+="&version="+version
    if ha_configured != None:
        if flag is 0:
            url_path+="?ha_configured="+ha_configured
            flag=1
        else:
            url_path+="&ha_configured="+ha_configured
    if platform != None:
        if flag is 0:
            url_path+="?platform="+platform
            flag=1
        else:
            url_path+="&platform="+platform
    if date_added != None:
        if flag is 0:
            url_path+="?date_added="+date_added
            flag=1
        else:
            url_path+="&date_added="+date_added
    if last_checkin != None:
        if flag is 0:
            url_path+="?last_checkin="+last_checkin
            flag=1
        else:
            url_path+="&last_checkin="+last_checkin
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
    url_path+="application-records"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (record_name != None) & (record_name != key):
        payload['record_name']=record_name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (hostname != None) & (hostname != key):
        payload['hostname']=hostname
    if (url != None) & (url != key):
        payload['url']=url
    if (system_id != None) & (system_id != key):
        payload['system_id']=system_id
    if (version != None) & (version != key):
        payload['version']=version
    if (ha_configured != None) & (ha_configured != key):
        payload['ha_configured']=ha_configured
    if (platform != None) & (platform != key):
        payload['platform']=platform
    if (date_added != None) & (date_added != key):
        payload['date_added']=date_added
    if (last_checkin != None) & (last_checkin != key):
        payload['last_checkin']=last_checkin
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
    url_path+="application-records/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (record_name != None) & (record_name != key):
        payload['record_name']=record_name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (hostname != None) & (hostname != key):
        payload['hostname']=hostname
    if (url != None) & (url != key):
        payload['url']=url
    if (system_id != None) & (system_id != key):
        payload['system_id']=system_id
    if (version != None) & (version != key):
        payload['version']=version
    if (ha_configured != None) & (ha_configured != key):
        payload['ha_configured']=ha_configured
    if (platform != None) & (platform != key):
        payload['platform']=platform
    if (date_added != None) & (date_added != key):
        payload['date_added']=date_added
    if (last_checkin != None) & (last_checkin != key):
        payload['last_checkin']=last_checkin
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
    url_path+="application-records/"

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
                "record_name" : {"required": False, "type": "str"},
                "cluster_key" : {"required": False, "type": "str"},
                "hostname" : {"required": False, "type": "str"},
                "url" : {"required": False, "type": "str"},
                "system_id" : {"required": False, "type": "str"},
                "version" : {"required": False, "type": "str"},
                "ha_configured" : {"required": False, "type": "str"},
                "platform" : {"required": False, "type": "str"},
                "date_added" : {"required": False, "type": "str"},
                "last_checkin" : {"required": False, "type": "str"},
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
        global record_name
        record_name = module.params["record_name"]
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global hostname
        hostname = module.params["hostname"]
        global url
        url = module.params["url"]
        global system_id
        system_id = module.params["system_id"]
        global version
        version = module.params["version"]
        global ha_configured
        ha_configured = module.params["ha_configured"]
        global platform
        platform = module.params["platform"]
        global date_added
        date_added = module.params["date_added"]
        global last_checkin
        last_checkin = module.params["last_checkin"]
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
