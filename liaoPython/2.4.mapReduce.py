#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map/reduce
'''
map(f, *Iterables) # f is a function, Iterable is an iterable object
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
reduce(lambda x, y: 10*x + y, [1,3,5,7,9])
'''

# practices about reduce/map
## a sample of string to integer using reduce/map
from functools import reduce

def str2int(string):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(lambda x, y: 10*x+y, map(char2num, string))

def normalize(name):
    return name[0].upper() + name[1:].lower()

def prod(L):
    return reduce(lambda x, y: x*y, L)


## convert string to float
def str2float(s):
    if '.' not in s:
        return str2int(s)
    L = s. split('.')
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    l1 = reduce(lambda x, y: 10*x + y, map(char2num, L[0]+L[1]))
    l2 = 10 ** (len(L[1])) * 1.0
    return l1/l2

print(str2float('134.23'))
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))


# another solution from website

from functools import reduce

def str2float(s):
    L = s.split('.')
    F = L[1]
    def fn1(x,y):
        return x*10 + y
    def fn2(x,y):
        return x/10 + y
    def char2num(s):
        return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}[s]
    return reduce(fn1, map(char2num,L[0])) + 0.1*reduce(fn2,map(char2num,F[::-1]))

