#!/usr/bin/env python3

"""
Created on 21 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line example:
./scs_osio/user.py -v -n "Mickey Mouse"
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_user import CmdUser


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUser()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    auth = APIAuth.load_from_host(Host)

    if auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        auth = APIAuth(cmd.org_id, cmd.api_key)
        auth.save(Host)

    else:
        # find self...
        auth = APIAuth.load_from_host(Host)

    print(JSONify.dumps(auth))
