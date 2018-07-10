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

    url_path+="network-subnets"

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
    if network_broadcast_domain_key != None:
        if flag is 0:
            url_path+="?network_broadcast_domain_key="+network_broadcast_domain_key
            flag=1
        else:
            url_path+="&network_broadcast_domain_key="+network_broadcast_domain_key
    if subnet != None:
        if flag is 0:
            url_path+="?subnet="+subnet
            flag=1
        else:
            url_path+="&subnet="+subnet
    if network_ip_space_key != None:
        if flag is 0:
            url_path+="?network_ip_space_key="+network_ip_space_key
            flag=1
        else:
            url_path+="&network_ip_space_key="+network_ip_space_key
    if force_update_lif_associations != None:
        if flag is 0:
            url_path+="?force_update_lif_associations="+force_update_lif_associations
            flag=1
        else:
            url_path+="&force_update_lif_associations="+force_update_lif_associations
    if gateway_address != None:
        if flag is 0:
            url_path+="?gateway_address="+gateway_address
            flag=1
        else:
            url_path+="&gateway_address="+gateway_address
    if ip_ranges != None:
        if flag is 0:
            url_path+="?ip_ranges="+ip_ranges
            flag=1
        else:
            url_path+="&ip_ranges="+ip_ranges
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
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
    url_path+="network-subnets"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (network_broadcast_domain_key != None) & (network_broadcast_domain_key != key):
        payload['network_broadcast_domain_key']=network_broadcast_domain_key
    if (subnet != None) & (subnet != key):
        payload['subnet']=subnet
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (force_update_lif_associations != None) & (force_update_lif_associations != key):
        payload['force_update_lif_associations']=force_update_lif_associations
    if (gateway_address != None) & (gateway_address != key):
        payload['gateway_address']=gateway_address
    if (ip_ranges != None) & (ip_ranges != key):
        payload['ip_ranges']=ip_ranges
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
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
    url_path+="network-subnets/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (network_broadcast_domain_key != None) & (network_broadcast_domain_key != key):
        payload['network_broadcast_domain_key']=network_broadcast_domain_key
    if (subnet != None) & (subnet != key):
        payload['subnet']=subnet
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (force_update_lif_associations != None) & (force_update_lif_associations != key):
        payload['force_update_lif_associations']=force_update_lif_associations
    if (gateway_address != None) & (gateway_address != key):
        payload['gateway_address']=gateway_address
    if (ip_ranges != None) & (ip_ranges != key):
        payload['ip_ranges']=ip_ranges
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
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
    url_path+="network-subnets/"

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
                "network_broadcast_domain_key" : {"required": False, "type": "str"},
                "subnet" : {"required": False, "type": "str"},
                "network_ip_space_key" : {"required": False, "type": "str"},
                "force_update_lif_associations" : {"required": False, "type": "str"},
                "gateway_address" : {"required": False, "type": "str"},
                "ip_ranges" : {"required": False, "type": "str"},
                "cluster_key" : {"required": False, "type": "str"},
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
        global network_broadcast_domain_key
        network_broadcast_domain_key = module.params["network_broadcast_domain_key"]
        global subnet
        subnet = module.params["subnet"]
        global network_ip_space_key
        network_ip_space_key = module.params["network_ip_space_key"]
        global force_update_lif_associations
        force_update_lif_associations = module.params["force_update_lif_associations"]
        global gateway_address
        gateway_address = module.params["gateway_address"]
        global ip_ranges
        ip_ranges = module.params["ip_ranges"]
        global cluster_key
        cluster_key = module.params["cluster_key"]
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
