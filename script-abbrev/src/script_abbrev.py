import typer
from pathlib import Path


def next_abbrev(script: str, num_of_letters: int = 1):
    assert num_of_letters >= 1
    for line in script.splitlines():
        for word in line.split():
            punctuation = word[-1] if word[-1] in ".,?;" else ""
            yield word[:num_of_letters] + punctuation
        yield "\n"


def main(script_file_name: str, num_of_letters: int):
    assert num_of_letters >= 1
    spaces = "" if num_of_letters == 1 else " "
    script = Path(script_file_name).read_text()
    print(spaces.join(list(next_abbrev(script, num_of_letters))))


if __name__ == "__main__":
    typer.run(main)
