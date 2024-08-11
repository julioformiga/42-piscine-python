#!/bin/python3
import sys

if len(sys.argv) < 2:
    exit("none")
array_with_ism = []
for i in range(1, len(sys.argv)):
    if sys.argv[i][-3:] != "ism":
        array_with_ism.append(sys.argv[i])
print("ism\n".join(array_with_ism) + "ism")
