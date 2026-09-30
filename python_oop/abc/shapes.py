#!/usr/bin/env python3

from abc import ABC, abstractmethod
from math import pi


"""Module: Shapes"""


class Shape(ABC):
    """Base behaviour for shapes"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle shape behaviour"""
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * pi

    def perimeter(self):
        return 2 * self.radius * pi


class Rectangle(Shape):
    """Rectangle shape behaviour"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)


def shape_info(x):
    x.area()
    x.perimeter()
    print("Area: {}".format(x.area()))
    print("Perimeter: {}".format(x.perimeter()))
