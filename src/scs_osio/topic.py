#!/usr/bin/env python3

"""
Created on 16 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Requires APIAuth document.

workflow:
Use osio_publication instead.

command line example:
./topic.py /orgs/south-coast-science-dev/test/1/status -n "test" -d "test of status" -s 28 -v
"""

import sys

from scs_core.data.json import JSONify

from scs_core.osio.client.api_auth import APIAuth

from scs_core.osio.data.topic import Topic
from scs_core.osio.data.topic_info import TopicInfo

from scs_core.osio.manager.topic_manager import TopicManager

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_topic import CmdTopic


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdTopic()

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
        print("topic: APIAuth not available.", file=sys.stderr)
        exit(1)

    # manager...
    manager = TopicManager(HTTPClient(), api_auth.api_key)

    # check for existing registration...
    topic = manager.find(cmd.path)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        if topic:
            if cmd.schema_id is not None:
                print("topic: It is not possible to change the schema ID of an existing topic.", file=sys.stderr)
                cmd.print_help(sys.stderr)
                exit(1)

            name = topic.name if cmd.name is None else cmd.name
            description = topic.description if cmd.description is None else cmd.description

            info = TopicInfo(TopicInfo.FORMAT_JSON) if topic.info is None else topic.info

            # update Topic...
            updated = Topic(None, name, description, topic.is_public, info, None, None)

            manager.update(topic.path, updated)

            topic = manager.find(topic.path)

        else:
            if not cmd.is_complete():
                print("topic: All fields required for topic creation must be provided.", file=sys.stderr)
                cmd.print_help(sys.stderr)
                exit(1)

            info = TopicInfo(TopicInfo.FORMAT_JSON)

            # create Topic...
            topic = Topic(cmd.path, cmd.name, cmd.description, True, info, True, cmd.schema_id)
            manager.create(topic)

    print(JSONify.dumps(topic))
