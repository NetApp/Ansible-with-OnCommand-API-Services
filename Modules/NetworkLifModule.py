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

    url_path+="network-lifs"

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
    if storage_vm_key != None:
        if flag is 0:
            url_path+="?storage_vm_key="+storage_vm_key
            flag=1
        else:
            url_path+="&storage_vm_key="+storage_vm_key
    if current_port_key != None:
        if flag is 0:
            url_path+="?current_port_key="+current_port_key
            flag=1
        else:
            url_path+="&current_port_key="+current_port_key
    if home_port_key != None:
        if flag is 0:
            url_path+="?home_port_key="+home_port_key
            flag=1
        else:
            url_path+="&home_port_key="+home_port_key
    if routing_group_key != None:
        if flag is 0:
            url_path+="?routing_group_key="+routing_group_key
            flag=1
        else:
            url_path+="&routing_group_key="+routing_group_key
    if is_auto_revert != None:
        if flag is 0:
            url_path+="?is_auto_revert="+is_auto_revert
            flag=1
        else:
            url_path+="&is_auto_revert="+is_auto_revert
    if is_home != None:
        if flag is 0:
            url_path+="?is_home="+is_home
            flag=1
        else:
            url_path+="&is_home="+is_home
    if address != None:
        if flag is 0:
            url_path+="?address="+address
            flag=1
        else:
            url_path+="&address="+address
    if netmask != None:
        if flag is 0:
            url_path+="?netmask="+netmask
            flag=1
        else:
            url_path+="&netmask="+netmask
    if netmask_length != None:
        if flag is 0:
            url_path+="?netmask_length="+netmask_length
            flag=1
        else:
            url_path+="&netmask_length="+netmask_length
    if dns_domain_name != None:
        if flag is 0:
            url_path+="?dns_domain_name="+dns_domain_name
            flag=1
        else:
            url_path+="&dns_domain_name="+dns_domain_name
    if operational_status != None:
        if flag is 0:
            url_path+="?operational_status="+operational_status
            flag=1
        else:
            url_path+="&operational_status="+operational_status
    if administrative_status != None:
        if flag is 0:
            url_path+="?administrative_status="+administrative_status
            flag=1
        else:
            url_path+="&administrative_status="+administrative_status
    if role != None:
        if flag is 0:
            url_path+="?role="+role
            flag=1
        else:
            url_path+="&role="+role
    if data_protocols != None:
        if flag is 0:
            url_path+="?data_protocols="+data_protocols
            flag=1
        else:
            url_path+="&data_protocols="+data_protocols
    if failover_group != None:
        if flag is 0:
            url_path+="?failover_group="+failover_group
            flag=1
        else:
            url_path+="&failover_group="+failover_group
    if failover_policy != None:
        if flag is 0:
            url_path+="?failover_policy="+failover_policy
            flag=1
        else:
            url_path+="&failover_policy="+failover_policy
    if force_subnet_association != None:
        if flag is 0:
            url_path+="?force_subnet_association="+force_subnet_association
            flag=1
        else:
            url_path+="&force_subnet_association="+force_subnet_association
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
    url_path+="network-lifs"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (current_port_key != None) & (current_port_key != key):
        payload['current_port_key']=current_port_key
    if (home_port_key != None) & (home_port_key != key):
        payload['home_port_key']=home_port_key
    if (routing_group_key != None) & (routing_group_key != key):
        payload['routing_group_key']=routing_group_key
    if (is_auto_revert != None) & (is_auto_revert != key):
        payload['is_auto_revert']=is_auto_revert
    if (is_home != None) & (is_home != key):
        payload['is_home']=is_home
    if (address != None) & (address != key):
        payload['address']=address
    if (netmask != None) & (netmask != key):
        payload['netmask']=netmask
    if (netmask_length != None) & (netmask_length != key):
        payload['netmask_length']=netmask_length
    if (dns_domain_name != None) & (dns_domain_name != key):
        payload['dns_domain_name']=dns_domain_name
    if (operational_status != None) & (operational_status != key):
        payload['operational_status']=operational_status
    if (administrative_status != None) & (administrative_status != key):
        payload['administrative_status']=administrative_status
    if (role != None) & (role != key):
        payload['role']=role
    if (data_protocols != None) & (data_protocols != key):
        payload['data_protocols']=data_protocols
    if (failover_group != None) & (failover_group != key):
        payload['failover_group']=failover_group
    if (failover_policy != None) & (failover_policy != key):
        payload['failover_policy']=failover_policy
    if (force_subnet_association != None) & (force_subnet_association != key):
        payload['force_subnet_association']=force_subnet_association
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
    url_path+="network-lifs/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (storage_vm_key != None) & (storage_vm_key != key):
        payload['storage_vm_key']=storage_vm_key
    if (current_port_key != None) & (current_port_key != key):
        payload['current_port_key']=current_port_key
    if (home_port_key != None) & (home_port_key != key):
        payload['home_port_key']=home_port_key
    if (routing_group_key != None) & (routing_group_key != key):
        payload['routing_group_key']=routing_group_key
    if (is_auto_revert != None) & (is_auto_revert != key):
        payload['is_auto_revert']=is_auto_revert
    if (is_home != None) & (is_home != key):
        payload['is_home']=is_home
    if (address != None) & (address != key):
        payload['address']=address
    if (netmask != None) & (netmask != key):
        payload['netmask']=netmask
    if (netmask_length != None) & (netmask_length != key):
        payload['netmask_length']=netmask_length
    if (dns_domain_name != None) & (dns_domain_name != key):
        payload['dns_domain_name']=dns_domain_name
    if (operational_status != None) & (operational_status != key):
        payload['operational_status']=operational_status
    if (administrative_status != None) & (administrative_status != key):
        payload['administrative_status']=administrative_status
    if (role != None) & (role != key):
        payload['role']=role
    if (data_protocols != None) & (data_protocols != key):
        payload['data_protocols']=data_protocols
    if (failover_group != None) & (failover_group != key):
        payload['failover_group']=failover_group
    if (failover_policy != None) & (failover_policy != key):
        payload['failover_policy']=failover_policy
    if (force_subnet_association != None) & (force_subnet_association != key):
        payload['force_subnet_association']=force_subnet_association
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
    url_path+="network-lifs/"

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
                "storage_vm_key" : {"required": False, "type": "str"},
                "current_port_key" : {"required": False, "type": "str"},
                "home_port_key" : {"required": False, "type": "str"},
                "routing_group_key" : {"required": False, "type": "str"},
                "is_auto_revert" : {"required": False, "type": "str"},
                "is_home" : {"required": False, "type": "str"},
                "address" : {"required": False, "type": "str"},
                "netmask" : {"required": False, "type": "str"},
                "netmask_length" : {"required": False, "type": "str"},
                "dns_domain_name" : {"required": False, "type": "str"},
                "operational_status" : {"required": False, "type": "str"},
                "administrative_status" : {"required": False, "type": "str"},
                "role" : {"required": False, "type": "str"},
                "data_protocols" : {"required": False, "type": "str"},
                "failover_group" : {"required": False, "type": "str"},
                "failover_policy" : {"required": False, "type": "str"},
                "force_subnet_association" : {"required": False, "type": "str"},
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
        global storage_vm_key
        storage_vm_key = module.params["storage_vm_key"]
        global current_port_key
        current_port_key = module.params["current_port_key"]
        global home_port_key
        home_port_key = module.params["home_port_key"]
        global routing_group_key
        routing_group_key = module.params["routing_group_key"]
        global is_auto_revert
        is_auto_revert = module.params["is_auto_revert"]
        global is_home
        is_home = module.params["is_home"]
        global address
        address = module.params["address"]
        global netmask
        netmask = module.params["netmask"]
        global netmask_length
        netmask_length = module.params["netmask_length"]
        global dns_domain_name
        dns_domain_name = module.params["dns_domain_name"]
        global operational_status
        operational_status = module.params["operational_status"]
        global administrative_status
        administrative_status = module.params["administrative_status"]
        global role
        role = module.params["role"]
        global data_protocols
        data_protocols = module.params["data_protocols"]
        global failover_group
        failover_group = module.params["failover_group"]
        global failover_policy
        failover_policy = module.params["failover_policy"]
        global force_subnet_association
        force_subnet_association = module.params["force_subnet_association"]
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
