#!/usr/bin/env python3

def uppercase(str):

    new_string = ""

    for letter in str:
        if ord(letter) in range(ord('a'), ord('z') + 1):
            new_string += chr(ord(letter) - 32)
        else:
            new_string += (letter)
    print("{}".format(new_string))
