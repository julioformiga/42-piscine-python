import subprocess
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("42", "This number is different from zero.\n"),
        ("0", "This number is equal to zero.\n"),
        ("Wil", "This input is not a number.\n"),
    ],
)
def test_cell02_ex00(input, expected):
    file = "./src/cell02/ex00/iszero.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        assert result.stdout == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("-42", "This number is negative.\n"),
        ("0", "This number is both positive and negative.\n"),
        ("42", "This number is positive.\n"),
        ("Wil", "This input is not a number.\n"),
    ],
)
def test_cell02_ex01(input, expected):
    file = "./src/cell02/ex01/isneg.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        assert result.stdout == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Python is awesome", "ACCESS GRANTED\n"),
        ("C", "ACCESS DENIED\n"),
    ],
)
def test_cell02_ex02(input, expected):
    file = "./src/cell02/ex02/password.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    assert result.stdout == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    [
        ("2", "3", "The result is positive.\n"),
        ("2", "-3", "The result is negative.\n"),
        ("2", "0", "The result is positive and negative.\n"),
        ("2", "a", "This input is not a number.\n"),
    ],
)
def test_cell02_ex03(input1, input2, expected):
    file = "./src/cell02/ex03/mult.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input1}\n{input2}\n",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        prompt = "Enter the first number:\nEnter the second number:\n"
        prompt += f"{input1} x {input2} = {int(input1) * int(input2)}\n"
        assert result.stdout == prompt + expected
