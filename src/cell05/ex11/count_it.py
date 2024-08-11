#!/bin/python3
import sys

if len(sys.argv) < 2:
    exit("none")
print(f"parameters: {len(sys.argv) - 1}")
for p in sys.argv[1:]:
    print(f"{p}: {len(p)}")
