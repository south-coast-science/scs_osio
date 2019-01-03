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
        self.__parser = optparse.OptionParser(usage="%prog CLIENT_ID [-l LAT LNG POSTCODE] [-d DESCRIPTION] [-v]",
                                              version="%prog 1.0")

        # optional...
        self.__parser.add_option("--loc", "-l", type="string", nargs=3, action="store", dest="lat_lng_postcode",
                                 help="set device location")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="set device description")

        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self):
        if self.client_id is None:
            return False

        return True


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.__opts.lat_lng_postcode is not None or self.description is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def client_id(self):
        return self.__args[0] if len(self.__args) > 0 else None


    @property
    def lat(self):
        return None if self.__opts.lat_lng_postcode is None else self.__opts.lat_lng_postcode[0]


    @property
    def lng(self):
        return None if self.__opts.lat_lng_postcode is None else self.__opts.lat_lng_postcode[1]


    @property
    def postcode(self):
        return None if self.__opts.lat_lng_postcode is None else self.__opts.lat_lng_postcode[2]


    @property
    def description(self):
        return self.__opts.description


    @property
    def verbose(self):
        return self.__opts.verbose


    # ----------------------------------------------------------------------------------------------------------------

    def print_help(self, file):
        self.__parser.print_help(file)


    def __str__(self, *args, **kwargs):
        return "CmdDevice:{client_id:%s, lat:%s, lng:%s, postcode:%s, description:%s, verbose:%s}" % \
                    (self.client_id, self.lat, self.lng, self.postcode, self.description, self.verbose)
