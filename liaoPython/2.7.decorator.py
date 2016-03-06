#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper
# functools.wraps() is to switch wrapper.__name__ to func.__name__

@log
def now():
    print('2016-3-4')

# Homework
def headTail(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('Begin Call')
        f = func(*args, **kw)
        print('End Call')
        return f
    return wrapper

@headTail
def now1():
    print('2001-1-1')

# Overload the log decorator
def logAdv(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('Call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper

@logAdv('execute')
def test1():
    print('test1')

@logAdv
def test2():
    print('test2')


if __name__ == '__main__':
    test1()
    print('\n')
    test2()
