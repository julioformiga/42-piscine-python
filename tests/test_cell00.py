from os import path
import subprocess


async def test_cell00_ex00():
    assert path.exists("./src/cell00/ex00")


async def test_cell00_ex01():
    result = subprocess.run(
        ["python3", "./src/cell00/ex01/42.py"], capture_output=True, text=True
    )
    assert result.stdout == "42\n"


async def test_cell00_ex02():
    result = subprocess.run(
        ["python3", "./src/cell00/ex02/hello_world.py"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "Hello World\n"
