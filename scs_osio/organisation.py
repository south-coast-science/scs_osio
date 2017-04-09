#!/usr/bin/env python3

"""
Created on 8 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

Note: this script does not create organisations. Arguably, it should.

command line examples:
./scs_osio/organisation.py -v -o test-org-1 -n "Test Org 1" -w www.southcoastscience.com \
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

    manager = OrganisationManager(http_client, api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    # find self...
    org = manager.find(api_auth.org_id)

    if cmd.set():
        if org is None:
            print("Organisation not found.", file=sys.stderr)
            exit()

        name = org.name if cmd.name is None else cmd.name
        website = org.website if cmd.website is None else cmd.website
        description = org.description if cmd.description is None else cmd.description
        email = org.email if cmd.email is None else cmd.email

        # update Organisation...
        updated = Organisation(None, name, website, description, email)
        manager.update(org.id, updated)

        org = manager.find(org.id)

    print(JSONify.dumps(org))
