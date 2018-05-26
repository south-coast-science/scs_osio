#!/usr/bin/env python3

"""
Created on 14 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line example:
./topic_list.py -p /orgs/south-coast-science-dev/uk -v
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.manager.schema_manager import SchemaManager
from scs_core.osio.client.api_auth import APIAuth

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_schema_list import CmdSchemaList


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdSchemaList()

    if cmd.verbose:
        print("schema_list: %s" % cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    auth = APIAuth.load(Host)

    if auth is None:
        print("schema_list: APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("schema_list: %s" % auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = SchemaManager(HTTPClient(), auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    schemas = manager.find_all()

    for schema in schemas:
        print(JSONify.dumps(schema))

    if cmd.verbose:
        print("schema_list: total: %d" % len(schemas), file=sys.stderr)
