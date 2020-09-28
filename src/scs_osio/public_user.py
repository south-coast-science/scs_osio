#!/usr/bin/env python3

"""
Created on 30 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line example:
./public_user.py -v south-coast-science-test-user
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.manager.user_manager import UserManager

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_public_user import CmdPublicUser


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdPublicUser()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("public_user: %s" % cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load(Host)

    if api_auth is None:
        print("public_user: APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("public_user: %s" % api_auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = UserManager(api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    # find self...
    user = manager.find_public(cmd.user_id)

    if user:
        print(JSONify.dumps(user))
