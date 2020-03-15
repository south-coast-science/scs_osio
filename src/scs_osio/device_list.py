#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and ClientAuth documents.

command line example:
./device_list.py -u -v
"""

import sys

from scs_core.client.http_client import HTTPClient

from scs_core.data.json import JSONify
from scs_core.osio.manager.device_manager import DeviceManager
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device_list import CmdDeviceList


# TODO: add ability to specify the used ID

# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDeviceList()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("device_list: %s" % cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load(Host)

    if api_auth is None:
        print("device_list: APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("device_list: %s" % api_auth, file=sys.stderr)

    # ClientAuth...
    client_auth = ClientAuth.load(Host)

    if client_auth is None:
        print("device_list: ClientAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("device_list: %s" % client_auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = DeviceManager(HTTPClient(False), api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.org:
        devices = manager.find_all_for_org(api_auth.org_id)
    else:
        devices = manager.find_all_for_user(client_auth.user_id)

    for device in devices:
        print(JSONify.dumps(device))

    if cmd.verbose:
        print("device_list: total: %d" % len(devices), file=sys.stderr)
