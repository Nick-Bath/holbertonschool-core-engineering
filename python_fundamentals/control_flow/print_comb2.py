#!/usr/bin/env python3

i = 0
j = 0
while (i <= 9):
    if j == 9:
        i += 1
        j = 0
    else:
        print("{}{}, ".format(i, j), end="")
        j += 1
        if j == 9 and i == 9:
            print("{}{}".format(i, j))
        
     

