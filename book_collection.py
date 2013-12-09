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
        self.user = UserHelper()

    # List all the book collections for specific user.
    def list_user_books( self, user_id ):
        return self.helper.client.book.list_all( user_id )

    # List all the book collections for current user.
    def list_current_user_books( self ):
        return self.list_user_books( self.user.get_current_user_id() )

    # Upsert all the user collection information into MongoDB.
    def upsert_book_collection( self, user_id ):
        mongodb = MongoDBClient()
        db = mongodb.db
        db_book_collections = db.book_collections
        user_collections = self.list_user_books( user_id )
        for user_collection in user_collections:
            if ( db_book_collections.find_one( { "book_id" : "%s" % user_collection.get( "book_id" ), "user_id" : "%s" % user_id } ) ):
                pass
            else:
                book_collection = self.deserialize_book_collection_info( user_collection )
                db_book_collections.insert( self.serialize_book_collection( book_collection ) )

    # Compare the book collections between 2 users.
    def compare_book_collections( self, user_a_id, user_b_id ):
        mongodb = MongoDBClient()
        db = mongodb.db
        db_book_collections = db.book_collections
        user_a_collections = db_book_collections.find( { "user_id" : "%s" % user_a_id } )
        # user_b_collections = db_book_collections.find( { "user_id" : "%s" % user_b_id } )
        for user_a_collection in user_a_collections:
            if ( db_book_collections.find_one( { "user_id" : "%s" % user_b_id,
                    "book_id" : "%s" % user_a_collection.get( "book_id" ) } )):
                print user_a_collection.get( "book_id" )

    # Serialize the Book collection object into dictionary.
    def serialize_book_collection( self, book_collection ):
        book_collection_info = {}
        book_collection_info['id'] = book_collection.id
        book_collection_info['user_id'] = book_collection.user_id
        book_collection_info['book_id'] = book_collection.book_id
        book_collection_info['comment'] = book_collection.comment
        book_collection_info['rating'] = book_collection.rating
        book_collection_info['status'] = book_collection.status
        book_collection_info['updated'] = book_collection.updated
        return book_collection_info

    # Deserialize the book information dictionary into book
    # object.
    def deserialize_book_collection_info( self, book_collection_info ):
        book_collection = BookCollection()
        book_collection.id = book_collection_info.get("id")
        book_collection.user_id = book_collection_info.get("user_id")
        book_collection.book_id = book_collection_info.get("book_id")
        book_collection.comment = book_collection_info.get("comment")
        book_collection.rating = book_collection_info.get("rating")
        book_collection.status = book_collection_info.get("status")
        book_collection.updated = book_collection_info.get("updated")
        return book_collection

# Main.
def main():
    helper = BookCollectionHelper()
    # helper.upsert_book_collection( helper.user.get_current_user_id() )
    # helper.upsert_book_collection( "1905602" )
    helper.compare_book_collections( helper.user.get_current_user_id(), "1905602" )

if __name__ == "__main__":
    main()
