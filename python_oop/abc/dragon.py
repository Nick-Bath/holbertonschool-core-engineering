#!/usr/bin/env python3

"""Module: making a dragon with mixins"""


class SwimMixin:
    """Mixin for the swim behaviour"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin for the fly behaviour"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon Behaviour"""
    def roar(self):
        print("The dragon roars!")
