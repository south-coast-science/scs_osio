#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
  1: ./scs_osio/device_id.py
  2: ./scs_osio/api_auth.py
> 3: ./scs_osio/host_device.py
  4: ./scs_osio/host_project.py

Requires APIAuth and DeviceID documents.
Creates ClientAuth document.

command line examples:
./scs_osio/device.py -v -u south-coast-science-test-user -l 50.823130 -0.122922 "BN2 0DA" -d "test 1"
./scs_osio/device.py -v -u south-coast-science-test-user -l 50.819456, -0.128336 "BN2 1AF" -d "BB dev platform"
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.config.source import Source
from scs_core.osio.manager.device_manager import DeviceManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device import CmdDevice


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDevice()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()

    if cmd.verbose:
        print(api_auth, file=sys.stderr)


    http_client = HTTPClient()

    manager = DeviceManager(http_client, api_auth.api_key)

    # check for existing registration...
    device = manager.find(api_auth.org_id, cmd.client_id)

    if device is None:
        print("Device not found.", file=sys.stderr)
        exit()


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        # update Device...
        updated = Source.update(device, cmd.lat, cmd.lng, cmd.postcode, cmd.description)
        manager.update(api_auth.org_id, device.client_id, updated)

        # find updated device...
        device = manager.find(api_auth.org_id, device.client_id)

    print(JSONify.dumps(device))
