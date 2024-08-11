#!/bin/python3
import sys


def add_one(number: int) -> int:
    number += 1
    return number


def main():
    number = 1

    print(number)
    add_one(number)
    print(number)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("none")
        exit(1)

    main()
