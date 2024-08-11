#!/bin/python3
import sys

if len(sys.argv) > 2:
    print("\n".join([i for i in sys.argv[:0:-1]]))
else:
    print("none")
