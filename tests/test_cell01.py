import subprocess
import pytest


def test_cell01_ex00():
    file = "./src/cell01/ex00/name.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    assert "first_name" in env, "first_name is not defined"
    assert "last_name" in env, "last_name is not defined"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    expected = f"{env['first_name']} {env['last_name']}\n"
    assert result.stdout == expected


def test_cell01_ex01():
    file = "./src/cell01/ex01/name.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    assert "first_name" in env, "first_name is not defined"
    assert "last_name" in env, "last_name is not defined"
    assert "whole_name" in env, "whole_name is not defined"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    expected = f"{env['first_name']} {env['last_name']}\n"
    assert result.stdout == expected


def test_cell01_ex02():
    file = "./src/cell01/ex02/age.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    assert "my_age" in env, "my_age is not defined"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    expected = f"{env['my_age']}\n"
    assert result.stdout == expected


@pytest.mark.parametrize(
    "input1, input2", [("Wil", "42"), ("Julio", "Formiga")]
)
def test_cell01_ex03(input1, input2):
    file = "./src/cell01/ex03/whatsyourname.py"

    result = subprocess.run(
        ["python3", file],
        input=f"{input1}\n{input2}\n",
        capture_output=True,
        text=True,
    )
    expected = f"Hey, what's your first name? : And your last name? : \
Well, pleased to meet you, {input1} {input2}.\n"
    assert result.stdout == expected
