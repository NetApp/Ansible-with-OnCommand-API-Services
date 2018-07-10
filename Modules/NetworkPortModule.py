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

    url_path+="network-ports"

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
    if node_key != None:
        if flag is 0:
            url_path+="?node_key="+node_key
            flag=1
        else:
            url_path+="&node_key="+node_key
    if network_broadcast_domain_key != None:
        if flag is 0:
            url_path+="?network_broadcast_domain_key="+network_broadcast_domain_key
            flag=1
        else:
            url_path+="&network_broadcast_domain_key="+network_broadcast_domain_key
    if vlan_port_key != None:
        if flag is 0:
            url_path+="?vlan_port_key="+vlan_port_key
            flag=1
        else:
            url_path+="&vlan_port_key="+vlan_port_key
    if ifgroup_key != None:
        if flag is 0:
            url_path+="?ifgroup_key="+ifgroup_key
            flag=1
        else:
            url_path+="&ifgroup_key="+ifgroup_key
    if mac_address != None:
        if flag is 0:
            url_path+="?mac_address="+mac_address
            flag=1
        else:
            url_path+="&mac_address="+mac_address
    if administrative_speed != None:
        if flag is 0:
            url_path+="?administrative_speed="+administrative_speed
            flag=1
        else:
            url_path+="&administrative_speed="+administrative_speed
    if operational_speed != None:
        if flag is 0:
            url_path+="?operational_speed="+operational_speed
            flag=1
        else:
            url_path+="&operational_speed="+operational_speed
    if link_status != None:
        if flag is 0:
            url_path+="?link_status="+link_status
            flag=1
        else:
            url_path+="&link_status="+link_status
    if role != None:
        if flag is 0:
            url_path+="?role="+role
            flag=1
        else:
            url_path+="&role="+role
    if port_type != None:
        if flag is 0:
            url_path+="?port_type="+port_type
            flag=1
        else:
            url_path+="&port_type="+port_type
    if vlan_identifier != None:
        if flag is 0:
            url_path+="?vlan_identifier="+vlan_identifier
            flag=1
        else:
            url_path+="&vlan_identifier="+vlan_identifier
    if mtu != None:
        if flag is 0:
            url_path+="?mtu="+mtu
            flag=1
        else:
            url_path+="&mtu="+mtu
    if operational_duplex != None:
        if flag is 0:
            url_path+="?operational_duplex="+operational_duplex
            flag=1
        else:
            url_path+="&operational_duplex="+operational_duplex
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
    url_path+="network-ports"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (network_broadcast_domain_key != None) & (network_broadcast_domain_key != key):
        payload['network_broadcast_domain_key']=network_broadcast_domain_key
    if (vlan_port_key != None) & (vlan_port_key != key):
        payload['vlan_port_key']=vlan_port_key
    if (ifgroup_key != None) & (ifgroup_key != key):
        payload['ifgroup_key']=ifgroup_key
    if (mac_address != None) & (mac_address != key):
        payload['mac_address']=mac_address
    if (administrative_speed != None) & (administrative_speed != key):
        payload['administrative_speed']=administrative_speed
    if (operational_speed != None) & (operational_speed != key):
        payload['operational_speed']=operational_speed
    if (link_status != None) & (link_status != key):
        payload['link_status']=link_status
    if (role != None) & (role != key):
        payload['role']=role
    if (port_type != None) & (port_type != key):
        payload['port_type']=port_type
    if (vlan_identifier != None) & (vlan_identifier != key):
        payload['vlan_identifier']=vlan_identifier
    if (mtu != None) & (mtu != key):
        payload['mtu']=mtu
    if (operational_duplex != None) & (operational_duplex != key):
        payload['operational_duplex']=operational_duplex
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
    url_path+="network-ports/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (node_key != None) & (node_key != key):
        payload['node_key']=node_key
    if (network_broadcast_domain_key != None) & (network_broadcast_domain_key != key):
        payload['network_broadcast_domain_key']=network_broadcast_domain_key
    if (vlan_port_key != None) & (vlan_port_key != key):
        payload['vlan_port_key']=vlan_port_key
    if (ifgroup_key != None) & (ifgroup_key != key):
        payload['ifgroup_key']=ifgroup_key
    if (mac_address != None) & (mac_address != key):
        payload['mac_address']=mac_address
    if (administrative_speed != None) & (administrative_speed != key):
        payload['administrative_speed']=administrative_speed
    if (operational_speed != None) & (operational_speed != key):
        payload['operational_speed']=operational_speed
    if (link_status != None) & (link_status != key):
        payload['link_status']=link_status
    if (role != None) & (role != key):
        payload['role']=role
    if (port_type != None) & (port_type != key):
        payload['port_type']=port_type
    if (vlan_identifier != None) & (vlan_identifier != key):
        payload['vlan_identifier']=vlan_identifier
    if (mtu != None) & (mtu != key):
        payload['mtu']=mtu
    if (operational_duplex != None) & (operational_duplex != key):
        payload['operational_duplex']=operational_duplex
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
    url_path+="network-ports/"

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
                "node_key" : {"required": False, "type": "str"},
                "network_broadcast_domain_key" : {"required": False, "type": "str"},
                "vlan_port_key" : {"required": False, "type": "str"},
                "ifgroup_key" : {"required": False, "type": "str"},
                "mac_address" : {"required": False, "type": "str"},
                "administrative_speed" : {"required": False, "type": "str"},
                "operational_speed" : {"required": False, "type": "str"},
                "link_status" : {"required": False, "type": "str"},
                "role" : {"required": False, "type": "str"},
                "port_type" : {"required": False, "type": "str"},
                "vlan_identifier" : {"required": False, "type": "str"},
                "mtu" : {"required": False, "type": "str"},
                "operational_duplex" : {"required": False, "type": "str"},
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
        global node_key
        node_key = module.params["node_key"]
        global network_broadcast_domain_key
        network_broadcast_domain_key = module.params["network_broadcast_domain_key"]
        global vlan_port_key
        vlan_port_key = module.params["vlan_port_key"]
        global ifgroup_key
        ifgroup_key = module.params["ifgroup_key"]
        global mac_address
        mac_address = module.params["mac_address"]
        global administrative_speed
        administrative_speed = module.params["administrative_speed"]
        global operational_speed
        operational_speed = module.params["operational_speed"]
        global link_status
        link_status = module.params["link_status"]
        global role
        role = module.params["role"]
        global port_type
        port_type = module.params["port_type"]
        global vlan_identifier
        vlan_identifier = module.params["vlan_identifier"]
        global mtu
        mtu = module.params["mtu"]
        global operational_duplex
        operational_duplex = module.params["operational_duplex"]
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
