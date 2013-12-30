#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Helper to get Douban API client.
#
# author: ze.apollo@gmail.com
#

from douban_client import DoubanClient

class ClientHelper():

    # Initiate the Douban API v2.0 client with OAuth.
    def __init__( self ):
        key = '022e300c79c18fc7068a90256d44af55'
        secret = '11c8bcbac80e8085'
        callback = 'http://www.douban.com'
        scope = 'douban_basic_common,community_basic_user'
        self.client = DoubanClient( key, secret, callback, scope )
        self.client.auth_with_token( '2bc683ca91a8985483538b5fb4f9c8fc' )

# Main.
def main():
    helper = ClientHelper()
    print helper.client.user.me

if __name__ == "__main__":
    main()
