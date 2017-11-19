"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdDeviceList(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog {-u | -o} [-v]", version="%prog 1.0")

        # compulsory...
        self.__parser.add_option("--user", "-u", action="store_true", dest="user", default=False,
                                 help="list for user ID of client auth")

        self.__parser.add_option("--org", "-o", action="store_true", dest="org", default=False,
                                 help="list for  org ID of API auth")

        # optional...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.user or self.org:
            return True

        return False


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def user(self):
        return self.__opts.user


    @property
    def org(self):
        return self.__opts.org


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
        return "CmdDeviceList:{user:%s, org:%s, verbose:%s, args:%s}" % \
               (self.user, self.org, self.verbose, self.args)
