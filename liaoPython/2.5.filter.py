#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# filter(function or None, Iterable) | similar to map function
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


output = filter(is_palindrome, range(1, 1000))
print(list(output))


# sorted | sorted(iterable, key=None, reverse=False)
## key is a function that every item in the list will call
## reverse decide the order of the sorting

