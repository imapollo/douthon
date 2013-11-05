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
        for book in list:
            print book['book']['id']

    def list_book_name(self):
        list = self.list()
        for book in list:
           print book['book']['title']

    def get_book_info(self, book_id):
        return self.helper.client.book.get(book_id)

    def get_book_authors(self, book_id):
        return self.get_book_info(book_id)['author']

def main():
    book = Book()
    # book.list_book_name()
    # book.list_book_id()
    print book.get_book_authors(1272857)[0]

if __name__ == "__main__":
    main()
