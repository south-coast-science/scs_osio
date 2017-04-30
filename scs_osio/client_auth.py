#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
Use host_device instead.

command line example:
./client_auth.py -v -s southcoastscience-dev 5406 jtxSrK2e
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.client_auth import ClientAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_client_auth import CmdClientAuth


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdClientAuth()

    if cmd.verbose:
        print(cmd, file=sys.stderr)
        sys.stderr.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        auth = ClientAuth(cmd.user_id, cmd.client_id, cmd.client_password)
        auth.save(Host)

    else:
        # find self...
        auth = ClientAuth.load_from_host(Host)

    print(JSONify.dumps(auth))
