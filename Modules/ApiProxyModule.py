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


def post():
    url_path        = "/api/" + api_version + "/ontap/"
    if(storagevmkey!=None):
        url_path+="storage-vms/"+storagevmkey+"/advanced/jobs/"
    if(clusterkey!=None):
        url_path+="clusters/"+clusterkey+"/advanced/jobs/"
    else:
        return "Provide the storage_vm or cluster key" 
    url_path+="proxy-api"

    if is_sensitive != None:
            url_path+="?is_sensitive=false"
    else:
        if is_sensitive == false
            url_path+="?is_sensitive=false"
        else
            url_path+="?is_sensitive=true"

    payload={}
    payload['body']=body

    response=http_request_for_post(url_path,**payload)
    json_response=response.json()
    return json_response


def http_request_for_post(url_path,**payload):
    response = requests.post("https://"+api_host+":"+api_port+url_path, auth=(api_user_name,api_user_password), verify=False, data=json.dumps(payload),headers={'content-type': 'application/json'})
    return response



def main():
        fields = {
                "action" : {
                        "required": True,
                        "choices": [ 'post' ],
                        "type": 'str'
                        },
                "host" : {"required": True, "type": "str"},
                "port" : {"required": True, "type": "str"},
                "user" : {"required": True, "type": "str"},
                "password" : {"required": True, "type": "str"},
                "api_version" : {"required": False, "choices": [ '3.0', '4.0', '5.0' ], type: "str", "default": '2.0'},
                "storagevmkey" : {"required": False, "type": "str"},
                "clusterkey" : {"required": False, "type": "str"},
                "is_sensitive" : {"required": False, "type": "str"},
                "body" : {"required": False, "type": "str"},
                }

        module = AnsibleModule(argument_spec=fields)

        # NetApp Service Level Manager details
        global api_host
        global api_port
        global api_user_name
        global api_user_password
        global api_version

        global storagevmkey
        storagevmkey   = module.params["storagevmkey"]
        global clusterkey
        clusterkey   = module.params["clusterkey"]
        global is_sensitive
        is_sensitive   = module.params["is_sensitive"]

        api_host                = module.params["host"]
        api_port                = module.params["port"]
        api_user_name           = module.params["user"]
        api_user_password       = module.params["password"]
        api_version             = module.params["api_version"]

        # Properties details
        global body
        body = module.params["body"]

        global json_response

        # Actions
        if module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)

if __name__ == '__main__':
    main()
