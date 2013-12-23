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

from datetime import datetime
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
        mongodb = MongoDBClient()
        self.db = mongodb.db

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
        # this will use mongo db cursor.
        # TODO have to rewind?
        user_a_collections = db_book_collections.find( { "user_id" : "%s" % user_a_id } )
        user_b_collections = db_book_collections.find( { "user_id" : "%s" % user_b_id } )
        user_common_authors = self.get_common_authors( user_a_collections, user_b_collections )
        user_a_collections.rewind()
        user_b_collections.rewind()
        user_common_tags = self.get_common_tags( user_a_collections, user_b_collections )
        print user_common_authors
        print user_common_tags

    # Get common authors for 2 different users.
    def get_common_authors( self, user_a_collections, user_b_collections ):
        user_common_authors = {}
        user_a_collection = user_a_collections[0]
        user_a_id = user_a_collection.get("user_id")
        user_b_collection = user_b_collections[0]
        user_b_id = user_b_collection.get("user_id")
        common_authors = []
        a_authors = self.get_collection_authors( user_a_collections )
        b_authors = self.get_collection_authors( user_b_collections )
        for a_author_key in a_authors:
            for b_author_key in b_authors:
                if ( a_author_key == b_author_key ):
                    common_authors.append( a_author_key )
                    user_author = {}
                    user_author[ "%s" % user_a_id ] = a_authors[ "%s" % a_author_key ]
                    user_author[ "%s" % user_b_id ] = b_authors[ "%s" % b_author_key ]
                    user_common_authors[ "%s" % a_author_key ] = user_author
                    break
        # for common_author in common_authors:
        #     print common_author
        return user_common_authors

    # Get common tags for 2 different users.
    def get_common_tags( self, user_a_collections, user_b_collections ):
        user_common_tags = {}
        user_a_collection = user_a_collections[0]
        user_a_id = user_a_collection.get("user_id")
        user_b_collection = user_b_collections[0]
        user_b_id = user_b_collection.get("user_id")
        common_tags = []
        a_tags = self.get_collection_tags( user_a_collections )
        b_tags = self.get_collection_tags( user_b_collections )
        for a_tag_key in a_tags:
            for b_tag_key in b_tags:
                if ( a_tag_key == b_tag_key ):
                    common_tags.append( a_tag_key )
                    user_tag = {}
                    user_tag[ "%s" % user_a_id ] = a_tags[ "%s" % a_tag_key ]
                    user_tag[ "%s" % user_b_id ] = b_tags[ "%s" % b_tag_key ]
                    user_common_tags[ "%s" % a_tag_key ] = user_tag
                    break
        # for common_tag in common_tags:
        #     print common_tag
        return user_common_tags

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
                author = self.bookHelper.trim_book_autor( author )
                if ( collection_authors.get( "%s" % author ) ):
                    collection_authors["%s" % author] = collection_authors["%s" % author] + 1
                else:
                    collection_authors["%s" % author] = 1
        return collection_authors

    # Check common authors for 2 users collections.
    def compare_book_collection_authors( self, user_a_id ):
        # TODO
        pass

    # Check if 2 users have same interesting on same book.
    def compare_book_collection_ratings( self, user_a_collection, user_b_collection ):
        a_rating = user_a_collection.get("rating")
        b_rating = user_b_collection.get("rating")
        if ( a_rating and b_rating ):
            similar_taste = int( a_rating.get("value") ) - int( b_rating.get("value") )
            if ( similar_taste > -2 and similar_taste < 2 ):
                print "book id: %s" % user_a_collection.get( "book_id" )

    # Get the books read each month.
    def get_book_read_trends( self, user_id ):
        db_book_collections = self.db.book_collections
        book_collections = db_book_collections.find( { "user_id" : "%s" % user_id } )
        months_trends = {}
        for book_collection in book_collections:
            if ( book_collection["status"] == "read" ):
                read_date = datetime.strptime( book_collection["updated"], "%Y-%m-%d %H:%M:%S")
                book_info = self.bookHelper.get_book_info( book_collection["book_id"])
                month = "%04d-%02d" %( read_date.year, read_date.month )
                if ( months_trends.get( "%s" % month ) ):
                    trending_info = months_trends[ "%s" % month ]
                    trending_info_books = trending_info[ "books" ]
                    trending_info_authors = trending_info[ "authors" ]
                    trending_info_tags = trending_info[ "tags" ]
                    trending_info_books[ "%s" % book_info[ "id"] ] = 1

                    for book_author in book_info[ "author" ]:
                        book_author = self.bookHelper.trim_book_author( book_author )
                        if ( trending_info_authors.get( book_author ) ):
                            trending_info_authors[ book_author ] += 1
                        else:
                            trending_info_authors[ book_author ] = 1

                    for book_tag in book_info[ "tags" ]:
                        book_tag = book_tag[ "title" ]
                        if ( trending_info_tags.get( book_tag ) ):
                            trending_info_tags[ book_tag ] += 1
                        else:
                            trending_info_tags[ book_tag ] = 1

                else:
                    trending_info = {}
                    trending_info_books = {}
                    trending_info_authors = {}
                    trending_info_tags = {}
                    trending_info[ "books" ] = trending_info_books
                    trending_info[ "authors" ] = trending_info_authors
                    trending_info[ "tags" ] = trending_info_tags
                    trending_info_books[ "%s" % book_info["id"] ] = 1
                    for book_author in book_info[ "author" ]:
                        book_author = self.bookHelper.trim_book_author( book_author )
                        trending_info_authors[ "%s" % book_author ] = 1
                    for book_tag in book_info[ "tags" ]:
                        book_tag = book_tag[ "title" ]
                        trending_info_tags[ "%s" % book_tag ] = 1
                    months_trends[ "%s" % month ] = trending_info

        return months_trends

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
    # helper.compare_book_collections_metadata( helper.user.get_current_user_id(), "1905602" )
    months = helper.get_book_read_trends( helper.user.get_current_user_id() )
    print months

if __name__ == "__main__":
    main()
