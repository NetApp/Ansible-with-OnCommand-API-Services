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

    url_path+="storage-vms"

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
    if network_ip_space_key != None:
        if flag is 0:
            url_path+="?network_ip_space_key="+network_ip_space_key
            flag=1
        else:
            url_path+="&network_ip_space_key="+network_ip_space_key
    if qos_policy_group_key != None:
        if flag is 0:
            url_path+="?qos_policy_group_key="+qos_policy_group_key
            flag=1
        else:
            url_path+="&qos_policy_group_key="+qos_policy_group_key
    if state != None:
        if flag is 0:
            url_path+="?state="+state
            flag=1
        else:
            url_path+="&state="+state
    if operational_state != None:
        if flag is 0:
            url_path+="?operational_state="+operational_state
            flag=1
        else:
            url_path+="&operational_state="+operational_state
    if type != None:
        if flag is 0:
            url_path+="?type="+type
            flag=1
        else:
            url_path+="&type="+type
    if subtype != None:
        if flag is 0:
            url_path+="?subtype="+subtype
            flag=1
        else:
            url_path+="&subtype="+subtype
    if allowed_protocols != None:
        if flag is 0:
            url_path+="?allowed_protocols="+allowed_protocols
            flag=1
        else:
            url_path+="&allowed_protocols="+allowed_protocols
    if disallowed_protocols != None:
        if flag is 0:
            url_path+="?disallowed_protocols="+disallowed_protocols
            flag=1
        else:
            url_path+="&disallowed_protocols="+disallowed_protocols
    if is_config_locked_for_changes != None:
        if flag is 0:
            url_path+="?is_config_locked_for_changes="+is_config_locked_for_changes
            flag=1
        else:
            url_path+="&is_config_locked_for_changes="+is_config_locked_for_changes
    if nfs_enabled != None:
        if flag is 0:
            url_path+="?nfs_enabled="+nfs_enabled
            flag=1
        else:
            url_path+="&nfs_enabled="+nfs_enabled
    if nfs_v2supported != None:
        if flag is 0:
            url_path+="?nfs_v2supported="+nfs_v2supported
            flag=1
        else:
            url_path+="&nfs_v2supported="+nfs_v2supported
    if nfs_v3supported != None:
        if flag is 0:
            url_path+="?nfs_v3supported="+nfs_v3supported
            flag=1
        else:
            url_path+="&nfs_v3supported="+nfs_v3supported
    if nfs_v4supported != None:
        if flag is 0:
            url_path+="?nfs_v4supported="+nfs_v4supported
            flag=1
        else:
            url_path+="&nfs_v4supported="+nfs_v4supported
    if nfs_v41supported != None:
        if flag is 0:
            url_path+="?nfs_v41supported="+nfs_v41supported
            flag=1
        else:
            url_path+="&nfs_v41supported="+nfs_v41supported
    if nfs_v41pnfs_enabled != None:
        if flag is 0:
            url_path+="?nfs_v41pnfs_enabled="+nfs_v41pnfs_enabled
            flag=1
        else:
            url_path+="&nfs_v41pnfs_enabled="+nfs_v41pnfs_enabled
    if nfs41acl_enabled != None:
        if flag is 0:
            url_path+="?nfs41acl_enabled="+nfs41acl_enabled
            flag=1
        else:
            url_path+="&nfs41acl_enabled="+nfs41acl_enabled
    if nfs_v4read_delegation_enabled != None:
        if flag is 0:
            url_path+="?nfs_v4read_delegation_enabled="+nfs_v4read_delegation_enabled
            flag=1
        else:
            url_path+="&nfs_v4read_delegation_enabled="+nfs_v4read_delegation_enabled
    if nfs_v4write_delegation_enabled != None:
        if flag is 0:
            url_path+="?nfs_v4write_delegation_enabled="+nfs_v4write_delegation_enabled
            flag=1
        else:
            url_path+="&nfs_v4write_delegation_enabled="+nfs_v4write_delegation_enabled
    if nfs_v4migration_enabled != None:
        if flag is 0:
            url_path+="?nfs_v4migration_enabled="+nfs_v4migration_enabled
            flag=1
        else:
            url_path+="&nfs_v4migration_enabled="+nfs_v4migration_enabled
    if nfs_v4referrals_enabled != None:
        if flag is 0:
            url_path+="?nfs_v4referrals_enabled="+nfs_v4referrals_enabled
            flag=1
        else:
            url_path+="&nfs_v4referrals_enabled="+nfs_v4referrals_enabled
    if nfs_v41migration_enabled != None:
        if flag is 0:
            url_path+="?nfs_v41migration_enabled="+nfs_v41migration_enabled
            flag=1
        else:
            url_path+="&nfs_v41migration_enabled="+nfs_v41migration_enabled
    if nfs_v41referrals_enabled != None:
        if flag is 0:
            url_path+="?nfs_v41referrals_enabled="+nfs_v41referrals_enabled
            flag=1
        else:
            url_path+="&nfs_v41referrals_enabled="+nfs_v41referrals_enabled
    if cifs_enabled != None:
        if flag is 0:
            url_path+="?cifs_enabled="+cifs_enabled
            flag=1
        else:
            url_path+="&cifs_enabled="+cifs_enabled
    if cifs_server != None:
        if flag is 0:
            url_path+="?cifs_server="+cifs_server
            flag=1
        else:
            url_path+="&cifs_server="+cifs_server
    if cifs_authentication_style != None:
        if flag is 0:
            url_path+="?cifs_authentication_style="+cifs_authentication_style
            flag=1
        else:
            url_path+="&cifs_authentication_style="+cifs_authentication_style
    if cifs_domain != None:
        if flag is 0:
            url_path+="?cifs_domain="+cifs_domain
            flag=1
        else:
            url_path+="&cifs_domain="+cifs_domain
    if export_policy_enabled != None:
        if flag is 0:
            url_path+="?export_policy_enabled="+export_policy_enabled
            flag=1
        else:
            url_path+="&export_policy_enabled="+export_policy_enabled
    if default_unix_user != None:
        if flag is 0:
            url_path+="?default_unix_user="+default_unix_user
            flag=1
        else:
            url_path+="&default_unix_user="+default_unix_user
    if default_unix_group != None:
        if flag is 0:
            url_path+="?default_unix_group="+default_unix_group
            flag=1
        else:
            url_path+="&default_unix_group="+default_unix_group
    if iscsi_enabled != None:
        if flag is 0:
            url_path+="?iscsi_enabled="+iscsi_enabled
            flag=1
        else:
            url_path+="&iscsi_enabled="+iscsi_enabled
    if iscsi_node_name != None:
        if flag is 0:
            url_path+="?iscsi_node_name="+iscsi_node_name
            flag=1
        else:
            url_path+="&iscsi_node_name="+iscsi_node_name
    if iscsi_alias_name != None:
        if flag is 0:
            url_path+="?iscsi_alias_name="+iscsi_alias_name
            flag=1
        else:
            url_path+="&iscsi_alias_name="+iscsi_alias_name
    if fcp_enabled != None:
        if flag is 0:
            url_path+="?fcp_enabled="+fcp_enabled
            flag=1
        else:
            url_path+="&fcp_enabled="+fcp_enabled
    if fcp_node_name != None:
        if flag is 0:
            url_path+="?fcp_node_name="+fcp_node_name
            flag=1
        else:
            url_path+="&fcp_node_name="+fcp_node_name
    if nis_enabled != None:
        if flag is 0:
            url_path+="?nis_enabled="+nis_enabled
            flag=1
        else:
            url_path+="&nis_enabled="+nis_enabled
    if active_nis_domain_name != None:
        if flag is 0:
            url_path+="?active_nis_domain_name="+active_nis_domain_name
            flag=1
        else:
            url_path+="&active_nis_domain_name="+active_nis_domain_name
    if active_nis_servers != None:
        if flag is 0:
            url_path+="?active_nis_servers="+active_nis_servers
            flag=1
        else:
            url_path+="&active_nis_servers="+active_nis_servers
    if dns_enabled != None:
        if flag is 0:
            url_path+="?dns_enabled="+dns_enabled
            flag=1
        else:
            url_path+="&dns_enabled="+dns_enabled
    if dns_servers != None:
        if flag is 0:
            url_path+="?dns_servers="+dns_servers
            flag=1
        else:
            url_path+="&dns_servers="+dns_servers
    if dns_domain_names != None:
        if flag is 0:
            url_path+="?dns_domain_names="+dns_domain_names
            flag=1
        else:
            url_path+="&dns_domain_names="+dns_domain_names
    if maximum_volumes != None:
        if flag is 0:
            url_path+="?maximum_volumes="+maximum_volumes
            flag=1
        else:
            url_path+="&maximum_volumes="+maximum_volumes
    if language != None:
        if flag is 0:
            url_path+="?language="+language
            flag=1
        else:
            url_path+="&language="+language
    if name_server_switch != None:
        if flag is 0:
            url_path+="?name_server_switch="+name_server_switch
            flag=1
        else:
            url_path+="&name_server_switch="+name_server_switch
    if volume_bytes_used != None:
        if flag is 0:
            url_path+="?volume_bytes_used="+volume_bytes_used
            flag=1
        else:
            url_path+="&volume_bytes_used="+volume_bytes_used
    if volume_bytes_avail != None:
        if flag is 0:
            url_path+="?volume_bytes_avail="+volume_bytes_avail
            flag=1
        else:
            url_path+="&volume_bytes_avail="+volume_bytes_avail
    if volume_bytes_total != None:
        if flag is 0:
            url_path+="?volume_bytes_total="+volume_bytes_total
            flag=1
        else:
            url_path+="&volume_bytes_total="+volume_bytes_total
    if ldap_client_enabled != None:
        if flag is 0:
            url_path+="?ldap_client_enabled="+ldap_client_enabled
            flag=1
        else:
            url_path+="&ldap_client_enabled="+ldap_client_enabled
    if is_kerberos_enabled != None:
        if flag is 0:
            url_path+="?is_kerberos_enabled="+is_kerberos_enabled
            flag=1
        else:
            url_path+="&is_kerberos_enabled="+is_kerberos_enabled
    if root_volume_name != None:
        if flag is 0:
            url_path+="?root_volume_name="+root_volume_name
            flag=1
        else:
            url_path+="&root_volume_name="+root_volume_name
    if aggregate_key != None:
        if flag is 0:
            url_path+="?aggregate_key="+aggregate_key
            flag=1
        else:
            url_path+="&aggregate_key="+aggregate_key
    if root_volume_security_style != None:
        if flag is 0:
            url_path+="?root_volume_security_style="+root_volume_security_style
            flag=1
        else:
            url_path+="&root_volume_security_style="+root_volume_security_style
    if snapshot_policy_key != None:
        if flag is 0:
            url_path+="?snapshot_policy_key="+snapshot_policy_key
            flag=1
        else:
            url_path+="&snapshot_policy_key="+snapshot_policy_key
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
    url_path+="storage-vms"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (state != None) & (state != key):
        payload['state']=state
    if (operational_state != None) & (operational_state != key):
        payload['operational_state']=operational_state
    if (type != None) & (type != key):
        payload['type']=type
    if (subtype != None) & (subtype != key):
        payload['subtype']=subtype
    if (allowed_protocols != None) & (allowed_protocols != key):
        payload['allowed_protocols']=allowed_protocols
    if (disallowed_protocols != None) & (disallowed_protocols != key):
        payload['disallowed_protocols']=disallowed_protocols
    if (is_config_locked_for_changes != None) & (is_config_locked_for_changes != key):
        payload['is_config_locked_for_changes']=is_config_locked_for_changes
    if (nfs_enabled != None) & (nfs_enabled != key):
        payload['nfs_enabled']=nfs_enabled
    if (nfs_v2supported != None) & (nfs_v2supported != key):
        payload['nfs_v2supported']=nfs_v2supported
    if (nfs_v3supported != None) & (nfs_v3supported != key):
        payload['nfs_v3supported']=nfs_v3supported
    if (nfs_v4supported != None) & (nfs_v4supported != key):
        payload['nfs_v4supported']=nfs_v4supported
    if (nfs_v41supported != None) & (nfs_v41supported != key):
        payload['nfs_v41supported']=nfs_v41supported
    if (nfs_v41pnfs_enabled != None) & (nfs_v41pnfs_enabled != key):
        payload['nfs_v41pnfs_enabled']=nfs_v41pnfs_enabled
    if (nfs41acl_enabled != None) & (nfs41acl_enabled != key):
        payload['nfs41acl_enabled']=nfs41acl_enabled
    if (nfs_v4read_delegation_enabled != None) & (nfs_v4read_delegation_enabled != key):
        payload['nfs_v4read_delegation_enabled']=nfs_v4read_delegation_enabled
    if (nfs_v4write_delegation_enabled != None) & (nfs_v4write_delegation_enabled != key):
        payload['nfs_v4write_delegation_enabled']=nfs_v4write_delegation_enabled
    if (nfs_v4migration_enabled != None) & (nfs_v4migration_enabled != key):
        payload['nfs_v4migration_enabled']=nfs_v4migration_enabled
    if (nfs_v4referrals_enabled != None) & (nfs_v4referrals_enabled != key):
        payload['nfs_v4referrals_enabled']=nfs_v4referrals_enabled
    if (nfs_v41migration_enabled != None) & (nfs_v41migration_enabled != key):
        payload['nfs_v41migration_enabled']=nfs_v41migration_enabled
    if (nfs_v41referrals_enabled != None) & (nfs_v41referrals_enabled != key):
        payload['nfs_v41referrals_enabled']=nfs_v41referrals_enabled
    if (cifs_enabled != None) & (cifs_enabled != key):
        payload['cifs_enabled']=cifs_enabled
    if (cifs_server != None) & (cifs_server != key):
        payload['cifs_server']=cifs_server
    if (cifs_authentication_style != None) & (cifs_authentication_style != key):
        payload['cifs_authentication_style']=cifs_authentication_style
    if (cifs_domain != None) & (cifs_domain != key):
        payload['cifs_domain']=cifs_domain
    if (export_policy_enabled != None) & (export_policy_enabled != key):
        payload['export_policy_enabled']=export_policy_enabled
    if (default_unix_user != None) & (default_unix_user != key):
        payload['default_unix_user']=default_unix_user
    if (default_unix_group != None) & (default_unix_group != key):
        payload['default_unix_group']=default_unix_group
    if (iscsi_enabled != None) & (iscsi_enabled != key):
        payload['iscsi_enabled']=iscsi_enabled
    if (iscsi_node_name != None) & (iscsi_node_name != key):
        payload['iscsi_node_name']=iscsi_node_name
    if (iscsi_alias_name != None) & (iscsi_alias_name != key):
        payload['iscsi_alias_name']=iscsi_alias_name
    if (fcp_enabled != None) & (fcp_enabled != key):
        payload['fcp_enabled']=fcp_enabled
    if (fcp_node_name != None) & (fcp_node_name != key):
        payload['fcp_node_name']=fcp_node_name
    if (nis_enabled != None) & (nis_enabled != key):
        payload['nis_enabled']=nis_enabled
    if (active_nis_domain_name != None) & (active_nis_domain_name != key):
        payload['active_nis_domain_name']=active_nis_domain_name
    if (active_nis_servers != None) & (active_nis_servers != key):
        payload['active_nis_servers']=active_nis_servers
    if (dns_enabled != None) & (dns_enabled != key):
        payload['dns_enabled']=dns_enabled
    if (dns_servers != None) & (dns_servers != key):
        payload['dns_servers']=dns_servers
    if (dns_domain_names != None) & (dns_domain_names != key):
        payload['dns_domain_names']=dns_domain_names
    if (maximum_volumes != None) & (maximum_volumes != key):
        payload['maximum_volumes']=maximum_volumes
    if (language != None) & (language != key):
        payload['language']=language
    if (name_server_switch != None) & (name_server_switch != key):
        payload['name_server_switch']=name_server_switch
    if (volume_bytes_used != None) & (volume_bytes_used != key):
        payload['volume_bytes_used']=volume_bytes_used
    if (volume_bytes_avail != None) & (volume_bytes_avail != key):
        payload['volume_bytes_avail']=volume_bytes_avail
    if (volume_bytes_total != None) & (volume_bytes_total != key):
        payload['volume_bytes_total']=volume_bytes_total
    if (ldap_client_enabled != None) & (ldap_client_enabled != key):
        payload['ldap_client_enabled']=ldap_client_enabled
    if (is_kerberos_enabled != None) & (is_kerberos_enabled != key):
        payload['is_kerberos_enabled']=is_kerberos_enabled
    if (root_volume_name != None) & (root_volume_name != key):
        payload['root_volume_name']=root_volume_name
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (root_volume_security_style != None) & (root_volume_security_style != key):
        payload['root_volume_security_style']=root_volume_security_style
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
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
    url_path+="storage-vms/"

    payload={}
    if (key != None) & (key != key):
        payload['key']=key
    if (name != None) & (name != key):
        payload['name']=name
    if (cluster_key != None) & (cluster_key != key):
        payload['cluster_key']=cluster_key
    if (network_ip_space_key != None) & (network_ip_space_key != key):
        payload['network_ip_space_key']=network_ip_space_key
    if (qos_policy_group_key != None) & (qos_policy_group_key != key):
        payload['qos_policy_group_key']=qos_policy_group_key
    if (state != None) & (state != key):
        payload['state']=state
    if (operational_state != None) & (operational_state != key):
        payload['operational_state']=operational_state
    if (type != None) & (type != key):
        payload['type']=type
    if (subtype != None) & (subtype != key):
        payload['subtype']=subtype
    if (allowed_protocols != None) & (allowed_protocols != key):
        payload['allowed_protocols']=allowed_protocols
    if (disallowed_protocols != None) & (disallowed_protocols != key):
        payload['disallowed_protocols']=disallowed_protocols
    if (is_config_locked_for_changes != None) & (is_config_locked_for_changes != key):
        payload['is_config_locked_for_changes']=is_config_locked_for_changes
    if (nfs_enabled != None) & (nfs_enabled != key):
        payload['nfs_enabled']=nfs_enabled
    if (nfs_v2supported != None) & (nfs_v2supported != key):
        payload['nfs_v2supported']=nfs_v2supported
    if (nfs_v3supported != None) & (nfs_v3supported != key):
        payload['nfs_v3supported']=nfs_v3supported
    if (nfs_v4supported != None) & (nfs_v4supported != key):
        payload['nfs_v4supported']=nfs_v4supported
    if (nfs_v41supported != None) & (nfs_v41supported != key):
        payload['nfs_v41supported']=nfs_v41supported
    if (nfs_v41pnfs_enabled != None) & (nfs_v41pnfs_enabled != key):
        payload['nfs_v41pnfs_enabled']=nfs_v41pnfs_enabled
    if (nfs41acl_enabled != None) & (nfs41acl_enabled != key):
        payload['nfs41acl_enabled']=nfs41acl_enabled
    if (nfs_v4read_delegation_enabled != None) & (nfs_v4read_delegation_enabled != key):
        payload['nfs_v4read_delegation_enabled']=nfs_v4read_delegation_enabled
    if (nfs_v4write_delegation_enabled != None) & (nfs_v4write_delegation_enabled != key):
        payload['nfs_v4write_delegation_enabled']=nfs_v4write_delegation_enabled
    if (nfs_v4migration_enabled != None) & (nfs_v4migration_enabled != key):
        payload['nfs_v4migration_enabled']=nfs_v4migration_enabled
    if (nfs_v4referrals_enabled != None) & (nfs_v4referrals_enabled != key):
        payload['nfs_v4referrals_enabled']=nfs_v4referrals_enabled
    if (nfs_v41migration_enabled != None) & (nfs_v41migration_enabled != key):
        payload['nfs_v41migration_enabled']=nfs_v41migration_enabled
    if (nfs_v41referrals_enabled != None) & (nfs_v41referrals_enabled != key):
        payload['nfs_v41referrals_enabled']=nfs_v41referrals_enabled
    if (cifs_enabled != None) & (cifs_enabled != key):
        payload['cifs_enabled']=cifs_enabled
    if (cifs_server != None) & (cifs_server != key):
        payload['cifs_server']=cifs_server
    if (cifs_authentication_style != None) & (cifs_authentication_style != key):
        payload['cifs_authentication_style']=cifs_authentication_style
    if (cifs_domain != None) & (cifs_domain != key):
        payload['cifs_domain']=cifs_domain
    if (export_policy_enabled != None) & (export_policy_enabled != key):
        payload['export_policy_enabled']=export_policy_enabled
    if (default_unix_user != None) & (default_unix_user != key):
        payload['default_unix_user']=default_unix_user
    if (default_unix_group != None) & (default_unix_group != key):
        payload['default_unix_group']=default_unix_group
    if (iscsi_enabled != None) & (iscsi_enabled != key):
        payload['iscsi_enabled']=iscsi_enabled
    if (iscsi_node_name != None) & (iscsi_node_name != key):
        payload['iscsi_node_name']=iscsi_node_name
    if (iscsi_alias_name != None) & (iscsi_alias_name != key):
        payload['iscsi_alias_name']=iscsi_alias_name
    if (fcp_enabled != None) & (fcp_enabled != key):
        payload['fcp_enabled']=fcp_enabled
    if (fcp_node_name != None) & (fcp_node_name != key):
        payload['fcp_node_name']=fcp_node_name
    if (nis_enabled != None) & (nis_enabled != key):
        payload['nis_enabled']=nis_enabled
    if (active_nis_domain_name != None) & (active_nis_domain_name != key):
        payload['active_nis_domain_name']=active_nis_domain_name
    if (active_nis_servers != None) & (active_nis_servers != key):
        payload['active_nis_servers']=active_nis_servers
    if (dns_enabled != None) & (dns_enabled != key):
        payload['dns_enabled']=dns_enabled
    if (dns_servers != None) & (dns_servers != key):
        payload['dns_servers']=dns_servers
    if (dns_domain_names != None) & (dns_domain_names != key):
        payload['dns_domain_names']=dns_domain_names
    if (maximum_volumes != None) & (maximum_volumes != key):
        payload['maximum_volumes']=maximum_volumes
    if (language != None) & (language != key):
        payload['language']=language
    if (name_server_switch != None) & (name_server_switch != key):
        payload['name_server_switch']=name_server_switch
    if (volume_bytes_used != None) & (volume_bytes_used != key):
        payload['volume_bytes_used']=volume_bytes_used
    if (volume_bytes_avail != None) & (volume_bytes_avail != key):
        payload['volume_bytes_avail']=volume_bytes_avail
    if (volume_bytes_total != None) & (volume_bytes_total != key):
        payload['volume_bytes_total']=volume_bytes_total
    if (ldap_client_enabled != None) & (ldap_client_enabled != key):
        payload['ldap_client_enabled']=ldap_client_enabled
    if (is_kerberos_enabled != None) & (is_kerberos_enabled != key):
        payload['is_kerberos_enabled']=is_kerberos_enabled
    if (root_volume_name != None) & (root_volume_name != key):
        payload['root_volume_name']=root_volume_name
    if (aggregate_key != None) & (aggregate_key != key):
        payload['aggregate_key']=aggregate_key
    if (root_volume_security_style != None) & (root_volume_security_style != key):
        payload['root_volume_security_style']=root_volume_security_style
    if (snapshot_policy_key != None) & (snapshot_policy_key != key):
        payload['snapshot_policy_key']=snapshot_policy_key
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
    url_path+="storage-vms/"

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
                "network_ip_space_key" : {"required": False, "type": "str"},
                "qos_policy_group_key" : {"required": False, "type": "str"},
                "state" : {"required": False, "type": "str"},
                "operational_state" : {"required": False, "type": "str"},
                "type" : {"required": False, "type": "str"},
                "subtype" : {"required": False, "type": "str"},
                "allowed_protocols" : {"required": False, "type": "str"},
                "disallowed_protocols" : {"required": False, "type": "str"},
                "is_config_locked_for_changes" : {"required": False, "type": "str"},
                "nfs_enabled" : {"required": False, "type": "str"},
                "nfs_v2supported" : {"required": False, "type": "str"},
                "nfs_v3supported" : {"required": False, "type": "str"},
                "nfs_v4supported" : {"required": False, "type": "str"},
                "nfs_v41supported" : {"required": False, "type": "str"},
                "nfs_v41pnfs_enabled" : {"required": False, "type": "str"},
                "nfs41acl_enabled" : {"required": False, "type": "str"},
                "nfs_v4read_delegation_enabled" : {"required": False, "type": "str"},
                "nfs_v4write_delegation_enabled" : {"required": False, "type": "str"},
                "nfs_v4migration_enabled" : {"required": False, "type": "str"},
                "nfs_v4referrals_enabled" : {"required": False, "type": "str"},
                "nfs_v41migration_enabled" : {"required": False, "type": "str"},
                "nfs_v41referrals_enabled" : {"required": False, "type": "str"},
                "cifs_enabled" : {"required": False, "type": "str"},
                "cifs_server" : {"required": False, "type": "str"},
                "cifs_authentication_style" : {"required": False, "type": "str"},
                "cifs_domain" : {"required": False, "type": "str"},
                "export_policy_enabled" : {"required": False, "type": "str"},
                "default_unix_user" : {"required": False, "type": "str"},
                "default_unix_group" : {"required": False, "type": "str"},
                "iscsi_enabled" : {"required": False, "type": "str"},
                "iscsi_node_name" : {"required": False, "type": "str"},
                "iscsi_alias_name" : {"required": False, "type": "str"},
                "fcp_enabled" : {"required": False, "type": "str"},
                "fcp_node_name" : {"required": False, "type": "str"},
                "nis_enabled" : {"required": False, "type": "str"},
                "active_nis_domain_name" : {"required": False, "type": "str"},
                "active_nis_servers" : {"required": False, "type": "str"},
                "dns_enabled" : {"required": False, "type": "str"},
                "dns_servers" : {"required": False, "type": "str"},
                "dns_domain_names" : {"required": False, "type": "str"},
                "maximum_volumes" : {"required": False, "type": "str"},
                "language" : {"required": False, "type": "str"},
                "name_server_switch" : {"required": False, "type": "str"},
                "volume_bytes_used" : {"required": False, "type": "str"},
                "volume_bytes_avail" : {"required": False, "type": "str"},
                "volume_bytes_total" : {"required": False, "type": "str"},
                "ldap_client_enabled" : {"required": False, "type": "str"},
                "is_kerberos_enabled" : {"required": False, "type": "str"},
                "root_volume_name" : {"required": False, "type": "str"},
                "aggregate_key" : {"required": False, "type": "str"},
                "root_volume_security_style" : {"required": False, "type": "str"},
                "snapshot_policy_key" : {"required": False, "type": "str"},
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
        global network_ip_space_key
        network_ip_space_key = module.params["network_ip_space_key"]
        global qos_policy_group_key
        qos_policy_group_key = module.params["qos_policy_group_key"]
        global state
        state = module.params["state"]
        global operational_state
        operational_state = module.params["operational_state"]
        global type
        type = module.params["type"]
        global subtype
        subtype = module.params["subtype"]
        global allowed_protocols
        allowed_protocols = module.params["allowed_protocols"]
        global disallowed_protocols
        disallowed_protocols = module.params["disallowed_protocols"]
        global is_config_locked_for_changes
        is_config_locked_for_changes = module.params["is_config_locked_for_changes"]
        global nfs_enabled
        nfs_enabled = module.params["nfs_enabled"]
        global nfs_v2supported
        nfs_v2supported = module.params["nfs_v2supported"]
        global nfs_v3supported
        nfs_v3supported = module.params["nfs_v3supported"]
        global nfs_v4supported
        nfs_v4supported = module.params["nfs_v4supported"]
        global nfs_v41supported
        nfs_v41supported = module.params["nfs_v41supported"]
        global nfs_v41pnfs_enabled
        nfs_v41pnfs_enabled = module.params["nfs_v41pnfs_enabled"]
        global nfs41acl_enabled
        nfs41acl_enabled = module.params["nfs41acl_enabled"]
        global nfs_v4read_delegation_enabled
        nfs_v4read_delegation_enabled = module.params["nfs_v4read_delegation_enabled"]
        global nfs_v4write_delegation_enabled
        nfs_v4write_delegation_enabled = module.params["nfs_v4write_delegation_enabled"]
        global nfs_v4migration_enabled
        nfs_v4migration_enabled = module.params["nfs_v4migration_enabled"]
        global nfs_v4referrals_enabled
        nfs_v4referrals_enabled = module.params["nfs_v4referrals_enabled"]
        global nfs_v41migration_enabled
        nfs_v41migration_enabled = module.params["nfs_v41migration_enabled"]
        global nfs_v41referrals_enabled
        nfs_v41referrals_enabled = module.params["nfs_v41referrals_enabled"]
        global cifs_enabled
        cifs_enabled = module.params["cifs_enabled"]
        global cifs_server
        cifs_server = module.params["cifs_server"]
        global cifs_authentication_style
        cifs_authentication_style = module.params["cifs_authentication_style"]
        global cifs_domain
        cifs_domain = module.params["cifs_domain"]
        global export_policy_enabled
        export_policy_enabled = module.params["export_policy_enabled"]
        global default_unix_user
        default_unix_user = module.params["default_unix_user"]
        global default_unix_group
        default_unix_group = module.params["default_unix_group"]
        global iscsi_enabled
        iscsi_enabled = module.params["iscsi_enabled"]
        global iscsi_node_name
        iscsi_node_name = module.params["iscsi_node_name"]
        global iscsi_alias_name
        iscsi_alias_name = module.params["iscsi_alias_name"]
        global fcp_enabled
        fcp_enabled = module.params["fcp_enabled"]
        global fcp_node_name
        fcp_node_name = module.params["fcp_node_name"]
        global nis_enabled
        nis_enabled = module.params["nis_enabled"]
        global active_nis_domain_name
        active_nis_domain_name = module.params["active_nis_domain_name"]
        global active_nis_servers
        active_nis_servers = module.params["active_nis_servers"]
        global dns_enabled
        dns_enabled = module.params["dns_enabled"]
        global dns_servers
        dns_servers = module.params["dns_servers"]
        global dns_domain_names
        dns_domain_names = module.params["dns_domain_names"]
        global maximum_volumes
        maximum_volumes = module.params["maximum_volumes"]
        global language
        language = module.params["language"]
        global name_server_switch
        name_server_switch = module.params["name_server_switch"]
        global volume_bytes_used
        volume_bytes_used = module.params["volume_bytes_used"]
        global volume_bytes_avail
        volume_bytes_avail = module.params["volume_bytes_avail"]
        global volume_bytes_total
        volume_bytes_total = module.params["volume_bytes_total"]
        global ldap_client_enabled
        ldap_client_enabled = module.params["ldap_client_enabled"]
        global is_kerberos_enabled
        is_kerberos_enabled = module.params["is_kerberos_enabled"]
        global root_volume_name
        root_volume_name = module.params["root_volume_name"]
        global aggregate_key
        aggregate_key = module.params["aggregate_key"]
        global root_volume_security_style
        root_volume_security_style = module.params["root_volume_security_style"]
        global snapshot_policy_key
        snapshot_policy_key = module.params["snapshot_policy_key"]
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
