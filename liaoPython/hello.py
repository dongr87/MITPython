#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'Dong Wang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, World!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

'''
If the python interpreter is running the module(the source file)
as the main program, it sets the special name variable
to have a value "main".
If this file is being imported from another module,
name will be set to the module's name.

In other words, by assign __main__ to __name__ ,
you don't have to call the test() method by yourself.
'''
if __name__ == '__main__':
    test()
