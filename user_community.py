#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about users community, followers / following etc.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient

class UserCommunityHelper:

    # Initiate user.
    def __init__( self ):
        self.helper = ClientHelper()
        mongodb = MongoDBClient()
        self.db = mongo.db

# Main.
def main():
    helper = UserCommunityHelper()

if __name__ == "__main__":
    main()
