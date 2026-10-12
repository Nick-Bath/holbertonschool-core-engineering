#!/usr/bin/env python3
"""Module: Reads given file"""


def read_file(filename=""):
    """reads given file and prints to stdout"""
    with open(filename) as f:
        read_data = f.read()
    print(read_data)
