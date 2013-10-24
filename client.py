#!/usr/bin/python
#
# Helper to get Douban API client.
#
# author: ze.apollo@gmail.com
#

from douban_client import DoubanClient

class ClientHelper():

    def __init__(self):
        key = '022e300c79c18fc7068a90256d44af55'
        secret = '11c8bcbac80e8085'
        callback = 'http://www.douban.com'
        scope = 'douban_basic_common,community_basic_user'
        self.client = DoubanClient( key, secret, callback, scope )
        self.client.auth_with_token( '2090de6f59fea80a61b29b4e0dfbf81e' )

def main():
    helper = ClientHelper()
    print helper.client.user.me

if __name__ == "__main__":
    main()
