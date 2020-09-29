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
from scs_core.osio.manager.topic_manager import TopicManager
from scs_core.osio.client.api_auth import APIAuth

from scs_host.sys.host import Host

from scs_osio.cmd.cmd_topic_list import CmdTopicList


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdTopicList()

    if cmd.verbose:
        print("topic_list: %s" % cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resources...

    # APIAuth...
    api_auth = APIAuth.load(Host)

    if api_auth is None:
        print("topic_list: APIAuth not available.", file=sys.stderr)
        exit(1)

    if cmd.verbose:
        print("topic_list: %s" % api_auth, file=sys.stderr)
        sys.stderr.flush()

    # manager...
    manager = TopicManager(api_auth.api_key)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    topics = manager.find_for_org(api_auth.org_id, cmd.partial_path, cmd.schema_id)

    for topic in topics:
        print(JSONify.dumps(topic))

    if cmd.verbose:
        print("topic_list: total: %d" % len(topics), file=sys.stderr)
