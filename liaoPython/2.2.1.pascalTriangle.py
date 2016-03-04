#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pascal Triangle
# Solution1 | normal solution
def pTri1():
    realList = [1]
    yield realList
    while 1:
        tempList = [1]
        n = len(realList)
        i = 1
        while i < n:
            tempList.append(realList[i-1]+realList[i])
            i += 1
        tempList.append(1)
        realList = tempList
        yield realList

# solution 2 using list generator
def pTri2():
    b = [1]
    while 1:
        yield b
        b = [1] + [b[i]+b[i+1] for i in range(len(b)-1)] + [1]

# solution 3 using zip()
def pTri3():
    b = [1]
    while 1:
        yield b
        b = [x+y for x, y in zip(b+[0], [0]+b)]

