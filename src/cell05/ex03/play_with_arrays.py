#!/bin/python3
ar = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"{ar}")
ar_set = {i + 2 for i in ar if i > 5}
print(f"{ar_set}")
