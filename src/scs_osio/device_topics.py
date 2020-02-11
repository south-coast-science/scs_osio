#!/usr/bin/env python3

"""
Created on 2 Jul 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth and SystemID documents.

command line examples:
./device_topics.py 5926 -v
"""

import sys

from scs_core.data.datetime import LocalizedDatetime
from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.manager.device_manager import DeviceManager
from scs_core.osio.manager.topic_manager import TopicManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_device_topics import CmdDeviceTopics


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdDeviceTopics()

    if not cmd.is_valid():
        cmd.print_help(sys.stderr)
        exit(2)

    if cmd.verbose:
        print("device_topics: %s" % cmd, file=sys.stderr)

    try:
        # ------------------------------------------------------------------------------------------------------------
        # resources...

        # APIAuth...
        api_auth = APIAuth.load(Host)

        if api_auth is None:
            print("device_topics: APIAuth not available.", file=sys.stderr)
            exit(1)

        if cmd.verbose:
            print("device_topics: %s" % api_auth, file=sys.stderr)
            sys.stderr.flush()

        # managers...
        device_manager = DeviceManager(HTTPClient(), api_auth.api_key)

        # check for existing registration...
        device = device_manager.find(api_auth.org_id, cmd.client_id)

        if device is None:
            print("device_topics: Device not found.", file=sys.stderr)
            exit(1)

        topic_manager = TopicManager(HTTPClient(), api_auth.api_key)


        # ------------------------------------------------------------------------------------------------------------
        # run...

        # time...
        if cmd.use_offset():
            end = LocalizedDatetime.now()
            start = end.timedelta(minutes=-cmd.minutes)
        else:
            end = LocalizedDatetime.now() if cmd.end is None else cmd.end
            start = cmd.start

        if cmd.verbose:
            print("device_topics: start: %s" % start, file=sys.stderr)
            print("device_topics: end: %s" % end, file=sys.stderr)
            sys.stderr.flush()

        # topics...
        topics = topic_manager.find_for_device(cmd.client_id, start, end)

        for topic in topics:
            print(JSONify.dumps(topic))

        if cmd.verbose:
            print("device_topics: total: %d" % len(topics), file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # end...

    except KeyboardInterrupt:
        if cmd.verbose:
            print("device_topics: KeyboardInterrupt", file=sys.stderr)
