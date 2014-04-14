#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Data parent class that always changes.
#
# author: ze.apollo@gmail.com
#

from client import ClientHelper
from mongodb import MongoDBClient

class ChangingData:

    def get_data( self, id ):
        data = self.get_data_from_mongodb( id )
        if ( data ):
            return data
        else:
            data = self.get_data_from_douban( id )
            self.upsert_data_into_mongo( data )

