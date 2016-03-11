#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __str__
# define the __str__ function and by print statement to compute the informal string representation
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

# __repr__
# define the __repr__ function and by string conversions to compute the official string representation

# __iter__
# build an iterator for the object

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self # instance itself is the iterator, so return itself

# difference between python3 (__next__) and python2 (next)
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a>1000:
            raise StopIteration
        return self.a

for i in Fib():
    print(i)

# __getitem__
# called to implement evaluation of self[key], the accepted keys should be intergers and slice objects
class Fib1():
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

f = Fib1()
print(f[0])
print(f[100])

## For slice method in list object, we have to rewrite the method
class Fib2():
    def __getitem__(self, n):
        if isinstance(n, int): # n is an index
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice): # n is a slice
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib2()
print(f[0:5])
print(f[:10])

# if object is a dictionary, the argument of __getitem__() can also be the key to dict, such as str
# __setitem__ is called to implement assignment to self[key]
# __delitem__ called to impolemnt deletion of self[key]


# __getattr__
# called when an attribete lookip has not found the attribute in the usual places
class Student1(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        # you can return a value for it
        if attr == 'score':
            return 99
        # you can also return a method
        if attr == 'age':
            return lambda: 25
        # throw the AttributeError for general call
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# Application: RESTful development, handle the dynamic URL
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

# __call__
# called when the instance is "called" as a function, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...)
# practice Chain 2
class Chain2(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        return Chain2('%s/%s' % (self._path, attr))

    def __str__(self):
        return self._path

    def __call__(self, param):
        return Chain2('%s/%s' % (self._path, str(param)))

    __repr__ = __str__

print(Chain2().users('micheal').age(23).repos)

# callable method
# To check if the object or a function is callable
