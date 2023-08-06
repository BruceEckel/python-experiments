import typer
from pathlib import Path


def next_abbrev(script: str):
    for line in script.splitlines():
        for word in line.split():
            yield word[0]
            if word[-1] in ".,?;":
                yield word[-1] + " "
        yield "\n"


def main(script_file_name: str):
    script = Path(script_file_name).read_text()
    print("".join(list(next_abbrev(script))))


if __name__ == "__main__":
    typer.run(main)
