#!/bin/python3
try:
    first_number = int(input("Give me the first number: "))
    second_number = int(input("Give me the second number: "))
except ValueError:
    exit("This input is not a number.")
print("Thank you!")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} / {second_number}", end="")
if second_number == 0:
    print(" = Error (division by zero)")
else:
    print(f" = {(first_number / second_number):0.0f}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
