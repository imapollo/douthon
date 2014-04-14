#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Douban Call.
#
# author: ze.apollo@gmail.com
#

def douban_limited_call( function ):
    def _douban_limited_call( *args, **kw ):
        print "via douban limited call"
        result = function( *args, **kw )
        return result
    return _douban_limited_call
