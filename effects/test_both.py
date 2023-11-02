# test_both.py
import io
import sys
from pathlib import Path


# Returns the output from exec(code)
def exec_o(code: str) -> str:
    buffer = io.StringIO()
    sys.stdout = buffer
    try:
        exec(code, globals())
    finally:
        # Reset stdout
        sys.stdout = sys.__stdout__
    return buffer.getvalue()


if __name__ == "__main__":
    code = Path("return_result.py").read_text()
    output1 = exec_o(code)
    print(output1)

    modified = code.replace("my_result", "result")
    output2 = exec_o(modified)

    assert output1 == output2
