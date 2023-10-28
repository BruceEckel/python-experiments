# my_error.py


class MyError(Exception):
    pass


# Display helper:
def err(type: str, msg: str):
    print(f"{type} Error -> {msg}")
