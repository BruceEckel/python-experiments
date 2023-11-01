# test_both.py
from pathlib import Path
import os


if __name__ == "__main__":
    print("========== 'my_result' library ==========")
    os.system("python return_result.py")
    print("========== 'result' library ==========")
    Path("return_result_2.py").write_text(
        Path("return_result.py")
        .read_text()
        .replace(
            "my_result",
            "result",
        )
    )
    os.system("python return_result_2.py")
