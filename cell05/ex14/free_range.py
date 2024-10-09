#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        last = int(sys.argv[2])
        x = list(range(start, last + 1))
        print(x)

    except:
        print("none")

