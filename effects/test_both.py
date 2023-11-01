from pathlib import Path
import subprocess

if __name__ == "__main__":
    file_path = Path("return_result.py")

    print("Running tests with 'result' library")
    subprocess.run(["python", "return_result.py"])

    print("Running tests with 'my_result' library")
    content = file_path.read_text()
    modified_content = content.replace(
        "from result import Result, Ok, Err",
        "from my_result import Result, Ok, Err",
    )
    file_path.write_text(modified_content)

    subprocess.run(["python", "return_result.py"])
