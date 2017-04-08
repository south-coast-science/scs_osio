"""
Created on 16 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdTopic(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog PATH [-n NAME -d DESCRIPTION [-s SCHEMA_ID]] [-v]",
                                              version="%prog 1.0")

        # optional...
        self.__parser.add_option("--name", "-n", type="string", nargs=1, action="store", dest="name",
                                 help="set name (required if topic has not yet been registered)")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="set description (required if topic has not yet been registered)")

        self.__parser.add_option("--schema", "-s", type="int", nargs=1, action="store", dest="schema_id",
                                 help="set schema ID (only if topic has not yet been registered)")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self, topic):
        if self.path is None:
            return False

        if topic is None:
            return self.is_complete()

        return True


    def is_complete(self):
        if self.name is None or self.description is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.__opts.name is not None or self.__opts.description is not None


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
        return "CmdTopic:{path:%s, name:%s, description:%s, schema_id:%s, verbose:%s, args:%s}" % \
                    (self.path, self.name, self.description, self.schema_id, self.verbose, self.args)
