#!/usr/bin/env python3

"""
Created on 2 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example:
"""

import sys

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.manager.topic_manager import TopicManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------
# resource...

api_auth = APIAuth.load_from_host(Host)

if api_auth is None:
    print("APIAuth not available.", file=sys.stderr)
    exit()

print(api_auth)


client_auth = ClientAuth.load_from_host(Host)

if client_auth is None:
    print("ClientAuth not available.", file=sys.stderr)
    exit()

print(client_auth)


http_client = HTTPClient()

manager = TopicManager(http_client, api_auth.api_key)

print(manager)
print("-")


# --------------------------------------------------------------------------------------------------------------------
# run...

print("find:")
topic = manager.find('/orgs/south-coast-science-dev/development/loc/2/gases')

print(topic)
print("-")


print("find for org:")
topics = manager.find_for_org(api_auth.org_id)

for topic in topics:
    print(topic)
print("-")

