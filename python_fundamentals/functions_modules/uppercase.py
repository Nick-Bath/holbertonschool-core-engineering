#!/usr/bin/env python3

def uppercase(str):
    for letter in str:
        if ord(letter) in range(ord('A'), ord('Z') + 1):
            print("{}".format(letter), end="")
        elif ord(letter) in range(ord('a'), ord('z') + 1):
            print("{}".format(chr(ord(letter) - 32)), end="")
        else:
            print(letter, end="")
    print()
