#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    x = sys.argv[1]
    y = x.count('z')
    
    if y == 0:
        print("none")
    else:
        print("z" * y)
