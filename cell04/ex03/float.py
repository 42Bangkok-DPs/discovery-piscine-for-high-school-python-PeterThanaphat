#!/usr/bin/env python3
user_input = input("Give me a number: ")

try:
    number = float(user_input)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except:
    print("That's not a valid number.")
