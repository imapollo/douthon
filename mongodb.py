#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymongo import MongoClient

class MongoDBClient:
    def __init__(self):
        self.db = MongoClient('localhost', 27017).test

def main():
    mongodb = MongoDBClient()
    db = mongodb.db
    users = db.users
    print users.find_one( {"name": "xia"} )

if __name__ == "__main__":
    main()
