#!/bin/python3
import sys

if len(sys.argv) != 2:
    exit("none")
param = input("What was the parameter? ")
print(f"{'Nope, sorry...' if sys.argv[1] != param else 'Good job!'}")
