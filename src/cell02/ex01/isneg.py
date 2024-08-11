#!/bin/python3
try:
    number = int(input())
except ValueError:
    exit("This input is not a number.")
if number == 0:
    print("This number is both positive and negative.")
else:
    print(f"This number is {'positive' if number > 0 else 'negative'}.")
