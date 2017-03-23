#!/usr/bin/env python3

"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

workflow:
  1: ./scs_osio/device_id.py
  2: ./scs_osio/api_auth.py
  3: ./scs_osio/device.py
> 4: ./scs_osio/project.py

Requires APIAuth and DeviceID documents.
Creates Project document.

command line example:
./scs_osio/project.py -v -s field-trial 2 -g 28
"""

import sys

from scs_core.data.json import JSONify
from scs_core.osio.client.api_auth import APIAuth
from scs_core.osio.config.project import Project
from scs_core.osio.data.topic import Topic
from scs_core.osio.data.topic_info import TopicInfo
from scs_core.osio.manager.topic_manager import TopicManager
from scs_core.sys.device_id import DeviceID

from scs_host.client.http_client import HTTPClient
from scs_host.sys.host import Host

from scs_osio.cmd.cmd_publication import CmdPublication


# TODO: rename as "project"

# TODO: balk if there already are any topics with the given paths (override with -f)

# --------------------------------------------------------------------------------------------------------------------

class TopicCreator(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, topic_manager):
        """
        Constructor
        """
        self.__topic_manager = topic_manager


    # ----------------------------------------------------------------------------------------------------------------

    def construct_topic(self, path, name, description, schema_id):
        # topic = self.__topic_manager.find(path)

        # if topic:
        #     print("Warning: topic already exists: %s")
        #     TODO: update topic with field params
            # return

        # success = self.__topic_manager.create()

        topic_info = TopicInfo(TopicInfo.FORMAT_JSON, None, None, None)     # for the v2 API, schema_id goes in Topic
        topic = Topic(path, name, description, True, True, topic_info, schema_id)

        print(topic)

        try:
            success = self.__topic_manager.create(topic)
        except RuntimeError:
            success = False

        return success


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "TopicCreator:{topic_manager:%s}" % self.__topic_manager


# --------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ----------------------------------------------------------------------------------------------------------------
    # cmd...

    cmd = CmdPublication()

    if cmd.verbose:
        print(cmd, file=sys.stderr)


    # ----------------------------------------------------------------------------------------------------------------
    # resource...

    http_client = HTTPClient()

    auth = APIAuth.load_from_host(Host)

    if auth is None:
        print("APIAuth not available.", file=sys.stderr)
        exit()


    device_id = DeviceID.load_from_host(Host)

    if device_id is None:
        print("DeviceID not available.", file=sys.stderr)
        exit()

    if cmd.verbose:
        print(device_id, file=sys.stderr)


    manager = TopicManager(http_client, auth.api_key)

    creator = TopicCreator(manager)


    # ----------------------------------------------------------------------------------------------------------------
    # run...

    if cmd.set():
        pub = Project.construct(auth.org_id, cmd.group, cmd.location_id)

        print(JSONify.dumps(pub))

        creator.construct_topic(pub.climate_topic_path(), Project.CLIMATE_NAME,
                                Project.CLIMATE_DESCRIPTION, Project.CLIMATE_SCHEMA)

        creator.construct_topic(pub.gases_topic_path(), Project.GASES_NAME,
                                Project.GASES_DESCRIPTION, cmd.gases_schema_id)

        creator.construct_topic(pub.particulates_topic_path(), Project.PARTICULATES_NAME,
                                Project.PARTICULATES_DESCRIPTION, Project.PARTICULATES_SCHEMA)

        creator.construct_topic(pub.status_topic_path(device_id), Project.STATUS_NAME,
                                Project.STATUS_DESCRIPTION, Project.STATUS_SCHEMA)

        creator.construct_topic(pub.control_topic_path(device_id), Project.CONTROL_NAME,
                                Project.CONTROL_DESCRIPTION, Project.CONTROL_SCHEMA)

        pub.save(Host)      # TODO: only save if successful


    else:
        pub = Project.load_from_host(Host)
        print(JSONify.dumps(pub))

    if cmd.verbose:
        print("-", file=sys.stderr)
        print("climate_topic:      %s" % pub.climate_topic_path(), file=sys.stderr)
        print("gases_topic:        %s" % pub.gases_topic_path(), file=sys.stderr)
        print("particulates_topic: %s" % pub.particulates_topic_path(), file=sys.stderr)

        print("status_topic:       %s" % pub.status_topic_path(device_id), file=sys.stderr)
        print("control_topic:      %s" % pub.control_topic_path(device_id), file=sys.stderr)
