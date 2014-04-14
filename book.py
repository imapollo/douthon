#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about books.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient
from fixed_data import FixedData
from user import UserHelper
from douban_call import douban_limited_call

import re
import sys

#
# Book object.
#
class Book:

    id = 0
    isbn10 = 0
    isbn13 = 0
    title = ""
    alt = ""
    image = ""
    author = []
    translator = []
    publisher = ""
    pubdate = ""
    rating = {}
    tags = []
    price = 0
    pages = 0

#
# Data Persistence for Book.
#
class BookData( FixedData ):

    def __init__( self ):
        self.helper = ClientHelper()
        mongodb = MongoDBClient()
        self.db = mongodb.db

    @douban_limited_call
    def get_data_from_douban( self, id ):
        return self.helper.client.book.get( id )

    def get_data_from_mongodb( self, id ):
        db_books = self.db.books
        return db_books.find_one( { "id" : "%s" % id } )

    def upsert_data_into_mongo( self, data ):
        books = self.db.books
        if ( books.find_one( { "id": "%s" % data[ 'id' ] } ) ):
            pass
        else:
            book = self.deserialize_book_info( data )
            books.insert( self.serialize_book( book ) )

    # Serialize the Book object into dictionary.
    def serialize_book( self, book ):
        book_info = {}
        book_info['id'] = book.id
        book_info['isbn10'] = book.isbn10
        book_info['isbn13'] = book.isbn13
        book_info['title'] = book.title
        book_info['alt'] = book.alt
        book_info['image'] = book.image
        book_info['price'] = book.price
        book_info['pages'] = book.pages
        book_info['author'] = book.author
        book_info['translator'] = book.translator
        book_info['publisher'] = book.publisher
        book_info['pubdate'] = book.pubdate
        book_info['rating'] = book.rating
        book_info['tags'] = book.tags
        return book_info

    # Deserialize the book information dictionary into book
    # object.
    def deserialize_book_info( self, book_info ):
        book = Book()
        book.id     = book_info.get( "id" )
        book.title  = book_info.get( "title" )
        book.isbn10 = book_info.get( "isbn10" )
        book.isbn13 = book_info.get( "isbn13" )
        book.alt    = book_info.get( "alt" )
        book.image  = book_info.get( "image" )
        book.price  = book_info.get( "price" )
        book.pages  = book_info.get( "pages" )
        book.author = book_info.get( "author" )
        book.translator = book_info.get( "translator" )
        book.publisher  = book_info.get( "publisher" )
        book.pubdate    = book_info.get( "pubdate" )
        book.rating     = book_info.get( "rating" )
        book.tags       = book_info.get( "tags" )
        return book

#
# Helper class for book.
#
class BookHelper:

    # Initate the helper.
    def __init__( self ):
        self.book_data = BookData()

    # Get full information of a book from Douban API.
    def get_book_info( self, book_id ):
        return self.book_data.get_data( book_id )

    # Get the author of a book.
    def get_book_authors( self, book_id ):
        return self.get_book_info( book_id )[ 'author' ]

    # Remove unnecessary characters from the author.
    def trim_book_author( self, author ):
        # TODO remove the unnecessary diff.
        author = re.sub( r'\s*\[.*\]\s*', '', author )
        author = re.sub( r'\s*\(.*\)\s*', '', author )
        # erase chinese（）
        author = re.sub( ur'\s*\uff08.*\uff09\s*', '', author )
        return author

# Main.
def main():
    helper = BookHelper()
    # helper.upsert_book_info( 1003078 )
    # book.list_book_name()
    # user_book_collections = { book.me.get_current_user_id(): book.list_book_id() }
    # print user_book_collections
    print helper.get_book_authors( "1003078" )
    #for book_id in helper.list_user_book_id( "1905602" ):
    #    helper.upsert_book_info( book_id )
    # print book.get_book_authors(1272857)[0]

if __name__ == "__main__":
    main()
