import sys
from pathlib import Path


def display_directory_contents(path: Path) -> None:
    for item in path.iterdir():
        if item.is_file():
            print("File:", item.name)
        elif item.is_dir():
            print("Directory:", item.name)
            display_directory_contents(item)


if __name__ == "__main__":
    # Select the starting directory from the command line
    # or use the current directory
    if len(sys.argv) > 1:
        starting_directory = Path(sys.argv[1])
    else:
        starting_directory = Path.cwd()

    display_directory_contents(starting_directory)
