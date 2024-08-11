#!/bin/python3
try:
    number = int(input("Enter a number less than 25\n"))
except ValueError:
    exit("This input is not a number.")
if number > 25:
    exit("Error")
while number <= 25:
    print(f"Inside the loop, my variable is {number}")
    number += 1
