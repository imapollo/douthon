#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tests for book_collection.py.
#
# author: ze.apollo@gmail.com
#

import sys
sys.path.insert( 0, '/home/minjzhang/douthon' )

from book_collection import BookCollectionHelper
import random
import unittest

class TestBookCollectionHelper( unittest.TestCase ):

    def setUp( self ):
        self.helper = BookCollectionHelper()

    def test_list_current_user_books( self ):
        book_collections = self.helper.list_current_user_books()
        self.assertTrue( len( book_collections ) > 400 )

    def tearDown( self ):
        pass

if __name__ == '__main__':
    unittest.main()
