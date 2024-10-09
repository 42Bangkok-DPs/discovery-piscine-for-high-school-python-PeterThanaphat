#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if len(arg) > 8:
            print(arg[:8])
        elif len(arg) < 8:
            print(arg + 'Z' * (8 - len(arg)))
        else:
            print(arg)
