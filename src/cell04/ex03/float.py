#!/bin/python3
try:
    number = float(input("Give me a number: "))
except ValueError:
    exit("This input is not a number.")
i, d = divmod(number, 1)
print(f"This number is a {'integer' if d == 0 else 'decimal'}.")
