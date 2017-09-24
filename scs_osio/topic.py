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
    api_auth = APIAuth.load_from_host(Host)

    if api_auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit(1)

    # manager...
    manager = TopicManager(HTTPClient(), api_auth.api_key)

    # check for existing registration...
    topics = manager.find_for_org(api_auth.org_id, cmd.path, cmd.schema_id)     # find TopicSummary

    topic = topics[0] if len(topics) > 0 else None


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():

        if topic:
            name = topic.name if cmd.name is None else cmd.name
            description = topic.description if cmd.description is None else cmd.description

            info = TopicInfo(TopicInfo.FORMAT_JSON) if topic.info is None else topic.info
            schema_id = topic.schema_id if cmd.schema_id is None else cmd.schema_id

            # update Topic...
            updated = Topic(None, name, description, topic.is_public, info, True, schema_id)
            manager.update(topic.path, updated)

            topic = manager.find(topic.path)

        else:
            if not cmd.is_complete():
                print("The topic does not exist, and not all fields required for its creation were provided.",
                      file=sys.stderr)
                cmd.print_help(sys.stderr)
                exit(1)

            info = TopicInfo(TopicInfo.FORMAT_JSON)

            # create Topic...
            topic = Topic(cmd.path, cmd.name, cmd.description, True, info, True, cmd.schema_id)
            manager.create(topic)

    print(JSONify.dumps(topic))
