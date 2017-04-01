#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
  1: ./scs_osio/device_id.py
> 2: ./scs_osio/api_auth.py
  3: ./scs_osio/device_host.py
  4: ./scs_osio/project_host.py

Creates APIAuth document.

command line example:
./scs_osio/api_auth.py -v -s south-coast-science-test 9fdfb841-3433-45b8-b223-3f5a283ceb8e
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_api_auth import CmdAPIAuth


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdAPIAuth()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        auth = APIAuth(cmd.org_id, cmd.api_key)
        auth.save(Host)

    else:
        # find self...
        auth = APIAuth.load_from_host(Host)

    print(JSONify.dumps(auth))
