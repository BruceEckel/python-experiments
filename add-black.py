from pathlib import Path
import toml


def update_pyproject(file_path: Path):
    try:
        data = toml.load(file_path)

        # Check if [tool.black] exists, if not add it
        if "tool" not in data or "black" not in data["tool"]:
            if "tool" not in data:
                data["tool"] = {}
            data["tool"]["black"] = {"line-length": 47}

            with file_path.open("w") as f:
                toml.dump(data, f)
            print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def main():
    # Start from the current directory
    start_path = Path(".")

    # Use the rglob method to search for pyproject.toml in all subdirectories
    for toml_file in start_path.rglob("pyproject.toml"):
        update_pyproject(toml_file)


if __name__ == "__main__":
    main()
