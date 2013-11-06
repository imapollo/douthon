#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import ClientHelper
from user import User

class Book:
    def __init__(self):
        self.helper = ClientHelper()
        self.me = User()

    def list(self):
        return self.helper.client.book.list_all( self.me.get_current_user_id() )

    def list_book_id(self):
        list = self.list()
        book_id_list = []
        for book in list:
            book_id_list.append( book['book']['id'] )
        return book_id_list

    def list_book_name(self):
        list = self.list()
        book_name_list = []
        for book in list:
           bookd_name_list.append( book['book']['title'] )
        return book_name_list

    def get_book_info(self, book_id):
        return self.helper.client.book.get(book_id)

    def get_book_authors(self, book_id):
        return self.get_book_info(book_id)['author']

def main():
    book = Book()
    # book.list()
    # book.list_book_name()
    user_book_collections = { book.me.get_current_user_id(): book.list_book_id() }
    print user_book_collections
    # print book.list_book_id()
    # print book.get_book_authors(1272857)[0]

if __name__ == "__main__":
    main()
