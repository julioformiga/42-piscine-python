#!/bin/python3
import sys

if len(sys.argv) < 2:
    print("none")
    exit(1)


def shrink(str: str) -> str:
    return str[:8]


def enlarge(str: str) -> str:
    str = str + "Z" * (8 - len(str))
    return str


for i in sys.argv[1:]:
    print(shrink(i)) if len(i) > 8 else print(enlarge(i))
