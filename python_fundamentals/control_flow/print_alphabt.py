#!/usr/bin/env python3

i = 0
while i < 26:
    if i == 4 or i == 16:
        i += 1
    print("{}".format(chr(ord('a') + i)), end="")
    i += 1
