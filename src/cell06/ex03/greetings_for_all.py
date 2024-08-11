#!/bin/python3
from typing import Union


def greetings(name: Union[int, float, str] = "") -> None:
    if not isinstance(name, str):
        print("Error! It was not a string.")
    else:
        greetings = "Hello, "
        subject = name if name != "" else "noble stranger"
        print(greetings + subject + ".")


# greetings("Alexandra")
# greetings("Wil")
# greetings()
# greetings(42)
