#!/usr/bin/env python3
user_input = input("What you gotta say? : ")
while True :
    if user_input.strip().upper() == "STOP":
        break
    else :
        user_input = input("I got that! Anything else? : ")

