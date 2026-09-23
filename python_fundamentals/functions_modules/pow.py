#!/usr/bin/env python3

def pow(a, b):
    c = a
    if b == 0:
        return 1
    for i in range(1, b):
        c = c * a
    return c