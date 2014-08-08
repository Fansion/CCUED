#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test file'

__author__ = 'Frank Fu'

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

'''
The doctest module searches for pieces of text that 
look like interactive Python sessions in docstrings,
 and then executes those sessions to verify that they
  work exactly as shown.

'''
def square(x):
    """Squares x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()