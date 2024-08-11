#!/bin/python3
import sys

if len(sys.argv) != 2 or "z" not in sys.argv[1]:
    exit("none")
print("".join(i for i in sys.argv[1] if i == "z"))
