#!/usr/bin/env python3

i = 0
while (i <= 9):
    j = 0
    while (j <= 9):
        if j == 9 and i == 9:
            print("{}{}".format(i, j))
        print("{}{}, ".format(i, j), end="")
        j += 1
    i += 1


