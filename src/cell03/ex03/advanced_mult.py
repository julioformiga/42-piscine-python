#!/bin/python3
import sys

if sys.argv[1:]:
    exit("none")

i = 0
while i < 11:
    print(f"Table de {i}:", end="")
    j = 0
    while j < 11:
        print(f" {i * j}", end="")
        j += 1
    print()
    i += 1
