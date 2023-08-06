import typer
from pathlib import Path


def next_abbrev(script: str):
    for line in script.splitlines():
        for word in line.split():
            yield word[0]
            if word[-1] in ".,?;":
                yield word[-1] + " "
        yield "\n"


def main(fname: str):
    script = Path(fname).read_text()
    print("".join(list(next_abbrev(script))))


if __name__ == "__main__":
    typer.run(main)
