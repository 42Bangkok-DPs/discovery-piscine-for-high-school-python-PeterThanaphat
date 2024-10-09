#!/usr/bin/env python3

def greetings(n="noble stranger"):
    if not isinstance(n, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {n}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)




