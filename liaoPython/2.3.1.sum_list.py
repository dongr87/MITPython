#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# recursively sum the list
def sumList(xs):
    sum = 0
    for e in xs:
        if type(e) is list:
            print(("Calling sumList(%s) recursively" %e))
            v = sumList(e)
            print("sumList(%s) returned %s" %(e, v))
            sum += v
        else:
            sum += e
    return sum

testData = [10, [20, 30, [40], 50], 60]
print("Calling sumList(%s)" % testData)
result = sumList(testData)
print(("Final sum of all numbers in initial list is %s" % result))
