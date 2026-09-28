#!/usr/bin/env python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except Exception:
        print("{}".format("Inside result: None"))
        return None
    finally:
        print("{Inside Result: }".format(result))
    return result
