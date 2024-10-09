#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    x = sys.argv[1]
    y = sys.argv[2]
    z = re.findall(x, y)

    if z:
        print(len(z))
    else:
        print("none")


