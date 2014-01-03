#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about users community, followers / following etc.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from user import UserHelper
from book_collection import BookCollectionHelper
from mongodb import MongoDBClient

class UserCommunityHelper:

    # Initiate user.
    def __init__( self ):
        self.helper = ClientHelper()
        mongodb = MongoDBClient()
        self.db = mongodb.db
        self.userHelper = UserHelper()

    # Get the followers for a user.
    def get_user_followers( self, user_id ):
        return self.helper.client.user.followers( user_id )

    # Get the followers for the current user.
    def get_current_user_followers( self ):
        return self.get_user_followers( self.userHelper.get_current_user_id() )

    # Get the following for a user.
    def get_user_following( self, user_id ):
        return self.helper.client.user.all_following( user_id )

    # Get the following for the current user.
    def get_current_user_following( self ):
        return self.get_user_following( self.userHelper.get_current_user_id() )


# Main.
def main():
    helper = UserCommunityHelper()
    collectionHelper = BookCollectionHelper()
    followings = helper.get_current_user_following()
    for following in followings:
        print collectionHelper.get_book_read_trends( following[ "id" ] )
        break

if __name__ == "__main__":
    main()
