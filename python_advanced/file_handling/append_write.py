#!/usr/bin/env python3
"""Module: appends a string to a text file"""


def append_write(filename="", text=""):
    """appends text to a file and returns number of chars"""
    with open(filename, mode="a", encoding="utf-8") as f:
        wrote = f.write(text)
    return wrote
