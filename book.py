#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about books.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient
from user import UserHelper

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
# Helper class for book.
#
class BookHelper:

    # Initate the helper.
    def __init__( self ):
        self.helper = ClientHelper()
        self.me = UserHelper()

    # List all the book collections for specific user.
    def list_user_books( self, user_id )
        return self.helper.client.book.list_all( user_id )

    # List all the book collections for current user.
    def list( self ):
        return self.list_user_books( self.me.get_current_user_id() )

    # List all the book IDs for specific user.
    def list_user_book_id( self, user_id ):
        list = self.list_user_books( user_id )
        book_id_list = []
        for book in list:
            book_id_list.append( book['book']['id'] )
        return book_id_list

    # List all the book IDs for current user.
    def list_book_id( self ):
        return self.list_user_book_id( self.me.get_current_user_id() )

    # List all the book names for specific user.
    def list_user_book_names( self, user_id ):
        list = self.list_user_books( user_id )
        book_name_list = []
        for book in list:
           bookd_name_list.append( book['book']['title'] )
        return book_name_list

    # List all the book names for current user.
    def list_book_names( self ):
        return self.list_user_book_names( self.me.get_current_user_id() )

    # Get full information of a book.
    def get_book_info( self, book_id ):
        return self.helper.client.book.get(book_id)

    # Get the author of a book.
    def get_book_authors( self, book_id ):
        return self.get_book_info( book_id )['author']

    # Upsert all the book information for a user.
    def update_book_for_user( self, user_id ):
        for book_id in helper.list_book_id():
            helper.upsert_book_info( book_id )

    # Upsert the book information into MongoDB.
    def upsert_book_info( self, book_id ):
        mongodb = MongoDBClient()
        db = mongodb.db
        books = db.books
        if ( books.find_one( { "id": "%s" % book_id } ) ):
            pass
        else:
            book_info = self.get_book_info( book_id )
            book = self.deserialize_book_info( book_info )
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

# Main.
def main():
    helper = BookHelper()
    # helper.upsert_book_info( 1003078 )
    # book.list_book_name()
    # user_book_collections = { book.me.get_current_user_id(): book.list_book_id() }
    # print user_book_collections
    for book_id in helper.list_book_id():
        helper.upsert_book_info( book_id )
    # print book.get_book_authors(1272857)[0]

if __name__ == "__main__":
    main()
