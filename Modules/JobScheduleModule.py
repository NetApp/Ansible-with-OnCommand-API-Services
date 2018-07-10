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

    url_path+="job-schedules"

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
    if cluster_key != None:
        if flag is 0:
            url_path+="?cluster_key="+cluster_key
            flag=1
        else:
            url_path+="&cluster_key="+cluster_key
    if description != None:
        if flag is 0:
            url_path+="?description="+description
            flag=1
        else:
            url_path+="&description="+description
    if schedule_type != None:
        if flag is 0:
            url_path+="?schedule_type="+schedule_type
            flag=1
        else:
            url_path+="&schedule_type="+schedule_type
    if cron_day_of_month != None:
        if flag is 0:
            url_path+="?cron_day_of_month="+cron_day_of_month
            flag=1
        else:
            url_path+="&cron_day_of_month="+cron_day_of_month
    if cron_day_of_week != None:
        if flag is 0:
            url_path+="?cron_day_of_week="+cron_day_of_week
            flag=1
        else:
            url_path+="&cron_day_of_week="+cron_day_of_week
    if cron_hour != None:
        if flag is 0:
            url_path+="?cron_hour="+cron_hour
            flag=1
        else:
            url_path+="&cron_hour="+cron_hour
    if cron_minute != None:
        if flag is 0:
            url_path+="?cron_minute="+cron_minute
            flag=1
        else:
            url_path+="&cron_minute="+cron_minute
    if cron_month != None:
        if flag is 0:
            url_path+="?cron_month="+cron_month
            flag=1
        else:
            url_path+="&cron_month="+cron_month
    if interval_days != None:
        if flag is 0:
            url_path+="?interval_days="+interval_days
            flag=1
        else:
            url_path+="&interval_days="+interval_days
    if interval_hours != None:
        if flag is 0:
            url_path+="?interval_hours="+interval_hours
            flag=1
        else:
            url_path+="&interval_hours="+interval_hours
    if interval_minutes != None:
        if flag is 0:
            url_path+="?interval_minutes="+interval_minutes
            flag=1
        else:
            url_path+="&interval_minutes="+interval_minutes
    if interval_seconds != None:
        if flag is 0:
            url_path+="?interval_seconds="+interval_seconds
            flag=1
        else:
            url_path+="&interval_seconds="+interval_seconds
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
    url_path = "/api/" + api_version + "/ontap/"
    url_path+="job-schedules/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (description != None) & (description != key):
        payload['description']=description
    if (schedule_type != None) & (schedule_type != key):
        payload['schedule_type']=schedule_type
    if (cron_day_of_month != None) & (cron_day_of_month != key):
        payload['cron_day_of_month']=cron_day_of_month
    if (cron_day_of_week != None) & (cron_day_of_week != key):
        payload['cron_day_of_week']=cron_day_of_week
    if (cron_hour != None) & (cron_hour != key):
        payload['cron_hour']=cron_hour
    if (cron_minute != None) & (cron_minute != key):
        payload['cron_minute']=cron_minute
    if (cron_month != None) & (cron_month != key):
        payload['cron_month']=cron_month
    if (interval_days != None) & (interval_days != key):
        payload['interval_days']=interval_days
    if (interval_hours != None) & (interval_hours != key):
        payload['interval_hours']=interval_hours
    if (interval_minutes != None) & (interval_minutes != key):
        payload['interval_minutes']=interval_minutes
    if (interval_seconds != None) & (interval_seconds != key):
        payload['interval_seconds']=interval_seconds
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag

    response=http_request_for_post(url_path,**payload)
    json_response=response.json()
    return json_response

def put():
    url_path = "/api/" + api_version + "/ontap/"
    url_path+="job-schedules"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (description != None) & (description != key):
        payload['description']=description
    if (schedule_type != None) & (schedule_type != key):
        payload['schedule_type']=schedule_type
    if (cron_day_of_month != None) & (cron_day_of_month != key):
        payload['cron_day_of_month']=cron_day_of_month
    if (cron_day_of_week != None) & (cron_day_of_week != key):
        payload['cron_day_of_week']=cron_day_of_week
    if (cron_hour != None) & (cron_hour != key):
        payload['cron_hour']=cron_hour
    if (cron_minute != None) & (cron_minute != key):
        payload['cron_minute']=cron_minute
    if (cron_month != None) & (cron_month != key):
        payload['cron_month']=cron_month
    if (interval_days != None) & (interval_days != key):
        payload['interval_days']=interval_days
    if (interval_hours != None) & (interval_hours != key):
        payload['interval_hours']=interval_hours
    if (interval_minutes != None) & (interval_minutes != key):
        payload['interval_minutes']=interval_minutes
    if (interval_seconds != None) & (interval_seconds != key):
        payload['interval_seconds']=interval_seconds
    if (sortBy != None) & (sortBy != key):
        payload['sortBy']=sortBy
    if (maxRecords != None) & (maxRecords != key):
        payload['maxRecords']=maxRecords
    if (nextTag != None) & (nextTag != key):
        payload['nextTag']=nextTag
    if key != None:
        url_path+=key
        response=http_request_for_put(url_path,**payload)
        json_response=response.json()
        return json_response
    else:
        return "Provide the object key"

def delete():
    url_path = "/api/" + api_version + "/ontap/"
    url_path+="job-schedules/"

    if key != None:
        url_path+=key
        response=http_request_for_delete(url_path)
        json_response=response.json()
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
                "cluster_key" : {"required": False, "type": "str"},
                "description" : {"required": False, "type": "str"},
                "schedule_type" : {"required": False, "type": "str"},
                "cron_day_of_month" : {"required": False, "type": "str"},
                "cron_day_of_week" : {"required": False, "type": "str"},
                "cron_hour" : {"required": False, "type": "str"},
                "cron_minute" : {"required": False, "type": "str"},
                "cron_month" : {"required": False, "type": "str"},
                "interval_days" : {"required": False, "type": "str"},
                "interval_hours" : {"required": False, "type": "str"},
                "interval_minutes" : {"required": False, "type": "str"},
                "interval_seconds" : {"required": False, "type": "str"},
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
        global cluster_key
        cluster_key = module.params["cluster_key"]
        global description
        description = module.params["description"]
        global schedule_type
        schedule_type = module.params["schedule_type"]
        global cron_day_of_month
        cron_day_of_month = module.params["cron_day_of_month"]
        global cron_day_of_week
        cron_day_of_week = module.params["cron_day_of_week"]
        global cron_hour
        cron_hour = module.params["cron_hour"]
        global cron_minute
        cron_minute = module.params["cron_minute"]
        global cron_month
        cron_month = module.params["cron_month"]
        global interval_days
        interval_days = module.params["interval_days"]
        global interval_hours
        interval_hours = module.params["interval_hours"]
        global interval_minutes
        interval_minutes = module.params["interval_minutes"]
        global interval_seconds
        interval_seconds = module.params["interval_seconds"]
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
                module.exit_json(changed=True,meta=result)
        elif module.params["action"] == "post":
                result=post()
                module.exit_json(changed=True,meta=result)
        elif module.params["action"] == "delete":
                result=delete()
                module.exit_json(changed=True,meta=result)


if __name__ == '__main__':
    main()
