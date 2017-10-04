#!/usr/bin/env python3

"""
Created on 2 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
"""

import sys

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.manager.device_manager import DeviceManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------
# resources...

# APIAuth...
api_auth = APIAuth.load(Host)

if api_auth is None:
    print("APIAuth not available.", file=sys.stderr)
    exit(1)

print(api_auth)

# ClientAuth...
client_auth = ClientAuth.load(Host)

if client_auth is None:
    print("ClientAuth not available.", file=sys.stderr)
    exit(1)

print(client_auth)

# manager...
http_client = HTTPClient()

manager = DeviceManager(http_client, api_auth.api_key)

print(manager)
print("-")


# --------------------------------------------------------------------------------------------------------------------
# run...

print("find:")
device = manager.find(api_auth.org_id, client_auth.client_id)

print(device)
print("-")


print("find for name:")
device = manager.find_for_name(api_auth.org_id, device.name)

print(device)
print("-")


print("find for user:")
devices = manager.find_all_for_user(client_auth.user_id)

for device in devices:
    print(device)
print("-")


print("find for org:")
devices = manager.find_all_for_org(api_auth.org_id)

for device in devices:
    print(device)
print("-")

