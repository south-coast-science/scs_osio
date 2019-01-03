"""
Created on 18 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

example document:
{"user-id": "southcoastscience-dev", "client-id": "5873", "client-password": "d4MctQFa"}
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdClientAuth(object):
    """unix command line handler"""

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-s USER_ID CLIENT_ID CLIENT_PASSWORD] [-v]",
                                              version="%prog 1.0")

        # optional...
        self.__parser.add_option("--set", "-s", type="string", nargs=3, action="store", dest="user_client_password",
                                 help="user ID, client ID and client password")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.__opts.user_client_password is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def user_id(self):
        return None if self.__opts.user_client_password is None else self.__opts.user_client_password[0]


    @property
    def client_id(self):
        return None if self.__opts.user_client_password is None else self.__opts.user_client_password[1]


    @property
    def client_password(self):
        return None if self.__opts.user_client_password is None else self.__opts.user_client_password[2]


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "CmdClientAuth:{user_id:%s, client_id:%s, client_password:%s, verbose:%s}" % \
               (self.user_id, self.client_id, self.client_password, self.verbose)
