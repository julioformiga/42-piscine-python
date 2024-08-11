#!/bin/python3
import sys

if len(sys.argv) < 2:
    exit("none")


def downcase_it(str: str) -> str:
    return str.lower()


for i in range(1, len(sys.argv)):
    print(downcase_it(sys.argv[i]))
