import subprocess
import pytest


async def test_cell05_ex00():
    file = "./src/cell05/ex00/create_array.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    vars = list(env.keys())
    assert result.stdout == str(env.get(vars[1])) + "\n"


async def test_cell05_ex01():
    file = "./src/cell05/ex01/play_with_arrays.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    var_list = list(env.keys())
    var_list = env.get(var_list[1])
    output = (
        f"Original array: {var_list}\nNew array: {[i + 2 for i in var_list]}\n"
    )
    assert result.stdout == output, var_list


async def test_cell05_ex02():
    file = "./src/cell05/ex02/play_with_arrays.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    var_list = list(env.keys())
    var_list = env.get(var_list[1])
    output = f"{var_list}\n{[i + 2 for i in var_list if i > 5]}\n"
    assert result.stdout == output, var_list


async def test_cell05_ex03():
    file = "./src/cell05/ex03/play_with_arrays.py"
    env = {}
    with open(file) as f:
        exec(f.read(), env)
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    var_list = list(env.keys())
    var_list = env.get(var_list[1])
    var_set = {i + 2 for i in var_list if i > 5}
    output = f"{var_list}\n{var_set}\n"
    assert result.stdout == output


async def test_cell05_ex04():
    file = "./src/cell05/ex04/parameters.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    msg = "Number of parameters: 0.\n"
    assert result.stdout == msg
    result = subprocess.run(
        ["python3", file, "one"], capture_output=True, text=True
    )
    msg = "Number of parameters: 1.\n"
    assert result.stdout == msg
    result = subprocess.run(
        ["python3", file, "one", "two"], capture_output=True, text=True
    )
    msg = "Number of parameters: 2.\n"
    assert result.stdout == msg


async def test_cell05_ex05():
    file = "./src/cell05/ex05/aff_first_param.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "one"], capture_output=True, text=True
    )
    assert result.stdout == "one\n"
    result = subprocess.run(
        ["python3", file, "one", "two"], capture_output=True, text=True
    )
    assert result.stdout == "one\n"


async def test_cell05_ex06():
    file = "./src/cell05/ex06/upcase_it.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "one"], capture_output=True, text=True
    )
    assert result.stdout == "ONE\n"
    result = subprocess.run(
        ["python3", file, "one", "two"], capture_output=True, text=True
    )
    assert result.stdout == "none\n"


async def test_cell05_ex07():
    file = "./src/cell05/ex07/downcase_it.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "oNe"], capture_output=True, text=True
    )
    assert result.stdout == "one\n"
    result = subprocess.run(
        ["python3", file, "onE", "two"], capture_output=True, text=True
    )
    assert result.stdout == "none\n"


async def test_cell05_ex08():
    file = "./src/cell05/ex08/aff_rev_params.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "oNe"], capture_output=True, text=True
    )
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "onE", "two"], capture_output=True, text=True
    )
    assert result.stdout == "two\nonE\n"


async def test_cell05_ex09():
    file = "./src/cell05/ex09/scan_it.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stdout == "none\n"
    result = subprocess.run(
        ["python3", file, "oNe"], capture_output=True, text=True
    )
    assert result.stdout == "none\n"
    result = subprocess.run(
        [
            "python3",
            file,
            "the",
            "the quick brown fox jumps over the lazy dog",
        ],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "2\n"
    result = subprocess.run(
        ["python3", file, "onE", "two", "three"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "none\n"


@pytest.mark.parametrize("input", ["oNe", "one"])
async def test_cell05_ex10(input):
    file = "./src/cell05/ex10/parameter_matching.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "one", "two"], capture_output=True, text=True
    )
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "one"],
        input=f"{input}\n",
        capture_output=True,
        text=True,
    )
    prompt = "What was the parameter? "
    expected = "Good job!\n" if input == "one" else "Nope, sorry...\n"
    assert result.stdout == prompt + expected


async def test_cell05_ex11():
    file = "./src/cell05/ex11/count_it.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "Game", "of", "Thrones"],
        capture_output=True,
        text=True,
    )
    expected = "parameters: 3\nGame: 4\nof: 2\nThrones: 7\n"
    assert result.stdout == expected
    result = subprocess.run(
        ["python3", file, "one", "two"], capture_output=True, text=True
    )
    expected = "parameters: 2\none: 3\ntwo: 3\n"
    assert result.stdout == expected
    result = subprocess.run(
        ["python3", file, "one"], capture_output=True, text=True
    )
    expected = "parameters: 1\none: 3\n"
    assert result.stdout == expected


async def test_cell05_ex12():
    file = "./src/cell05/ex12/string_are_arrays.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "Game", "of", "Thrones"],
        capture_output=True,
        text=True,
    )
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "Zaz visits the zoo with Zazie"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "zzz\n"
    result = subprocess.run(
        ["python3", file, "z"], capture_output=True, text=True
    )
    assert result.stdout == "z\n"


async def test_cell05_ex13():
    file = "./src/cell05/ex13/append_it.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "parallel", "egoism", "human"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "parallelism\nhumanism\n"
    result = subprocess.run(
        ["python3", file, "parallelism", "egoism", "human"],
        capture_output=True,
        text=True,
    )
    assert result.stdout == "humanism\n"


async def test_cell05_ex14():
    file = "./src/cell05/ex14/free_range.py"
    result = subprocess.run(["python3", file], capture_output=True, text=True)
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "1"], capture_output=True, text=True
    )
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "a", "2"], capture_output=True, text=True
    )
    assert result.stderr == "Invalid numbers.\n"
    result = subprocess.run(
        ["python3", file, "1", "2", "3"], capture_output=True, text=True
    )
    assert result.stderr == "none\n"
    result = subprocess.run(
        ["python3", file, "1", "2"], capture_output=True, text=True
    )
    assert result.stdout == "[1, 2]\n"
    result = subprocess.run(
        ["python3", file, "10", "14"], capture_output=True, text=True
    )
    assert result.stdout == "[10, 11, 12, 13, 14]\n"
