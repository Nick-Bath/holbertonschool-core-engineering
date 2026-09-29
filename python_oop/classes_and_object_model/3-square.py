#!/usr/bin/env python3
"""Module: Square """


class Square():
    """Creates a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        sum = self.size * self.size
        return sum

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, d):
        if type(d) is not int:
            raise TypeError("size must be an integer")
        if not (d >= 0):
            raise ValueError("size must be >= 0")
        self.__size = d
