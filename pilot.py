#!/usr/bin/python

from douban_client import DoubanClient

def main():
    key = '022e300c79c18fc7068a90256d44af55'
    secret = '11c8bcbac80e8085'
    callback = 'http://www.douban.com'
    scope = 'douban_basic_common,community_basic_user,book_basic_r'

    client = DoubanClient( key, secret, callback, scope )

    # Following is to get the token at first time
    print 'Go to the following link in your browser:'
    print client.authorize_url
    code = raw_input( 'Enter the verification code:' )
    client.auth_with_code( code )
    print client.access_token.token

    # Following is to auth with the token already got
    # client.auth_with_token( '2090de6f59fea80a61b29b4e0dfbf81e' )
    print client.user.me

if __name__ == "__main__":
    main()
