#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about users.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient

#
# Douban user object.
#
class User:
    id = ""
    uid = ""
    name = ""
    created = ""
    avatar = ""
    signature = ""
    loc_name = ""
    desc = ""
    alt = ""

#
# Helper of user.
#
class UserHelper:

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

    # Get full information of a user from Douban API.
    def get_user_info( self, user_id ):
        return self.helper.client.user.get( user_id )

    # Get full information for the current user from Douban API.
    def get_current_user_info( self ):
        return self.get_user_info( self.get_current_user() )

    # Upsert the user information into MongoDB.
    def upsert_user_info( self, user_id ):
        mongodb = MongoDBClient()
        db = mongodb.db
        db_users = db.users
        if ( db_users.find_one( { "id": "%s" % user_id } ) ):
            pass
        else:
            user_info = self.get_user_info( user_id )
            user = self.deserialize_user_info( user_info )
            db_users.insert( self.serialize_user( user ) )

    # Serialize the User object into dictionary.
    def serialize_user( self, user ):
        user_info = {}
        user_info['id'] = user.id
        user_info['uid'] = user.uid
        user_info['name'] = user.name
        user_info['created'] = user.created
        user_info['avatar'] = user.avatar
        user_info['signature'] = user.signature
        user_info['loc_name'] = user.loc_name
        user_info['desc'] = user.desc
        user_info['alt'] = user.alt
        return user_info

    # Deserialize the user information dictionary into user 
    # object.
    def deserialize_user_info( self, user_info ):
        user = User()
        user.id = user_info.get("id")
        user.uid = user_info.get("uid")
        user.name = user_info.get("name")
        user.created = user_info.get("created")
        user.avatar = user_info.get("avatar")
        user.signature = user_info.get("signature")
        user.loc_name = user_info.get("loc_name")
        user.desc = user_info.get("desc")
        user.alt = user_info.get("alt")
        return user

# Main.
def main():
    helper = UserHelper()
    # print helper.get_current_user_id()
    # print helper.get_current_user()
    helper.upsert_user_info( helper.get_current_user_id() )

if __name__ == "__main__":
    main()
