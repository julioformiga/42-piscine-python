import src.cell07.ex00.your_namebook as ex00
import src.cell07.ex01.family_affairs as ex01
import src.cell07.ex02.help_your_professor as ex02
import src.cell07.ex03.persons_of_interest as ex03


async def test_cell07_ex00():
    assert callable(ex00.array_of_names)
    persons = {"jean": "valjean"}
    assert ex00.array_of_names(persons) == ["Jean Valjean"]
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier",
    }
    assert ex00.array_of_names(persons) == [
        "Jean Valjean",
        "Grace Hopper",
        "Xavier Niel",
        "Fifi Brindacier",
    ]


async def test_cell07_ex01():
    assert callable(ex01.find_the_redheads)
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
    }
    assert ex01.find_the_redheads(dupont_family) == [
        "florian",
    ]
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red",
    }
    assert ex01.find_the_redheads(dupont_family) == [
        "florian",
        "david",
        "franck",
    ]


async def test_cell07_ex02():
    assert callable(ex02.average)
    class_3B = {"marine": 18, "jean": 15, "coline": 8, "luc": 9}
    assert ex02.average(class_3B) == 12.5
    class_3C = {"quentin": 17, "julie": 15, "marc": 8, "stephanie": 13}
    assert ex02.average(class_3C) == 13.25


async def test_cell07_ex03(capsys):
    assert callable(ex03.famous_births)

    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
    }
    expected = "Ada Lovelace is a great scientist born in 1815.\n"
    expected += "Lise Meitner is a great scientist born in 1878.\n"
    expected += "Cecila Payne is a great scientist born in 1900.\n"
    expected += "Grace Hopper is a great scientist born in 1906.\n"
    ex03.famous_births(women_scientists)
    captured = capsys.readouterr()
    assert captured.out == expected
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "samantha": {
            "name": "Samantha Cristoforetti",
            "date_of_birth": "1977",
        },
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"},
    }
    expected = "Ada Lovelace is a great scientist born in 1815.\n"
    expected += "Lise Meitner is a great scientist born in 1878.\n"
    expected += "Cecila Payne is a great scientist born in 1900.\n"
    expected += "Grace Hopper is a great scientist born in 1906.\n"
    expected += "Samantha Cristoforetti is a great scientist born in 1977.\n"
    ex03.famous_births(women_scientists)
    captured = capsys.readouterr()
    assert captured.out == expected
