#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about books collections.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient
from user import UserHelper
from book import BookHelper

#
# Book collection object.
#
class BookCollection:

    id = 0
    user_id = 0
    book_id = 0
    comment = ""
    rating = {}
    status = ""
    updated = ""

#
# Helper class for book collection.
#
class BookCollectionHelper:

    # Initate the helper.
    def __init__( self ):
        self.helper = ClientHelper()

    # TODO need to know the data model for the user book collection at first.

    # List all the book collections for specific user.
    def list_user_books( self, user_id )
        return self.helper.client.book.list_all( user_id )

    # List all the book collections for current user.
    def list( self ):
        return self.list_user_books( self.me.get_current_user_id() )

# Main.
def main():
    helper = BookCollectionHelper()

if __name__ == "__main__":
    main()
