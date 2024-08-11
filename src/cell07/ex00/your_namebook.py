#!/bin/python3


def array_of_names(persons: dict) -> list:
    return [f"{key.title()} {value.title()}" for key, value in persons.items()]


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier",
}
print(array_of_names(persons))
