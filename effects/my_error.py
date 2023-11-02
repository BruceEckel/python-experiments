# my_error.py


class MyError(Exception):
    pass


# Display helper:
def err(type: str, e: Exception) -> None:
    print(f"{type} Error -> {e}")
