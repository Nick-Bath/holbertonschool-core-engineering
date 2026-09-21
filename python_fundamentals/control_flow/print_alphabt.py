#!/usr/bin/env python3

lowercase_alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
i = 0
while i < 26:
    if i == 4 or i == 16:
        i += 1
    print(f"{chr(ord('a') + i)}", end="")
    i += 1
