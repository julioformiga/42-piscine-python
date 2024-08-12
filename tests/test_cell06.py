import subprocess
import src.cell06.ex00.hello_all as ex00
import src.cell06.ex01.upcase_it as ex01
import src.cell06.ex03.greetings_for_all as ex03
import src.cell06.ex05.scope_that as ex05


async def test_cell06_ex00(capfd):
    ex00.hello()
    stdout, stderr = capfd.readouterr()
    assert stdout == "Hello, everyone!\n"


async def test_cell06_ex01():
    assert ex01.upcase_it("hello") == "HELLO"
    assert ex01.upcase_it("42") == "42"
    assert ex01.upcase_it("42 Firenze") == "42 FIRENZE"


async def test_cell06_ex02():
    file = "./src/cell06/ex02/downcase_all.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "42 Firenze"], capture_output=True, text=True
    )
    assert result.stdout == "42 firenze\n"
    result = subprocess.run(
        ["python3", file, "42 Firenze", "42 NetWork"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "42 firenze\n42 network\n"
    result = subprocess.run(
        ["python3", file, "HELLO WORLD", "I understood Arrays well!"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "hello world\ni understood arrays well!\n"


async def test_cell06_ex03(capfd):
    ex03.greetings("Alexandra")
    stdout, stderr = capfd.readouterr()
    assert stdout == "Hello, Alexandra.\n"
    ex03.greetings("Wil")
    stdout, stderr = capfd.readouterr()
    assert stdout == "Hello, Wil.\n"
    ex03.greetings()
    stdout, stderr = capfd.readouterr()
    assert stdout == "Hello, noble stranger.\n"
    ex03.greetings(42)
    stdout, stderr = capfd.readouterr()
    assert stdout == "Error! It was not a string.\n"


async def test_cell06_ex04():
    file = "./src/cell06/ex04/methods_everywhere.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "lol"], capture_output=True, text=True
    )
    assert result.stdout == "lolZZZZZ\n"
    result = subprocess.run(
        ["python3", file, "lol", "physically"], capture_output=True, text=True
    )
    assert result.stdout == "lolZZZZZ\nphysical\n"
    result = subprocess.run(
        ["python3", file, "lol", "physically", "backpack"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "lolZZZZZ\nphysical\nbackpack\n"


async def test_cell06_ex05():
    file = "./src/cell06/ex05/scope_that.py"
    result = subprocess.run(
        ["python3", file, "one"], capture_output=True, text=True
    )
    assert result.stdout == "none\n"
    assert callable(ex05.add_one), "add_one() not exists"
