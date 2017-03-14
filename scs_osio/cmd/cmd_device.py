"""
Created on 19 Feb 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdDevice(object):
    """
    unix command line handler
    """

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-u USER_ID -l LAT LNG POSTCODE [-d DESCRIPTION]] [-v]",
                                              version="%prog 1.0")

        # optional...
        self.__parser.add_option("--user", "-u", type="string", nargs=1, action="store", dest="user_id",
                                 help="user-id")

        self.__parser.add_option("--loc", "-l", type="string", nargs=3, action="store", dest="lat_lng_postcode",
                                 help="device location")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="device description")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if bool(self.__opts.user_id) == bool(self.__opts.lat_lng_postcode):
            return True

        return False


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.__opts.user_id is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def user_id(self):
        return self.__opts.user_id

    @property
    def lat(self):
        return self.__opts.lat_lng_postcode[0] if self.__opts.lat_lng_postcode else None


    @property
    def lng(self):
        return self.__opts.lat_lng_postcode[1] if self.__opts.lat_lng_postcode else None


    @property
    def postcode(self):
        return self.__opts.lat_lng_postcode[2] if self.__opts.lat_lng_postcode else None


    @property
    def description(self):
        return self.__opts.description


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
        return "CmdDevice:{user_id:%s, lat:%s, lng:%s, postcode:%s, description:%s, verbose:%s, args:%s}" % \
                    (self.user_id, self.lat, self.lng, self.postcode, self.description, self.verbose, self.args)
