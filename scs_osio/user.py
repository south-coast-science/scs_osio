#!/usr/bin/env python3

"""
Created on 21 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and ClientAuth documents.

command line example:
./scs_osio/user.py -v -n "Mickey Mouse"
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.manager.user_manager import UserManager

from scs_host.client.http_client import HTTPClient
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

    http_client = HTTPClient()


    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()

    if cmd.verbose:
        print(api_auth, file=sys.stderr)


    client_auth = ClientAuth.load_from_host(Host)

    if client_auth is None:
        print("ClientAuth not available.", file=sys.stderr)
        exit()

    if cmd.verbose:
        print(client_auth, file=sys.stderr)


    manager = UserManager(http_client, api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    user = manager.find(client_auth.user_id)

    if user is None:
        print("User not found.", file=sys.stderr)
        exit()

    # TODO: implement update

    # if cmd.set():
    #     auth = APIAuth(cmd.org_id, cmd.api_key)
    #     auth.save(Host)

    print(JSONify.dumps(user))
