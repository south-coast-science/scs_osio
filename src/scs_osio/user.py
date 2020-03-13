#!/usr/bin/env python3

"""
Created on 21 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and ClientAuth documents.

command line example:
./user.py -v -n "Mickey Mouse"
"""

import sys

from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.client.client_auth import ClientAuth
from scs_core.osio.data.user import User
from scs_core.osio.manager.user_manager import UserManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_user import CmdUser


# TODO: upgrade this, to take user_id explicitly

# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUser()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("user: %s" % cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load(Host)

    if api_auth is None:
        print("user: APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("user: %s" % api_auth, file=sys.stderr)

    # ClientAuth...
    client_auth = ClientAuth.load(Host)

    if client_auth is None:
        print("user: ClientAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("user: %s" % client_auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = UserManager(HTTPClient(False), api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    # find self...
    user = manager.find(client_auth.user_id)

    if user is None:
        print("user: User not found.", file=sys.stderr)
        exit(1)

    if cmd.set():
        name = user.name if cmd.name is None else cmd.name
        email = user.email if cmd.email is None else cmd.email
        password = user.password if cmd.password is None else cmd.password

        updated = User(None, name, email, password, None)

        manager.update(user.id, updated)

        user = manager.find(client_auth.user_id)

    print(JSONify.dumps(user))
