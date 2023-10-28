# python_enum.py
from enum import Enum, auto


class Basic(Enum):
    A = auto()
    B = auto()
    C = auto()

    def show():
        print(list(Basic))


if __name__ == "__main__":
    # Basic.B = 99
    Basic.show()
