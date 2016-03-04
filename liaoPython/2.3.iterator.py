#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Iterator | object that you can call next() to return next value
## str, list, dict are Iterable, but not Iterator | Iterator is a data flow, the length should not be fixed
## iter() to convert argument into Iterator (list, str, dict)

# Functional programming | allow passing a function to another function and return a function
# Side effect of functions

# Higher order function
## variable can point to functions | f = abs, f(8) does the same thing with abs(8)
## the name of the function is also variable
__builtins__.abs = 10
## pass in function
def add(x, y, f):
    return f(x) + f(y)
