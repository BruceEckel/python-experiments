# obj.py


class Obj:
    def __init__(self, id: str) -> None:
        self.id = id
        print(f"{self}")

    def __repr__(self):
        return f"[{self.id}]"

    def __del__(self):
        print(f"~{self}")
