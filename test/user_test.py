#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Tests for user.py.
#
# author: ze.apollo@gmail.com
#

import sys
sys.path.insert( 0, '/home/minjzhang/douthon' )

from user import UserHelper
import random
import unittest

class TestUserHelper( unittest.TestCase ):

    def setUp( self ):
        self.helper = UserHelper()

    def test_get_current_user_id( self ):
        id = self.helper.get_current_user_id()
        self.assertEqual( id, '1315244' )

    def test_get_current_user_info( self ):
        user_info = self.helper.get_current_user_info()
        self.assertEqual( user_info[ 'id' ], '1315244' )
        self.assertEqual( user_info[ 'name' ], 'Apollo' )

    def tearDown( self ):
        pass

if __name__ == '__main__':
    unittest.main()
