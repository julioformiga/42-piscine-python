import subprocess
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("42 Firenze", "42 FIRENZE\n"),
        ("Scuola 42 Firenze", "SCUOLA 42 FIRENZE\n"),
    ],
)
def test_cell04_ex00(input, expected):
    file = "./src/cell04/ex00/upcase_it.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    assert result.stdout == "Give me a word: " + expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("-42", "Invalid age.\n"),
        ("20", ""),
        ("Wil", "This input is not a int number.\n"),
    ],
)
def test_cell04_ex01(input, expected):
    file = "./src/cell04/ex01/age.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        prompt = "Please tell me your age: "
        prompt += f"You are currently {input} years old.\n"
        i = 1
        while i <= 3:
            prompt += f"In {i * 10} years, you'll be {int(input) + i * 10} years old.\n"
            i += 1
        assert result.stdout == prompt


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        ("2", "3", "The result is positive.\n"),
        ("2", "-3", "The result is negative.\n"),
        ("2", "0", "The result is positive and negative.\n"),
        ("a", "a", "This input is not a number.\n"),
        ("a", "2", "This input is not a number.\n"),
        ("2", "a", "This input is not a number.\n"),
    ],
)
def test_cell04_ex02(input1, input2, expected):
    file = "./src/cell04/ex02/calculator.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input1}\n{input2}\n",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        prompt = (
            "Give me the first number: Give me the second number: Thank you!\n"
        )
        prompt += f"{input1} + {input2} = {int(input1) + int(input2)}\n"
        prompt += f"{input1} - {input2} = {int(input1) - int(input2)}\n"
        if input2 == "0":
            prompt += f"{input1} / {input2} = Error (division by zero)\n"
        else:
            prompt += (
                f"{input1} / {input2} = {(int(input1) / int(input2)):0.0f}\n"
            )
        prompt += f"{input1} * {input2} = {int(input1) * int(input2)}\n"
        assert result.stdout == prompt


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Wil", "This input is not a number.\n"),
        ("-42", "This number is a integer.\n"),
        ("0", "This number is a integer.\n"),
        ("42", "This number is a integer.\n"),
        ("42.00", "This number is a integer.\n"),
        ("42.41", "This number is a decimal.\n"),
    ],
)
def test_cell04_ex03(input, expected):
    file = "./src/cell04/ex03/float.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        assert result.stdout == "Give me a number: " + expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Wil", "This input is not a number.\n"),
        ("-42", "-42\n"),
        ("0.0001", "1\n"),
        ("42", "42\n"),
        ("42.00", "42\n"),
        ("42.41", "43\n"),
    ],
)
def test_cell04_ex04(input, expected):
    file = "./src/cell04/ex04/round_up.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        assert result.stdout == "Give me a number: " + expected


@pytest.mark.parametrize(
    "input",
    [
        ("Wil"),
        ("42 Firenze"),
    ],
)
def test_cell04_ex05(input):
    file = "./src/cell04/ex05/up_low.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    assert result.stdout == input.swapcase() + "\n"
