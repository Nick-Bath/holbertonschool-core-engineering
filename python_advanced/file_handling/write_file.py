#!/bin/usr/env python
"""Module: writes a string to a text file"""


def write_file(filename="", text=""):
    """writes text to a file and returns number of chars"""
    with open(filename, mode="w", encoding="utf-8") as f:
        wrote = f.write(text)
    return wrote
