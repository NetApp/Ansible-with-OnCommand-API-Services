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

    url_path+="cluster-peers"

    flag=0

    if key != None:
        if flag is 0:
            url_path+="?key="+key
            flag=1
        else:
            url_path+="&key="+key
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if peer_cluster_key != None:
        if flag is 0:
            url_path+="?peer_cluster_key="+peer_cluster_key
            flag=1
        else:
            url_path+="&peer_cluster_key="+peer_cluster_key
    if address_family != None:
        if flag is 0:
            url_path+="?address_family="+address_family
            flag=1
        else:
            url_path+="&address_family="+address_family
    if network_ip_space_key != None:
        if flag is 0:
            url_path+="?network_ip_space_key="+network_ip_space_key
            flag=1
        else:
            url_path+="&network_ip_space_key="+network_ip_space_key
    if cluster_peer_addresses != None:
        if flag is 0:
            url_path+="?cluster_peer_addresses="+cluster_peer_addresses
            flag=1
        else:
            url_path+="&cluster_peer_addresses="+cluster_peer_addresses
    if local_addresses != None:
        if flag is 0:
            url_path+="?local_addresses="+local_addresses
            flag=1
        else:
            url_path+="&local_addresses="+local_addresses
    if passphrase != None:
        if flag is 0:
            url_path+="?passphrase="+passphrase
            flag=1
        else:
            url_path+="&passphrase="+passphrase
    if availability != None:
        if flag is 0:
            url_path+="?availability="+availability
            flag=1
        else:
            url_path+="&availability="+availability
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
    url_path+="cluster-peers"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (peer_cluster_key != None) & (peer_cluster_key != key):
        payload['peer_cluster_key']=peer_cluster_key
    if (address_family != None) & (address_family != key):
        payload['address_family']=address_family
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (cluster_peer_addresses != None) & (cluster_peer_addresses != key):
        payload['cluster_peer_addresses']=cluster_peer_addresses
    if (local_addresses != None) & (local_addresses != key):
        payload['local_addresses']=local_addresses
    if (passphrase != None) & (passphrase != key):
        payload['passphrase']=passphrase
    if (availability != None) & (availability != key):
        payload['availability']=availability
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
    url_path+="cluster-peers/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (peer_cluster_key != None) & (peer_cluster_key != key):
        payload['peer_cluster_key']=peer_cluster_key
    if (address_family != None) & (address_family != key):
        payload['address_family']=address_family
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (cluster_peer_addresses != None) & (cluster_peer_addresses != key):
        payload['cluster_peer_addresses']=cluster_peer_addresses
    if (local_addresses != None) & (local_addresses != key):
        payload['local_addresses']=local_addresses
    if (passphrase != None) & (passphrase != key):
        payload['passphrase']=passphrase
    if (availability != None) & (availability != key):
        payload['availability']=availability
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
    url_path+="cluster-peers/"

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
                "cluster_key" : {"required": False, "type": "str"},
                "peer_cluster_key" : {"required": False, "type": "str"},
                "address_family" : {"required": False, "type": "str"},
                "network_ip_space_key" : {"required": False, "type": "str"},
                "cluster_peer_addresses" : {"required": False, "type": "str"},
                "local_addresses" : {"required": False, "type": "str"},
                "passphrase" : {"required": False, "type": "str"},
                "availability" : {"required": False, "type": "str"},
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
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global peer_cluster_key
        peer_cluster_key = module.params["peer_cluster_key"]
        global address_family
        address_family = module.params["address_family"]
        global network_ip_space_key
        network_ip_space_key = module.params["network_ip_space_key"]
        global cluster_peer_addresses
        cluster_peer_addresses = module.params["cluster_peer_addresses"]
        global local_addresses
        local_addresses = module.params["local_addresses"]
        global passphrase
        passphrase = module.params["passphrase"]
        global availability
        availability = module.params["availability"]
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
