#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import ClientHelper

class User:
    def __init__(self):
        self.helper = ClientHelper()
        self.current_user = self.helper.client.user.me

    def get_current_user_id(self):
        return self.current_user['id']

def main():
    user = User()
    print user.get_current_user_id()

if __name__ == "__main__":
    main()