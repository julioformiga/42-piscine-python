#!/bin/python3


class Hello:
    def __init__(self, initial=None):
        self.init = initial if initial else "Hello, everyone!"

    def hello(self):
        print(self.init)


def hello():
    Hello().hello()


if __name__ == "__main__":
    hello()
