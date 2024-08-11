#!/bin/python3
try:
    number = int(input("Enter a number\n"))
except ValueError:
    exit("This input is not a number.")
for i in range(0, 10):
    print(f"{i} x {number} = {i * number}")
