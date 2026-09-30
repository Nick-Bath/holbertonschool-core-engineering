#!/usr/bin/env python3

from abc import ABC, abstractmethod

"""Module: Animal Abstract Class"""


class Animal(ABC):
    """Defining Base Animal Behaviour"""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """Defines Dog Behaviour"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Defines Cat Behaviour"""
    def sound(self):
        return "Meow"
