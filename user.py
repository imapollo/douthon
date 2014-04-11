#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# All about users.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient
from solid_data import SolidData

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
# Data Persistence for User.
#
class UserData( SolidData ):

    def __init__( self ):
        self.helper = ClientHelper()
        mongodb = MongoDBClient()
        self.db = mongodb.db

    def get_data_from_douban( self, id ):
        user = self.helper.client.user.get( id )
        return user

    def get_data_from_mongodb( self, id ):
        db_users = self.db.users
        return db_users.find_one( { "id": "%s" % id } )

    def upsert_data_into_mongo( self, data ):
        db_users = self.db.users
        if ( db_users.find_one( { "id": "%s" % data[ 'id' ] } ) ):
            pass
        else:
            user = self.deserialize_user_info( data )
            db_users.insert( self.serialize_user( user ) )

    def get_current_user( self ):
        return self.helper.client.user.me

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

#
# Helper of user.
#
class UserHelper:

    # Initiate user.
    def __init__( self ):
        self.user_data = UserData()
        self.current_user = self.user_data.get_current_user()

    # Get the current user ID.
    def get_current_user_id( self ):
        return self.current_user[ 'id' ]

    # Get the json of current user.
    def get_current_user( self ):
        return self.current_user

    # Get full information of a user from Douban API.
    def get_user_info( self, user_id ):
        return self.user_data.get_data( user_id )

    # Get full information for the current user from Douban API.
    def get_current_user_info( self ):
        return self.get_user_info( self.get_current_user_id() )

# Main.
def main():
    helper = UserHelper()
    # print helper.get_current_user_id()
    # print helper.get_current_user()
    # helper.upsert_user_info( helper.get_current_user_id() )

if __name__ == "__main__":
    main()
