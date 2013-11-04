#!/usr/bin/python
# -*- coding: utf-8 -*-

from client import ClientHelper

class Album():
    def __init__():
        pass
    
def main():
    helper = ClientHelper()
    # print helper.client.user.me
    # print helper.client.user.get( '1315244' )
    # utf8stdout = open("abc", 'w')
    # print helper.client.book.list( '1315244' )[1]['summary']
    print helper.client.book.get( '1626392' )['summary']

if __name__ == "__main__":
    main()
