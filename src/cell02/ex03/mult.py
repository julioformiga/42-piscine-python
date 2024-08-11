#!/bin/python3
try:
    first_number = int(input("Enter the first number:\n"))
    second_number = int(input("Enter the second number:\n"))
except ValueError:
    exit("This input is not a number.")
number = first_number * second_number
print(f"{first_number} x {second_number} = {number}")
if number == 0:
    print("The result is positive and negative.")
else:
    print(f"The result is {'positive' if number > 0 else 'negative'}.")
