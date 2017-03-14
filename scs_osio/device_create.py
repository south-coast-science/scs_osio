#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
  1: ./scs_osio/device_id.py
  2: ./scs_osio/api_auth.py
> 3: ./scs_osio/device_create.py
  4: ./scs_osio/publication.py

Requires APIAuth and DeviceID documents.
Creates ClientAuth document.

command line examples:
./scs_osio/device_create.py -v -u south-coast-science-test-user -l 50.823130 -0.122922 "BN2 0DA" -d "test 1"
./scs_osio/device_create.py -v -u south-coast-science-test-user -l 50.819456, -0.128336 "BN2 1AF" -d "BB dev platform"
"""

import sys

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth

from scs_core.osio.config.source import Source
from scs_core.osio.manager.device_manager import DeviceManager
from scs_core.sys.device_id import DeviceID

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device_create import CmdDeviceCreate


# TODO: balk if there already is a device with the device ID (override with -f)

# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDeviceCreate()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.")
        exit()

    if cmd.verbose:
        print(api_auth, file=sys.stderr)


    device_id = DeviceID.load_from_host(Host)

    if device_id is None:
        print("DeviceID not available.")
        exit()

    if cmd.verbose:
        print(device_id, file=sys.stderr)


    http_client = HTTPClient()

    manager = DeviceManager(http_client, api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    # TODO: responses should be JSON...

    # create prototype...
    device = Source.device(device_id, api_auth, cmd.lat, cmd.lng, cmd.postcode, cmd.description)

    # create device...
    device = manager.create(cmd.user_id, device)
    print(device)

    # create client_auth...
    client_auth = ClientAuth(cmd.user_id, device.client_id, device.password)
    client_auth.save(Host)
    print(client_auth)
