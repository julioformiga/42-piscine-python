import subprocess
import pytest


@pytest.mark.parametrize(
    "input, expected",
    [
        ("-42", "Inside the loop, my variable is"),
        ("20", "Inside the loop, my variable is"),
        ("30", "Error\n"),
        ("Wil", "This input is not a number.\n"),
    ],
)
def test_cell03_ex00(input, expected):
    file = "./src/cell03/ex00/to25.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        prompt = "Enter a number less than 25\n"
        i = int(input)
        while i <= 25:
            prompt += f"{expected} {i}\n"
            i += 1
        assert result.stdout == prompt


@pytest.mark.parametrize(
    "input, expected",
    [
        ("-42", ""),
        ("20", ""),
        ("Wil", "This input is not a number.\n"),
    ],
)
def test_cell03_ex01(input, expected):
    file = "./src/cell03/ex01/multiplication_table.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input}",
        capture_output=True,
        text=True,
    )
    if result.stderr:
        assert result.stderr == expected
    else:
        prompt = "Enter a number\n"
        for i in range(0, 10):
            prompt += f"{i} x {int(input)} = {i * int(input)}\n"
        assert result.stdout == prompt


@pytest.mark.parametrize(
    "input1, input2, input3",
    [
        ("Wil", "42", "STOP"),
        ("Wil", "STOP", "STOP"),
    ],
)
def test_cell03_ex02(input1, input2, input3):
    file = "./src/cell03/ex02/i_got_that.py"
    result = subprocess.run(
        ["python3", file],
        input=f"{input1}\n{input2}\n{input3}\n",
        capture_output=True,
        text=True,
    )
    prompt = "What you gotta say? : "
    list = [input1, input2, input3]
    while list.pop(0) != "STOP":
        prompt += "I got that! Anything else? : "
    assert result.stdout == prompt


@pytest.mark.parametrize(
    "arg, expected",
    [
        ("yolo", "none\n"),
        (None, ""),
    ],
)
def test_cell03_ex03(arg, expected):
    file = "./src/cell03/ex03/advanced_mult.py"
    if arg:
        result = subprocess.run(
            ["python3", file, arg],
            capture_output=True,
            text=True,
        )
        assert result.stderr == expected
    else:
        result = subprocess.run(
            ["python3", file],
            capture_output=True,
            text=True,
        )
        prompt = ""
        i = 0
        while i < 11:
            prompt += f"Table de {i}:"
            j = 0
            while j < 11:
                prompt += f" {i * j}"
                j += 1
            prompt += "\n"
            i += 1
        assert result.stdout == prompt
