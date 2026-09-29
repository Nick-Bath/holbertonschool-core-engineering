#!/usr/bin/env python3
"""Module: Square """


class Square():
    """Creates a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, d):
        if not d:
            raise TypeError("size must be an integer")
        self.__size = d

    @property
    def value(self):
        return self.__size

    @value.setter
    def value(self, v):
        if not (v >= 0):
            raise ValueError("size must be >= 0")
        self.__size = v
