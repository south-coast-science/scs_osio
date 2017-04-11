"""
Created on 8 Apr 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import optparse


# --------------------------------------------------------------------------------------------------------------------

class CmdHostOrganisation(object):
    """
    unix command line handler
    """

    def __init__(self):
        """
        Constructor
        """
        self.__parser = optparse.OptionParser(usage="%prog [-o ORG_ID] [-n NAME] [-w WEB] [-d DESCRIPTION] [-e EMAIL]"
                                                    " [-v]", version="%prog 1.0")

        # optional...
        self.__parser.add_option("--org", "-o", type="string", nargs=1, action="store", dest="org_id",
                                 help="set org-id (only if organisation has not yet been registered)")

        self.__parser.add_option("--name", "-n", type="string", nargs=1, action="store", dest="name",
                                 help="set name (required if organisation has not yet been registered)")

        self.__parser.add_option("--web", "-w", type="string", nargs=1, action="store", dest="website",
                                 help="set web URL (required if organisation has not yet been registered)")

        self.__parser.add_option("--desc", "-d", type="string", nargs=1, action="store", dest="description",
                                 help="set description (required if organisation has not yet been registered)")

        self.__parser.add_option("--email", "-e", type="string", nargs=1, action="store", dest="email",
                                 help="set email address (required if organisation has not yet been registered)")

        # optional...
        self.__parser.add_option("--verbose", "-v", action="store_true", dest="verbose", default=False,
                                 help="report narrative to stderr")

        self.__opts, self.__args = self.__parser.parse_args()


    # ----------------------------------------------------------------------------------------------------------------

    def is_valid(self, org):
        if org is None:
            return self.is_complete()

        return True


    def is_complete(self):
        return self.org_id is not None and self.name is not None and self.website is not None and \
               self.description is not None and self.email is not None


    # ----------------------------------------------------------------------------------------------------------------

    def set(self):
        return self.name is not None or self.website is not None or \
               self.description is not None or self.email is not None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def org_id(self):
        return self.__opts.org_id


    @property
    def name(self):
        return self.__opts.name


    @property
    def website(self):
        return self.__opts.website


    @property
    def description(self):
        return self.__opts.description


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
        return "CmdHostOrganisation:{org_id:%s, name:%s, website:%s, description:%s, email:%s, " \
               "verbose:%s, args:%s}" % \
                    (self.org_id, self.name, self.website, self.description, self.email,
                     self.verbose, self.args)
