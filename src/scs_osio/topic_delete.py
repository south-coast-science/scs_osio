#!/usr/bin/env python3

"""
Created on 16 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line example:
./topic_delete.py -v /orgs/south-coast-science-dev/test/b/status
"""

import sys

from scs_core.osio.manager.topic_manager import TopicManager
from scs_core.osio.client.api_auth import APIAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_topic_delete import CmdTopicDelete


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdTopicDelete()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("topic_delete: %s" % cmd, file=sys.stderr)
        sys.stderr.flush()


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    auth = APIAuth.load(Host)

    if auth is None:
        print("topic_delete: APIAuth not available.", file=sys.stderr)
        exit(1)

    # manager...
    manager = TopicManager(auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    success = manager.delete(cmd.path)

    if cmd.verbose:
        print("topic_delete: deleted: %s" % success, file=sys.stderr)
