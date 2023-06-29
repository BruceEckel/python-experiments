from pathlib import Path


def display_directory_contents(path):
    path = Path(path)

    for item in path.iterdir():
        if item.is_file():
            print("File:", item.name)
        elif item.is_dir():
            print("Directory:", item.name)
            display_directory_contents(item)


# Call the function with the current directory
current_directory = Path.cwd()
display_directory_contents(current_directory)
