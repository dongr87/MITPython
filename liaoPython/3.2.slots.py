#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# example class
class Student(object):
    pass

# you can bind an attribute to an instance
s = Student()
s.name = 'Micheal'
print(s.name)

# you can also bind a method to an instance
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # bind set_age method to instance s
s.set_age(25) # call the method
s.age # test the result
# this won't be effect on another instance

# you can also bind a method or an attribute to a class
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, Student)

## About __slots__ : restrict attributes that can be added to the class
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99 # cannot bind attribute 'score' to Student

# __slots__ won't be inherited by subclass
class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
