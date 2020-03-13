#!/usr/bin/env python3

"""
Created on 2 Jul 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

command line example:
./user_topics.py southcoastscience-dev -v
"""

import sys

from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.manager.topic_manager import TopicManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_user_topics import CmdUserTopics


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdUserTopics()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("user_topics: %s" % cmd, file=sys.stderr)


    try:
        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # APIAuth...
        api_auth = APIAuth.load(Host)

        if api_auth is None:
            print("user_topics: APIAuth not available.", file=sys.stderr)
            exit(1)

        if cmd.verbose:
            print("user_topics: %s" % api_auth, file=sys.stderr)
            sys.stderr.flush()

        # manager...
        manager = TopicManager(HTTPClient(False), api_auth.api_key)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # find...
        topics = manager.find_for_user(cmd.user_id)

        for topic in topics:
            print(JSONify.dumps(topic))

        if cmd.verbose:
            print("user_topics: total: %d" % len(topics), file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        if cmd.verbose:
            print("user_topics: KeyboardInterrupt", file=sys.stderr)
