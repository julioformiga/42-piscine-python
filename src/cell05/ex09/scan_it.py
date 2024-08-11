#!/bin/python3
import sys
# import re

if len(sys.argv) != 3:
    print("none")
else:
    print(f"{sys.argv[2].count(sys.argv[1])}")
    # print(f"{len(re.findall(sys.argv[1], sys.argv[2]))}")
