#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tests for user.py.
#
# author: ze.apollo@gmail.com
#

import sys
sys.path.insert( 0, '/home/minjzhang/douthon' )

from book import BookHelper
import random
import unittest

class TestUserHelper( unittest.TestCase ):

    def setUp( self ):
        self.helper = BookHelper()

    def test_get_book_info( self ):
        book_info = self.helper.get_book_info( '1779429' )
        self.assertEqual( book_info[ 'title' ],
                'UNIX and Linux System Administration Handbook' )
        self.assertEqual( book_info[ 'pubdate' ], '2010-7-24' )
        self.assertEqual( book_info[ 'id' ], '1779429' )

    def test_get_book_authors( self ):
        book_authors = self.helper.get_book_authors( '1779429' )
        self.assertTrue( 'Evi Nemeth' in book_authors )
        self.assertTrue( 'Garth Snyder' in book_authors )
        print book_authors

    def tearDown( self ):
        pass

if __name__ == '__main__':
    unittest.main()
