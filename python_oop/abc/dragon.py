#!/usr/bin/env python3

"""Module: making a dragon with mixins"""


class SwimMixin:
    """Mixin for the swim behaviour"""
    def swim():
        print("The creature swims!")


class FlyMixin:
    """Mixin for the fly behaviour"""
    def fly():
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon Behaviour"""
    def roar():
        print("The dragon roars!")
