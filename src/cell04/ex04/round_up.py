#!/bin/python3
from math import ceil

try:
    number = float(input("Give me a number: "))
except ValueError:
    exit("This input is not a number.")

print(int(ceil(number)))
