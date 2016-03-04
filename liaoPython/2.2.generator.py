#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Generator

g = (x*x for x in range(10))
next(g)
# yield | transform method into generator
def fib(n):
    c, a, b = 0, 0, 1
    while c < n:
        yield b
        a, b = b, a+b
        c += 1
    return 'Done'

# Generator (run at next() | return at yield) VS Method (run in order | return at return)
# the return value of fib(n) is in e.value of StopIteration

g = fib(6)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

