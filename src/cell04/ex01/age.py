#!/bin/python3
try:
    age = int(input("Please tell me your age: "))
except ValueError:
    exit("This input is not a int number.")
if age <= 0:
    exit("Invalid age.")
print(f"You are currently {age} years old.")
i = 1
while i <= 3:
    print(f"In {i * 10} years, you'll be {age + i * 10} years old.")
    i += 1
