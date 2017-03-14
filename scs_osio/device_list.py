#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and ClientAuth documents.

command line example:
./scs_osio/device_list.py -u -v
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.manager.device_manager import DeviceManager
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device_list import CmdDeviceList


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDeviceList()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    http_client = HTTPClient()


    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.")
        exit()

    if cmd.verbose:
        print(api_auth, file=sys.stderr)


    client_auth = ClientAuth.load_from_host(Host)

    if client_auth is None:
        print("ClientAuth not available.")
        exit()

    if cmd.verbose:
        print(client_auth, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    manager = DeviceManager(http_client, api_auth.api_key)

    if cmd.org:
        devices = manager.find_all_for_org(api_auth.org_id)
    else:
        devices = manager.find_all_for_user(client_auth.user_id)

    for device in devices:
        print(JSONify.dumps(device))
