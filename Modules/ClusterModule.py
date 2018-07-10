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
    url_path = "/api/" + api_version + "/ontap/"

    flag=0

    url_path+="clusters"

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
    if serial_number != None:
        if flag is 0:
            url_path+="?serial_number="+serial_number
            flag=1
        else:
            url_path+="&serial_number="+serial_number
    if management_ip != None:
        if flag is 0:
            url_path+="?management_ip="+management_ip
            flag=1
        else:
            url_path+="&management_ip="+management_ip
    if version != None:
        if flag is 0:
            url_path+="?version="+version
            flag=1
        else:
            url_path+="&version="+version
    if version_generation != None:
        if flag is 0:
            url_path+="?version_generation="+version_generation
            flag=1
        else:
            url_path+="&version_generation="+version_generation
    if version_major != None:
        if flag is 0:
            url_path+="?version_major="+version_major
            flag=1
        else:
            url_path+="&version_major="+version_major
    if version_minor != None:
        if flag is 0:
            url_path+="?version_minor="+version_minor
            flag=1
        else:
            url_path+="&version_minor="+version_minor
    if contact != None:
        if flag is 0:
            url_path+="?contact="+contact
            flag=1
        else:
            url_path+="&contact="+contact
    if location != None:
        if flag is 0:
            url_path+="?location="+location
            flag=1
        else:
            url_path+="&location="+location
    if ha_configured != None:
        if flag is 0:
            url_path+="?ha_configured="+ha_configured
            flag=1
        else:
            url_path+="&ha_configured="+ha_configured
    if time_zone != None:
        if flag is 0:
            url_path+="?time_zone="+time_zone
            flag=1
        else:
            url_path+="&time_zone="+time_zone
    if time_zone_utc != None:
        if flag is 0:
            url_path+="?time_zone_utc="+time_zone_utc
            flag=1
        else:
            url_path+="&time_zone_utc="+time_zone_utc
    if time_zone_version != None:
        if flag is 0:
            url_path+="?time_zone_version="+time_zone_version
            flag=1
        else:
            url_path+="&time_zone_version="+time_zone_version
    if is_metro_cluster != None:
        if flag is 0:
            url_path+="?is_metro_cluster="+is_metro_cluster
            flag=1
        else:
            url_path+="&is_metro_cluster="+is_metro_cluster
    if metro_cluster_partner_storage_system_key != None:
        if flag is 0:
            url_path+="?metro_cluster_partner_storage_system_key="+metro_cluster_partner_storage_system_key
            flag=1
        else:
            url_path+="&metro_cluster_partner_storage_system_key="+metro_cluster_partner_storage_system_key
    if metro_cluster_configuration_state != None:
        if flag is 0:
            url_path+="?metro_cluster_configuration_state="+metro_cluster_configuration_state
            flag=1
        else:
            url_path+="&metro_cluster_configuration_state="+metro_cluster_configuration_state
    if metro_cluster_mode != None:
        if flag is 0:
            url_path+="?metro_cluster_mode="+metro_cluster_mode
            flag=1
        else:
            url_path+="&metro_cluster_mode="+metro_cluster_mode
    if status != None:
        if flag is 0:
            url_path+="?status="+status
            flag=1
        else:
            url_path+="&status="+status
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
    url_path+="clusters"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (management_ip != None) & (management_ip != key):
        payload['management_ip']=management_ip
    if (version != None) & (version != key):
        payload['version']=version
    if (version_generation != None) & (version_generation != key):
        payload['version_generation']=version_generation
    if (version_major != None) & (version_major != key):
        payload['version_major']=version_major
    if (version_minor != None) & (version_minor != key):
        payload['version_minor']=version_minor
    if (contact != None) & (contact != key):
        payload['contact']=contact
    if (location != None) & (location != key):
        payload['location']=location
    if (ha_configured != None) & (ha_configured != key):
        payload['ha_configured']=ha_configured
    if (time_zone != None) & (time_zone != key):
        payload['time_zone']=time_zone
    if (time_zone_utc != None) & (time_zone_utc != key):
        payload['time_zone_utc']=time_zone_utc
    if (time_zone_version != None) & (time_zone_version != key):
        payload['time_zone_version']=time_zone_version
    if (is_metro_cluster != None) & (is_metro_cluster != key):
        payload['is_metro_cluster']=is_metro_cluster
    if (metro_cluster_partner_storage_system_key != None) & (metro_cluster_partner_storage_system_key != key):
        payload['metro_cluster_partner_storage_system_key']=metro_cluster_partner_storage_system_key
    if (metro_cluster_configuration_state != None) & (metro_cluster_configuration_state != key):
        payload['metro_cluster_configuration_state']=metro_cluster_configuration_state
    if (metro_cluster_mode != None) & (metro_cluster_mode != key):
        payload['metro_cluster_mode']=metro_cluster_mode
    if (status != None) & (status != key):
        payload['status']=status
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
    url_path+="clusters/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (management_ip != None) & (management_ip != key):
        payload['management_ip']=management_ip
    if (version != None) & (version != key):
        payload['version']=version
    if (version_generation != None) & (version_generation != key):
        payload['version_generation']=version_generation
    if (version_major != None) & (version_major != key):
        payload['version_major']=version_major
    if (version_minor != None) & (version_minor != key):
        payload['version_minor']=version_minor
    if (contact != None) & (contact != key):
        payload['contact']=contact
    if (location != None) & (location != key):
        payload['location']=location
    if (ha_configured != None) & (ha_configured != key):
        payload['ha_configured']=ha_configured
    if (time_zone != None) & (time_zone != key):
        payload['time_zone']=time_zone
    if (time_zone_utc != None) & (time_zone_utc != key):
        payload['time_zone_utc']=time_zone_utc
    if (time_zone_version != None) & (time_zone_version != key):
        payload['time_zone_version']=time_zone_version
    if (is_metro_cluster != None) & (is_metro_cluster != key):
        payload['is_metro_cluster']=is_metro_cluster
    if (metro_cluster_partner_storage_system_key != None) & (metro_cluster_partner_storage_system_key != key):
        payload['metro_cluster_partner_storage_system_key']=metro_cluster_partner_storage_system_key
    if (metro_cluster_configuration_state != None) & (metro_cluster_configuration_state != key):
        payload['metro_cluster_configuration_state']=metro_cluster_configuration_state
    if (metro_cluster_mode != None) & (metro_cluster_mode != key):
        payload['metro_cluster_mode']=metro_cluster_mode
    if (status != None) & (status != key):
        payload['status']=status
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
    url_path+="clusters/"

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
                "serial_number" : {"required": False, "type": "str"},
                "management_ip" : {"required": False, "type": "str"},
                "version" : {"required": False, "type": "str"},
                "version_generation" : {"required": False, "type": "str"},
                "version_major" : {"required": False, "type": "str"},
                "version_minor" : {"required": False, "type": "str"},
                "contact" : {"required": False, "type": "str"},
                "location" : {"required": False, "type": "str"},
                "ha_configured" : {"required": False, "type": "str"},
                "time_zone" : {"required": False, "type": "str"},
                "time_zone_utc" : {"required": False, "type": "str"},
                "time_zone_version" : {"required": False, "type": "str"},
                "is_metro_cluster" : {"required": False, "type": "str"},
                "metro_cluster_partner_storage_system_key" : {"required": False, "type": "str"},
                "metro_cluster_configuration_state" : {"required": False, "type": "str"},
                "metro_cluster_mode" : {"required": False, "type": "str"},
                "status" : {"required": False, "type": "str"},
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
        global serial_number
        serial_number = module.params["serial_number"]
        global management_ip
        management_ip = module.params["management_ip"]
        global version
        version = module.params["version"]
        global version_generation
        version_generation = module.params["version_generation"]
        global version_major
        version_major = module.params["version_major"]
        global version_minor
        version_minor = module.params["version_minor"]
        global contact
        contact = module.params["contact"]
        global location
        location = module.params["location"]
        global ha_configured
        ha_configured = module.params["ha_configured"]
        global time_zone
        time_zone = module.params["time_zone"]
        global time_zone_utc
        time_zone_utc = module.params["time_zone_utc"]
        global time_zone_version
        time_zone_version = module.params["time_zone_version"]
        global is_metro_cluster
        is_metro_cluster = module.params["is_metro_cluster"]
        global metro_cluster_partner_storage_system_key
        metro_cluster_partner_storage_system_key = module.params["metro_cluster_partner_storage_system_key"]
        global metro_cluster_configuration_state
        metro_cluster_configuration_state = module.params["metro_cluster_configuration_state"]
        global metro_cluster_mode
        metro_cluster_mode = module.params["metro_cluster_mode"]
        global status
        status = module.params["status"]
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
