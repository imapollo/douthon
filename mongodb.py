#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# MongoDB Client Helper.
#
# author: ze.apollo@gmail.com
#

from pymongo import MongoClient

#
# MongoDB client.
#
class MongoDBClient:

    # Initiate the MongeDB client.
    def __init__( self ):
        self.db = MongoClient( 'localhost', 27017 ).test

# Main.
def main():
    mongodb = MongoDBClient()
    db = mongodb.db
    users = db.users
    print users.find_one( { "name": "xia" } )

if __name__ == "__main__":
    main()
