#!/bin/python3
import sys

if len(sys.argv) != 3:
    exit("none")
try:
    print(f"{[i for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1)]}")
except ValueError:
    exit("Invalid numbers.")
