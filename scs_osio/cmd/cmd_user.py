"""
Created on 21 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdUser(object):
    """
    unix command line handler
    """

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog -p PASSWORD [-n NAME] [-e EMAIL] [-v]",
                                              version="%prog 1.0")

        # compulsory...
        self.__parser.add_option("--password", "-p", type="string", nargs=1, action="store", dest="password",
                                 help="password (compulsory)")

        # optional...
        self.__parser.add_option("--name", "-n", type="string", nargs=1, action="store", dest="name",
                                 help="set name")

        self.__parser.add_option("--email", "-e", type="string", nargs=1, action="store", dest="email",
                                 help="set email address")


        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.password is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.name is not None or self.email is not None or self.password is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def password(self):
        return self.__opts.password


    @property
    def name(self):
        return self.__opts.name

    @property
    def email(self):
        return self.__opts.email


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
        return "CmdUser:{password:%s, name:%s, email:%s, verbose:%s, args:%s}" % \
                    (self.password, self.name, self.email, self.verbose, self.args)
