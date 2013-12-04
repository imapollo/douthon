#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import ClientHelper

class User:
    def __init__(self):
        self.helper = ClientHelper()
        self.current_user = self.helper.client.user.me

    def get_current_user_id(self):
        return self.current_user['id']

    def get_current_user(self):
        return self.current_user

def main():
    user = User()
    print user.get_current_user_id()
    print user.get_current_user()

if __name__ == "__main__":
    main()
