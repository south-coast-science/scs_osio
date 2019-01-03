"""
Created on 14 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdTopicList(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [PARTIAL_PATH] [-s SCHEMA_ID] [-v]", version="%prog 1.0")

        # optional...
        self.__parser.add_option("--schema", "-s", type="int", nargs=1, action="store", dest="schema_id",
                                 help="restrict to topics matching SCHEMA_ID")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def partial_path(self):
        return self.__args[0] if len(self.__args) > 0 else None


    @property
    def schema_id(self):
        return self.__opts.schema_id


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "CmdTopicList:{partial_path:%s, schema_id:%s, verbose:%s}" % \
               (self.partial_path, self.schema_id, self.verbose)
