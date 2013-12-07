#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about users.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper

#
# Helper of user.
#
class User:

    # Initiate user.
    def __init__( self ):
        self.helper = ClientHelper()
        self.current_user = self.helper.client.user.me

    # Get the current user ID.
    def get_current_user_id( self ):
        return self.current_user[ 'id' ]

    # Get the json of current user.
    def get_current_user( self ):
        return self.current_user

# Main.
def main():
    user = User()
    print user.get_current_user_id()
    print user.get_current_user()

if __name__ == "__main__":
    main()
