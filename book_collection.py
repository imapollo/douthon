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
import re

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
        self.bookHelper = BookHelper()

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
        for user_a_collection in user_a_collections:
            user_b_collection = db_book_collections.find_one( { "user_id" : "%s" % user_b_id,
                    "book_id" : "%s" % user_a_collection.get( "book_id" ) } )
            if ( user_b_collection ):
                self.compare_book_collection( user_a_collection, user_b_collection )

    # Compare the book metadatas between 2 users.
    def compare_book_collections_metadata( self, user_a_id, user_b_id ):
        mongodb = MongoDBClient()
        db = mongodb.db
        db_book_collections = db.book_collections
        user_a_collections = db_book_collections.find( { "user_id" : "%s" % user_a_id } )
        user_b_collections = db_book_collections.find( { "user_id" : "%s" % user_b_id } )
        # TODO do we need to insert into DB?
        a_authors = self.get_collection_authors( user_a_collections )
        b_authors = self.get_collection_authors( user_b_collections )
        common_authors = []
        for a_author_key in a_authors:
            for b_author_key in b_authors:
                if ( a_author_key == b_author_key ):
                    common_authors.append( a_author_key )
                    break
        for common_author in common_authors:
            print common_author

    # Get tags for a user based on user book collection.
    def get_collection_tags( self, book_collections ):
        collection_tags = {}
        for book_collection in book_collections:
            tags = self.bookHelper.get_book_info( book_collection.get("book_id"))['tags']
            for tag in tags:
                if ( collection_tags.get( "%s" % tag ) ):
                    collection_tags["%s" % tag] = collection_tags["%s" % tag] + 1
                else:
                    collection_tags["%s" % tag] = 1
        return collection_tags

    # Get author interests for a user based on user book collection.
    def get_collection_authors( self, book_collections ):
        collection_authors = {}
        for book_collection in book_collections:
            authors = self.bookHelper.get_book_info( book_collection.get("book_id"))['author']
            for author in authors:
                # TODO remove the unnecessary diff.
                author = re.sub( r'\s*\[.*\]\s*', '', author )
                author = re.sub( r'\s*\(.*\)\s*', '', author )
                # erase chinese（）
                author = re.sub( ur'\s*\uff08.*\uff09\s*', '', author )
                if ( collection_authors.get( "%s" % author ) ):
                    collection_authors["%s" % author] = collection_authors["%s" % author] + 1
                else:
                    collection_authors["%s" % author] = 1
        return collection_authors

    # Check common authors for 2 users collections.
    def compare_book_collection_authors( self, user_a_id ):
        pass

    # Check if 2 users have same interesting on same book.
    def compare_book_collection_ratings( self, user_a_collection, user_b_collection ):
        a_rating = user_a_collection.get("rating")
        b_rating = user_b_collection.get("rating")
        if ( a_rating and b_rating ):
            similar_taste = int( a_rating.get("value") ) - int( b_rating.get("value") )
            if ( similar_taste > -2 and similar_taste < 2 ):
                print "book id: %s" % user_a_collection.get( "book_id" )

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
    helper.compare_book_collections_metadata( helper.user.get_current_user_id(), "1905602" )

if __name__ == "__main__":
    main()
