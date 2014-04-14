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

    def test_list_book_id( self ):
        book_ids = self.helper.list_book_id()
        self.assertTrue( len( book_ids ) > 400 )
        self.assertTrue( '3354855' in book_ids )

    def test_list_book_names( self ):
        book_names = self.helper.list_book_names()
        self.assertTrue( len( book_names ) > 400 )

    def test_get_book_read_trends( self ):
        read_trends = self.helper.get_book_read_trends( '1315244' )
        self.assertTrue( '2011-08', read_trends )
        self.assertTrue( '2012-10', read_trends )
        self.assertTrue( '2013-04', read_trends )
        read_trends_2011_08 = read_trends[ '2011-08' ]
        self.assertTrue( '3354855' in read_trends_2011_08[ 'books' ] )
        self.assertTrue( 'linux' in read_trends_2011_08[ 'tags' ] )
        self.assertTrue( 'Bill Lubanovic' in read_trends_2011_08[ 'authors' ] )

    def tearDown( self ):
        pass

if __name__ == '__main__':
    unittest.main()
