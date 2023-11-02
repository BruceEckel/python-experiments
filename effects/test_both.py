# test_both.py
from pathlib import Path

if __name__ == "__main__":
    code = Path("return_result.py").read_text()
    print(" 'my_result' ".center(40, "="))
    exec(code)
    modified = code.replace("my_result", "result")
    print(" 'result' ".center(40, "="))
    exec(modified)
