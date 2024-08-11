#!/bin/python3


def famous_births(persons: dict) -> None:
    scientist = sorted(
        persons.items(), key=lambda item: item[1]["date_of_birth"]
    )
    for value in scientist:
        n = value[1]["name"]
        d = value[1]["date_of_birth"]
        print(f"{n} is a great scientist born in {d}.")


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
}
famous_births(women_scientists)
