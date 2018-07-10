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

    url_path+="nodes"

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
    if partner_node_key != None:
        if flag is 0:
            url_path+="?partner_node_key="+partner_node_key
            flag=1
        else:
            url_path+="&partner_node_key="+partner_node_key
    if metro_cluster_dr_partner_node_key != None:
        if flag is 0:
            url_path+="?metro_cluster_dr_partner_node_key="+metro_cluster_dr_partner_node_key
            flag=1
        else:
            url_path+="&metro_cluster_dr_partner_node_key="+metro_cluster_dr_partner_node_key
    if metro_cluster_dr_operation_state != None:
        if flag is 0:
            url_path+="?metro_cluster_dr_operation_state="+metro_cluster_dr_operation_state
            flag=1
        else:
            url_path+="&metro_cluster_dr_operation_state="+metro_cluster_dr_operation_state
    if serial_number != None:
        if flag is 0:
            url_path+="?serial_number="+serial_number
            flag=1
        else:
            url_path+="&serial_number="+serial_number
    if version != None:
        if flag is 0:
            url_path+="?version="+version
            flag=1
        else:
            url_path+="&version="+version
    if model != None:
        if flag is 0:
            url_path+="?model="+model
            flag=1
        else:
            url_path+="&model="+model
    if uptime != None:
        if flag is 0:
            url_path+="?uptime="+uptime
            flag=1
        else:
            url_path+="&uptime="+uptime
    if vendor != None:
        if flag is 0:
            url_path+="?vendor="+vendor
            flag=1
        else:
            url_path+="&vendor="+vendor
    if location != None:
        if flag is 0:
            url_path+="?location="+location
            flag=1
        else:
            url_path+="&location="+location
    if failover_state != None:
        if flag is 0:
            url_path+="?failover_state="+failover_state
            flag=1
        else:
            url_path+="&failover_state="+failover_state
    if cpu_processor_type != None:
        if flag is 0:
            url_path+="?cpu_processor_type="+cpu_processor_type
            flag=1
        else:
            url_path+="&cpu_processor_type="+cpu_processor_type
    if cpu_processor_id != None:
        if flag is 0:
            url_path+="?cpu_processor_id="+cpu_processor_id
            flag=1
        else:
            url_path+="&cpu_processor_id="+cpu_processor_id
    if number_of_processors != None:
        if flag is 0:
            url_path+="?number_of_processors="+number_of_processors
            flag=1
        else:
            url_path+="&number_of_processors="+number_of_processors
    if memory_size != None:
        if flag is 0:
            url_path+="?memory_size="+memory_size
            flag=1
        else:
            url_path+="&memory_size="+memory_size
    if product_type != None:
        if flag is 0:
            url_path+="?product_type="+product_type
            flag=1
        else:
            url_path+="&product_type="+product_type
    if nvram_id != None:
        if flag is 0:
            url_path+="?nvram_id="+nvram_id
            flag=1
        else:
            url_path+="&nvram_id="+nvram_id
    if cpu_firmware_release != None:
        if flag is 0:
            url_path+="?cpu_firmware_release="+cpu_firmware_release
            flag=1
        else:
            url_path+="&cpu_firmware_release="+cpu_firmware_release
    if is_over_temperature != None:
        if flag is 0:
            url_path+="?is_over_temperature="+is_over_temperature
            flag=1
        else:
            url_path+="&is_over_temperature="+is_over_temperature
    if failed_fan_count != None:
        if flag is 0:
            url_path+="?failed_fan_count="+failed_fan_count
            flag=1
        else:
            url_path+="&failed_fan_count="+failed_fan_count
    if failed_power_supply_count != None:
        if flag is 0:
            url_path+="?failed_power_supply_count="+failed_power_supply_count
            flag=1
        else:
            url_path+="&failed_power_supply_count="+failed_power_supply_count
    if nvram_battery_status != None:
        if flag is 0:
            url_path+="?nvram_battery_status="+nvram_battery_status
            flag=1
        else:
            url_path+="&nvram_battery_status="+nvram_battery_status
    if is_failover_enabled != None:
        if flag is 0:
            url_path+="?is_failover_enabled="+is_failover_enabled
            flag=1
        else:
            url_path+="&is_failover_enabled="+is_failover_enabled
    if is_take_over_possible != None:
        if flag is 0:
            url_path+="?is_take_over_possible="+is_take_over_possible
            flag=1
        else:
            url_path+="&is_take_over_possible="+is_take_over_possible
    if partner_firmware_state != None:
        if flag is 0:
            url_path+="?partner_firmware_state="+partner_firmware_state
            flag=1
        else:
            url_path+="&partner_firmware_state="+partner_firmware_state
    if local_firmware_state != None:
        if flag is 0:
            url_path+="?local_firmware_state="+local_firmware_state
            flag=1
        else:
            url_path+="&local_firmware_state="+local_firmware_state
    if is_interconnect_up != None:
        if flag is 0:
            url_path+="?is_interconnect_up="+is_interconnect_up
            flag=1
        else:
            url_path+="&is_interconnect_up="+is_interconnect_up
    if interconnect_links != None:
        if flag is 0:
            url_path+="?interconnect_links="+interconnect_links
            flag=1
        else:
            url_path+="&interconnect_links="+interconnect_links
    if interconnect_type != None:
        if flag is 0:
            url_path+="?interconnect_type="+interconnect_type
            flag=1
        else:
            url_path+="&interconnect_type="+interconnect_type
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
    if owner != None:
        if flag is 0:
            url_path+="?owner="+owner
            flag=1
        else:
            url_path+="&owner="+owner
    if is_node_healthy != None:
        if flag is 0:
            url_path+="?is_node_healthy="+is_node_healthy
            flag=1
        else:
            url_path+="&is_node_healthy="+is_node_healthy
    if is_epsilon_node != None:
        if flag is 0:
            url_path+="?is_epsilon_node="+is_epsilon_node
            flag=1
        else:
            url_path+="&is_epsilon_node="+is_epsilon_node
    if env_failed_fan_message != None:
        if flag is 0:
            url_path+="?env_failed_fan_message="+env_failed_fan_message
            flag=1
        else:
            url_path+="&env_failed_fan_message="+env_failed_fan_message
    if env_failed_power_supply_message != None:
        if flag is 0:
            url_path+="?env_failed_power_supply_message="+env_failed_power_supply_message
            flag=1
        else:
            url_path+="&env_failed_power_supply_message="+env_failed_power_supply_message
    if give_back_state != None:
        if flag is 0:
            url_path+="?give_back_state="+give_back_state
            flag=1
        else:
            url_path+="&give_back_state="+give_back_state
    if current_mode != None:
        if flag is 0:
            url_path+="?current_mode="+current_mode
            flag=1
        else:
            url_path+="&current_mode="+current_mode
    if takeover_by_partner_not_possible_reason != None:
        if flag is 0:
            url_path+="?takeover_by_partner_not_possible_reason="+takeover_by_partner_not_possible_reason
            flag=1
        else:
            url_path+="&takeover_by_partner_not_possible_reason="+takeover_by_partner_not_possible_reason
    if takeover_of_partner_not_possible_reason != None:
        if flag is 0:
            url_path+="?takeover_of_partner_not_possible_reason="+takeover_of_partner_not_possible_reason
            flag=1
        else:
            url_path+="&takeover_of_partner_not_possible_reason="+takeover_of_partner_not_possible_reason
    if takeover_failure_reason != None:
        if flag is 0:
            url_path+="?takeover_failure_reason="+takeover_failure_reason
            flag=1
        else:
            url_path+="&takeover_failure_reason="+takeover_failure_reason
    if is_all_flash_optimized != None:
        if flag is 0:
            url_path+="?is_all_flash_optimized="+is_all_flash_optimized
            flag=1
        else:
            url_path+="&is_all_flash_optimized="+is_all_flash_optimized
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
    url_path+="nodes"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (partner_node_key != None) & (partner_node_key != key):
        payload['partner_node_key']=partner_node_key
    if (metro_cluster_dr_partner_node_key != None) & (metro_cluster_dr_partner_node_key != key):
        payload['metro_cluster_dr_partner_node_key']=metro_cluster_dr_partner_node_key
    if (metro_cluster_dr_operation_state != None) & (metro_cluster_dr_operation_state != key):
        payload['metro_cluster_dr_operation_state']=metro_cluster_dr_operation_state
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (version != None) & (version != key):
        payload['version']=version
    if (model != None) & (model != key):
        payload['model']=model
    if (uptime != None) & (uptime != key):
        payload['uptime']=uptime
    if (vendor != None) & (vendor != key):
        payload['vendor']=vendor
    if (location != None) & (location != key):
        payload['location']=location
    if (failover_state != None) & (failover_state != key):
        payload['failover_state']=failover_state
    if (cpu_processor_type != None) & (cpu_processor_type != key):
        payload['cpu_processor_type']=cpu_processor_type
    if (cpu_processor_id != None) & (cpu_processor_id != key):
        payload['cpu_processor_id']=cpu_processor_id
    if (number_of_processors != None) & (number_of_processors != key):
        payload['number_of_processors']=number_of_processors
    if (memory_size != None) & (memory_size != key):
        payload['memory_size']=memory_size
    if (product_type != None) & (product_type != key):
        payload['product_type']=product_type
    if (nvram_id != None) & (nvram_id != key):
        payload['nvram_id']=nvram_id
    if (cpu_firmware_release != None) & (cpu_firmware_release != key):
        payload['cpu_firmware_release']=cpu_firmware_release
    if (is_over_temperature != None) & (is_over_temperature != key):
        payload['is_over_temperature']=is_over_temperature
    if (failed_fan_count != None) & (failed_fan_count != key):
        payload['failed_fan_count']=failed_fan_count
    if (failed_power_supply_count != None) & (failed_power_supply_count != key):
        payload['failed_power_supply_count']=failed_power_supply_count
    if (nvram_battery_status != None) & (nvram_battery_status != key):
        payload['nvram_battery_status']=nvram_battery_status
    if (is_failover_enabled != None) & (is_failover_enabled != key):
        payload['is_failover_enabled']=is_failover_enabled
    if (is_take_over_possible != None) & (is_take_over_possible != key):
        payload['is_take_over_possible']=is_take_over_possible
    if (partner_firmware_state != None) & (partner_firmware_state != key):
        payload['partner_firmware_state']=partner_firmware_state
    if (local_firmware_state != None) & (local_firmware_state != key):
        payload['local_firmware_state']=local_firmware_state
    if (is_interconnect_up != None) & (is_interconnect_up != key):
        payload['is_interconnect_up']=is_interconnect_up
    if (interconnect_links != None) & (interconnect_links != key):
        payload['interconnect_links']=interconnect_links
    if (interconnect_type != None) & (interconnect_type != key):
        payload['interconnect_type']=interconnect_type
    if (version_generation != None) & (version_generation != key):
        payload['version_generation']=version_generation
    if (version_major != None) & (version_major != key):
        payload['version_major']=version_major
    if (version_minor != None) & (version_minor != key):
        payload['version_minor']=version_minor
    if (owner != None) & (owner != key):
        payload['owner']=owner
    if (is_node_healthy != None) & (is_node_healthy != key):
        payload['is_node_healthy']=is_node_healthy
    if (is_epsilon_node != None) & (is_epsilon_node != key):
        payload['is_epsilon_node']=is_epsilon_node
    if (env_failed_fan_message != None) & (env_failed_fan_message != key):
        payload['env_failed_fan_message']=env_failed_fan_message
    if (env_failed_power_supply_message != None) & (env_failed_power_supply_message != key):
        payload['env_failed_power_supply_message']=env_failed_power_supply_message
    if (give_back_state != None) & (give_back_state != key):
        payload['give_back_state']=give_back_state
    if (current_mode != None) & (current_mode != key):
        payload['current_mode']=current_mode
    if (takeover_by_partner_not_possible_reason != None) & (takeover_by_partner_not_possible_reason != key):
        payload['takeover_by_partner_not_possible_reason']=takeover_by_partner_not_possible_reason
    if (takeover_of_partner_not_possible_reason != None) & (takeover_of_partner_not_possible_reason != key):
        payload['takeover_of_partner_not_possible_reason']=takeover_of_partner_not_possible_reason
    if (takeover_failure_reason != None) & (takeover_failure_reason != key):
        payload['takeover_failure_reason']=takeover_failure_reason
    if (is_all_flash_optimized != None) & (is_all_flash_optimized != key):
        payload['is_all_flash_optimized']=is_all_flash_optimized
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
    url_path+="nodes/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (partner_node_key != None) & (partner_node_key != key):
        payload['partner_node_key']=partner_node_key
    if (metro_cluster_dr_partner_node_key != None) & (metro_cluster_dr_partner_node_key != key):
        payload['metro_cluster_dr_partner_node_key']=metro_cluster_dr_partner_node_key
    if (metro_cluster_dr_operation_state != None) & (metro_cluster_dr_operation_state != key):
        payload['metro_cluster_dr_operation_state']=metro_cluster_dr_operation_state
    if (serial_number != None) & (serial_number != key):
        payload['serial_number']=serial_number
    if (version != None) & (version != key):
        payload['version']=version
    if (model != None) & (model != key):
        payload['model']=model
    if (uptime != None) & (uptime != key):
        payload['uptime']=uptime
    if (vendor != None) & (vendor != key):
        payload['vendor']=vendor
    if (location != None) & (location != key):
        payload['location']=location
    if (failover_state != None) & (failover_state != key):
        payload['failover_state']=failover_state
    if (cpu_processor_type != None) & (cpu_processor_type != key):
        payload['cpu_processor_type']=cpu_processor_type
    if (cpu_processor_id != None) & (cpu_processor_id != key):
        payload['cpu_processor_id']=cpu_processor_id
    if (number_of_processors != None) & (number_of_processors != key):
        payload['number_of_processors']=number_of_processors
    if (memory_size != None) & (memory_size != key):
        payload['memory_size']=memory_size
    if (product_type != None) & (product_type != key):
        payload['product_type']=product_type
    if (nvram_id != None) & (nvram_id != key):
        payload['nvram_id']=nvram_id
    if (cpu_firmware_release != None) & (cpu_firmware_release != key):
        payload['cpu_firmware_release']=cpu_firmware_release
    if (is_over_temperature != None) & (is_over_temperature != key):
        payload['is_over_temperature']=is_over_temperature
    if (failed_fan_count != None) & (failed_fan_count != key):
        payload['failed_fan_count']=failed_fan_count
    if (failed_power_supply_count != None) & (failed_power_supply_count != key):
        payload['failed_power_supply_count']=failed_power_supply_count
    if (nvram_battery_status != None) & (nvram_battery_status != key):
        payload['nvram_battery_status']=nvram_battery_status
    if (is_failover_enabled != None) & (is_failover_enabled != key):
        payload['is_failover_enabled']=is_failover_enabled
    if (is_take_over_possible != None) & (is_take_over_possible != key):
        payload['is_take_over_possible']=is_take_over_possible
    if (partner_firmware_state != None) & (partner_firmware_state != key):
        payload['partner_firmware_state']=partner_firmware_state
    if (local_firmware_state != None) & (local_firmware_state != key):
        payload['local_firmware_state']=local_firmware_state
    if (is_interconnect_up != None) & (is_interconnect_up != key):
        payload['is_interconnect_up']=is_interconnect_up
    if (interconnect_links != None) & (interconnect_links != key):
        payload['interconnect_links']=interconnect_links
    if (interconnect_type != None) & (interconnect_type != key):
        payload['interconnect_type']=interconnect_type
    if (version_generation != None) & (version_generation != key):
        payload['version_generation']=version_generation
    if (version_major != None) & (version_major != key):
        payload['version_major']=version_major
    if (version_minor != None) & (version_minor != key):
        payload['version_minor']=version_minor
    if (owner != None) & (owner != key):
        payload['owner']=owner
    if (is_node_healthy != None) & (is_node_healthy != key):
        payload['is_node_healthy']=is_node_healthy
    if (is_epsilon_node != None) & (is_epsilon_node != key):
        payload['is_epsilon_node']=is_epsilon_node
    if (env_failed_fan_message != None) & (env_failed_fan_message != key):
        payload['env_failed_fan_message']=env_failed_fan_message
    if (env_failed_power_supply_message != None) & (env_failed_power_supply_message != key):
        payload['env_failed_power_supply_message']=env_failed_power_supply_message
    if (give_back_state != None) & (give_back_state != key):
        payload['give_back_state']=give_back_state
    if (current_mode != None) & (current_mode != key):
        payload['current_mode']=current_mode
    if (takeover_by_partner_not_possible_reason != None) & (takeover_by_partner_not_possible_reason != key):
        payload['takeover_by_partner_not_possible_reason']=takeover_by_partner_not_possible_reason
    if (takeover_of_partner_not_possible_reason != None) & (takeover_of_partner_not_possible_reason != key):
        payload['takeover_of_partner_not_possible_reason']=takeover_of_partner_not_possible_reason
    if (takeover_failure_reason != None) & (takeover_failure_reason != key):
        payload['takeover_failure_reason']=takeover_failure_reason
    if (is_all_flash_optimized != None) & (is_all_flash_optimized != key):
        payload['is_all_flash_optimized']=is_all_flash_optimized
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
    url_path+="nodes/"

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
                "cluster_key" : {"required": False, "type": "str"},
                "partner_node_key" : {"required": False, "type": "str"},
                "metro_cluster_dr_partner_node_key" : {"required": False, "type": "str"},
                "metro_cluster_dr_operation_state" : {"required": False, "type": "str"},
                "serial_number" : {"required": False, "type": "str"},
                "version" : {"required": False, "type": "str"},
                "model" : {"required": False, "type": "str"},
                "uptime" : {"required": False, "type": "str"},
                "vendor" : {"required": False, "type": "str"},
                "location" : {"required": False, "type": "str"},
                "failover_state" : {"required": False, "type": "str"},
                "cpu_processor_type" : {"required": False, "type": "str"},
                "cpu_processor_id" : {"required": False, "type": "str"},
                "number_of_processors" : {"required": False, "type": "str"},
                "memory_size" : {"required": False, "type": "str"},
                "product_type" : {"required": False, "type": "str"},
                "nvram_id" : {"required": False, "type": "str"},
                "cpu_firmware_release" : {"required": False, "type": "str"},
                "is_over_temperature" : {"required": False, "type": "str"},
                "failed_fan_count" : {"required": False, "type": "str"},
                "failed_power_supply_count" : {"required": False, "type": "str"},
                "nvram_battery_status" : {"required": False, "type": "str"},
                "is_failover_enabled" : {"required": False, "type": "str"},
                "is_take_over_possible" : {"required": False, "type": "str"},
                "partner_firmware_state" : {"required": False, "type": "str"},
                "local_firmware_state" : {"required": False, "type": "str"},
                "is_interconnect_up" : {"required": False, "type": "str"},
                "interconnect_links" : {"required": False, "type": "str"},
                "interconnect_type" : {"required": False, "type": "str"},
                "version_generation" : {"required": False, "type": "str"},
                "version_major" : {"required": False, "type": "str"},
                "version_minor" : {"required": False, "type": "str"},
                "owner" : {"required": False, "type": "str"},
                "is_node_healthy" : {"required": False, "type": "str"},
                "is_epsilon_node" : {"required": False, "type": "str"},
                "env_failed_fan_message" : {"required": False, "type": "str"},
                "env_failed_power_supply_message" : {"required": False, "type": "str"},
                "give_back_state" : {"required": False, "type": "str"},
                "current_mode" : {"required": False, "type": "str"},
                "takeover_by_partner_not_possible_reason" : {"required": False, "type": "str"},
                "takeover_of_partner_not_possible_reason" : {"required": False, "type": "str"},
                "takeover_failure_reason" : {"required": False, "type": "str"},
                "is_all_flash_optimized" : {"required": False, "type": "str"},
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
        global partner_node_key
        partner_node_key = module.params["partner_node_key"]
        global metro_cluster_dr_partner_node_key
        metro_cluster_dr_partner_node_key = module.params["metro_cluster_dr_partner_node_key"]
        global metro_cluster_dr_operation_state
        metro_cluster_dr_operation_state = module.params["metro_cluster_dr_operation_state"]
        global serial_number
        serial_number = module.params["serial_number"]
        global version
        version = module.params["version"]
        global model
        model = module.params["model"]
        global uptime
        uptime = module.params["uptime"]
        global vendor
        vendor = module.params["vendor"]
        global location
        location = module.params["location"]
        global failover_state
        failover_state = module.params["failover_state"]
        global cpu_processor_type
        cpu_processor_type = module.params["cpu_processor_type"]
        global cpu_processor_id
        cpu_processor_id = module.params["cpu_processor_id"]
        global number_of_processors
        number_of_processors = module.params["number_of_processors"]
        global memory_size
        memory_size = module.params["memory_size"]
        global product_type
        product_type = module.params["product_type"]
        global nvram_id
        nvram_id = module.params["nvram_id"]
        global cpu_firmware_release
        cpu_firmware_release = module.params["cpu_firmware_release"]
        global is_over_temperature
        is_over_temperature = module.params["is_over_temperature"]
        global failed_fan_count
        failed_fan_count = module.params["failed_fan_count"]
        global failed_power_supply_count
        failed_power_supply_count = module.params["failed_power_supply_count"]
        global nvram_battery_status
        nvram_battery_status = module.params["nvram_battery_status"]
        global is_failover_enabled
        is_failover_enabled = module.params["is_failover_enabled"]
        global is_take_over_possible
        is_take_over_possible = module.params["is_take_over_possible"]
        global partner_firmware_state
        partner_firmware_state = module.params["partner_firmware_state"]
        global local_firmware_state
        local_firmware_state = module.params["local_firmware_state"]
        global is_interconnect_up
        is_interconnect_up = module.params["is_interconnect_up"]
        global interconnect_links
        interconnect_links = module.params["interconnect_links"]
        global interconnect_type
        interconnect_type = module.params["interconnect_type"]
        global version_generation
        version_generation = module.params["version_generation"]
        global version_major
        version_major = module.params["version_major"]
        global version_minor
        version_minor = module.params["version_minor"]
        global owner
        owner = module.params["owner"]
        global is_node_healthy
        is_node_healthy = module.params["is_node_healthy"]
        global is_epsilon_node
        is_epsilon_node = module.params["is_epsilon_node"]
        global env_failed_fan_message
        env_failed_fan_message = module.params["env_failed_fan_message"]
        global env_failed_power_supply_message
        env_failed_power_supply_message = module.params["env_failed_power_supply_message"]
        global give_back_state
        give_back_state = module.params["give_back_state"]
        global current_mode
        current_mode = module.params["current_mode"]
        global takeover_by_partner_not_possible_reason
        takeover_by_partner_not_possible_reason = module.params["takeover_by_partner_not_possible_reason"]
        global takeover_of_partner_not_possible_reason
        takeover_of_partner_not_possible_reason = module.params["takeover_of_partner_not_possible_reason"]
        global takeover_failure_reason
        takeover_failure_reason = module.params["takeover_failure_reason"]
        global is_all_flash_optimized
        is_all_flash_optimized = module.params["is_all_flash_optimized"]
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
