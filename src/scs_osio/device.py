#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and SystemID documents.

Note: this script currently does not update device tags.

command line examples:
./device.py -v -u south-coast-science-test-user -l 50.823130 -0.122922 "BN2 0DF" -d "test 1"
./device.py -v -u south-coast-science-test-user -l 50.819456 -0.128336 "BN2 1AF" -d "BB dev platform"
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.config.project_source import ProjectSource
from scs_core.osio.manager.device_manager import DeviceManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device import CmdDevice


# TODO: ability to delete devices

# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDevice()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print(api_auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = DeviceManager(HTTPClient(), api_auth.api_key)

    # check for existing registration...
    device = manager.find(api_auth.org_id, cmd.client_id)

    if device is None:
        print("Device not found.", file=sys.stderr)
        exit(1)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        # update Device...
        updated = ProjectSource.update(device, cmd.lat, cmd.lng, cmd.postcode, cmd.description)
        manager.update(api_auth.org_id, device.client_id, updated)

        # find updated device...
        device = manager.find(api_auth.org_id, device.client_id)

    print(JSONify.dumps(device))
