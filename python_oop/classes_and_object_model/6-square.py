#!/usr/bin/env python3
"""Module: Square """


class Square():
    """Creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        sum = self.size * self.size
        return sum

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, v):
        if (type(v) is not tuple or len(v) != 2 or
        not all(type(n) is int for n in v) or v[0] < 0 or v[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = v

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for z in range(self.position[1]):
                print()
            for x in range(self.size):
                for y in range(self.position[0]):
                    print("", end="")
                for x in range(self.size):
                    print("#", end="")
                print()

    def __str__(self):
        result = ""

        if self.size == 0:
            return result

        for z in range(self.position[1]):
            result += "\n"

        for x in range(self.size):
            for y in range(self.position[0]):
                result += "_"
            for a in range(self.size):
                result += "#"
            if x != self.size - 1:
                result += "\n"

        return result

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
