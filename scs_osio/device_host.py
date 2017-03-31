#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
  1: ./scs_osio/device_id.py
  2: ./scs_osio/api_auth.py
> 3: ./scs_osio/device_host.py
  4: ./scs_osio/project_host.py

Requires APIAuth and DeviceID documents.
Creates ClientAuth document.

command line example:
./scs_osio/device_host.py -v -u south-coast-science-test-user -l 50.819456, -0.128336 "BN2 1AF" -d "BB dev platform"
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.config.source import Source
from scs_core.osio.manager.device_manager import DeviceManager
from scs_core.sys.device_id import DeviceID

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device_host import CmdDeviceHost


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()


    device_id = DeviceID.load_from_host(Host)

    if device_id is None:
        print("DeviceID not available.", file=sys.stderr)
        exit()


    http_client = HTTPClient()

    manager = DeviceManager(http_client, api_auth.api_key)

    # check for existing registration...
    device = manager.find_for_name(api_auth.org_id, device_id.box_label())


    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDeviceHost()

    if not cmd.is_valid(device):
        cmd.print_help(sys.stderr)
        exit()

    if cmd.verbose:
        print(cmd, file=sys.stderr)
        print(api_auth, file=sys.stderr)
        print(device_id, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        if device:
            # find ClientAuth...
            client_auth = ClientAuth.load_from_host(Host)

            # update Device...
            update = Source.update(device, cmd.lat, cmd.lng, cmd.postcode, cmd.description)
            manager.update(api_auth.org_id, device.client_id, update)

            # find updated device...
            device = manager.find(api_auth.org_id, device.client_id)

        else:
            if not cmd.is_complete():
                print("User ID and location are required to create a device.", file=sys.stderr)
                exit()

            # create Device...
            device = Source.create(device_id, api_auth, cmd.lat, cmd.lng, cmd.postcode, cmd.description)
            device = manager.create(cmd.user_id, device)

            # create ClientAuth...
            client_auth = ClientAuth(cmd.user_id, device.client_id, device.password)
            client_auth.save(Host)

    else:
        # find ClientAuth...
        client_auth = ClientAuth.load_from_host(Host)

    if cmd.verbose:
        print(client_auth, file=sys.stderr)

    print(JSONify.dumps(device))
