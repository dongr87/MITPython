#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# basic I/O
name=input('Please enter your name: ')
print('\nHello', name)


# Data Structure
# r' ', no escaping
# print multiple line '''...'''

parag ='I\'m okay'
print(parag)

# Variables
# Dynamic languages VS. Static languages | variables' data type
# constant variables => all capitalized

# String and Unicode
# ord() | convert character into integer ordinal
# chr() | convert integer ordinal into character
# '\u4e2d\u6587' => hexa to character using '\u'
# decode (unicode to ascii/utf-8)and encode (ascii/utf-8 to unicode)
# zhanweifu

print('%2d-%02d' % (3, 1))
x = 10/3
print(x)
print('%.1f' % x)
print('growth rate: %d%%' % 7)


# List and Tuple
# append() | insert() | pop()


# Dictionary (key => value)
d = {'Michael': 98, 'Bob': 78, 'Tracy': 88}
print(d['Michael'])
d['Micheal'] = 95
d['Jack'] = 99
# To check if the key is in dictionary
'Jack' in d
d.get('Jack', -1)
# pop(key) ==> to remove a value
# !Key in the dictionary should be immutable

# set | non-repetable, only keys
s = set([1,3,2])
# add(key) method to add element to set
# remove(key)
s1 = set([1,2,3])
s2 = set([2,3,4])
s1 & s2
s1 | s2
