#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about book recommendations, based on following.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from user import UserHelper
from book_collection import BookCollectionHelper
from user_community import UserCommunityHelper
from mongodb import MongoDBClient

class BookRecommender:

    # Initiate user.
    def __init__( self ):
        self.helper = ClientHelper()
        mongodb = MongoDBClient()
        self.db = mongodb.db
        self.userHelper = UserHelper()
        self.communityHelper = UserCommunityHelper()
        self.collectionHelper = BookCollectionHelper()

    # Get the reading trends for following.
    def get_following_reading_trends( self ):
        followings = self.communityHelper.get_current_user_following()
        for following in followings:
            print following
            print self.collectionHelper.get_book_read_trends( following[ "id" ] )

# Main.
def main():
    recommender = BookRecommender()
    recommender.get_following_reading_trends()

if __name__ == "__main__":
    main()
