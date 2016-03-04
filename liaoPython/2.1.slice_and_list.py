#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# function
# isinstance(instance, type) to check the input for functions
def my_abs(value):
    if not isinstance(value, (int, float)):
        raise TypeError('bad operand type')
    if value < 0: value = -value
    return value

import math

def quadratic(a, b, c):
    # check the validity of arguments
    for e in (a, b, c):
        if not isinstance(e, (float, int)):
            raise TypeError('use integer or float as arguments')
    delta = b**2 - 4*a*c
    if delta < 0:
        print('no solution')
        return None
    elif delta == 0:
        return -b/(2*a)
    else:
        return (-b-math.sqrt(delta))/(2*a), (-b+math.sqrt(delta))/(2*a)



# function arguments
def power(x, n = 2):
    # default value of n is 2
    if n == 1: return x
    return power(x, n - 1) * x
# a famous trap
def add_end(L=None):
    if L is None: L = []
    L.append('END')
    return L
# mutable argument | func(*args)
# key word argument | func(**kw)

