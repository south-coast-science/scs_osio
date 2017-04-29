"""
Created on 14 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# TODO: remove - use TopicDelete instead, because PATH should be compulsory

# --------------------------------------------------------------------------------------------------------------------

class CmdTopicList(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [PARTIAL_PATH] [-v]", version="%prog 1.0")

        # optional...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def partial_path(self):
        return self.__args[0] if len(self.__args) > 0 else "/"


    @property
    def verbose(self):
        return self.__opts.verbose


    @property
    def args(self):
        return self.__args


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "CmdTopicList:{partial_path:%s, verbose:%s, args:%s}" % (self.partial_path, self.verbose, self.args)
