#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    self.age = 10

    # getter method
    @property
    def score(self):
        return self._score

    # setter method
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # read-only property
    @property
    def age(self):
        return self.age


# homework from webpage
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self.width * self.height
