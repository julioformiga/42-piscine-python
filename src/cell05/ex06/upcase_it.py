#!/bin/python3
import sys

print(f"{'none' if len(sys.argv) != 2 else sys.argv[1].upper()}")
