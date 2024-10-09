#!/usr/bin/env python3import sys
if len(sys.argv) > 1:
    print("none")
 
    

for i in range(11):
    table = [i * j for j in range(11)]
    print(f"Table de {i}: {' '.join(map(str, table))}")
