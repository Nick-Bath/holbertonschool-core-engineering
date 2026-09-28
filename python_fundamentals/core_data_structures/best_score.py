#!/usr/bin/env python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    else:
        largest = max(a_dictionary, key=a_dictionary.get)
        return largest
