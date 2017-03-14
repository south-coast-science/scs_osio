"""
Created on 16 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdTopicCreate(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog PATH -n NAME -d DESCRIPTION [-s SCHEMA_ID] [-v]",
                                              version="%prog 1.0")

        # compulsory...
        self.__parser.add_option("--name", "-n", type="string", nargs=1, action="store", dest="name",
                                 help="name")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="description")

        # optional...
        self.__parser.add_option("--schema", "-s", type="int", nargs=1, action="store", dest="schema_id",
                                 help="schema ID")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.path is None or self.name is None or self.description is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def path(self):
        return self.__args[0] if len(self.__args) > 0 else None


    @property
    def name(self):
        return self.__opts.name


    @property
    def description(self):
        return self.__opts.description


    @property
    def schema_id(self):
        return self.__opts.schema_id


    @property
    def verbose(self):
        return self.__opts.verbose


    @property
    def args(self):
        return self.__args


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdTopicCreate:{path:%s, name:%s, description:%s, schema_id:%s, verbose:%s, args:%s}" % \
                    (self.path, self.name, self.description, self.schema_id, self.verbose, self.args)
