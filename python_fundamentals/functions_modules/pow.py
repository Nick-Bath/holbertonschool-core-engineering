#!/usr/bin/env python3

def pow(a, b):
    c = a
    if b == 0:
        return 1
    elif b < 0:
        for i in range(1, abs(b)):
            c = c * a
        return (1/c)
    else:
        for i in range(1, b):
            c = c * a
    return c
