#!/usr/bin/python

from douban_client import DoubanClient
from client import ClientHelper

class Album():
    def __init__():
        pass
    
def main():
    helper = ClientHelper()
    # print helper.client.user.me
    # print helper.client.album.liked_list( '1315244' )
    # print helper.client.user.get( '1315244' )
    print helper.client.album.get( '1371306' )

if __name__ == "__main__":
    main()
