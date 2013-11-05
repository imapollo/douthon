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

def main():
    book = Book()
    book.list_book_name()

if __name__ == "__main__":
    main()
