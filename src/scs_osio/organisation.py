#!/usr/bin/env python3

"""
Created on 14 May 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line examples:
./organisation.py -v -o test-org-1 -n "Test Org 1" -w www.southcoastscience.com \
-d "a test organisation" -e test1@southcoastscience.com
"""

import sys

from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.data.organisation import Organisation
from scs_core.osio.manager.organisation_manager import OrganisationManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_organisation import CmdOrganisation


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdOrganisation()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print(cmd, file=sys.stderr)
        sys.stderr.flush()


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
    manager = OrganisationManager(HTTPClient(), api_auth.api_key)

    # check for existing registration...
    org = manager.find(cmd.org_id)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        if org:
            name = org.name if cmd.name is None else cmd.name
            website = org.website if cmd.website is None else cmd.website
            description = org.description if cmd.description is None else cmd.description
            email = org.email if cmd.email is None else cmd.email

            # update Organisation...
            updated = Organisation(None, name, website, description, email)
            manager.update(org.id, updated)

        else:
            if not cmd.is_complete():
                print("The organisation does not exist, and not all fields required for its creation were provided.",
                      file=sys.stderr)
                cmd.print_help(sys.stderr)
                exit(1)

            # create Organisation...
            org = Organisation(None, cmd.name, cmd.website, cmd.description, cmd.email)
            manager.create(org)

        org = manager.find(org.id)


    print(JSONify.dumps(org))
