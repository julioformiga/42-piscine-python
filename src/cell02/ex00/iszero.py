#!/bin/python3
try:
    number = int(input())
except ValueError:
    exit("This input is not a number.")
print(
    f"This number is {'equal to' if number == 0 else 'different from'} zero."
)
