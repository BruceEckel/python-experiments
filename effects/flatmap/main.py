# main.py
from my_result import Ok, Err
from operations import (
    get_number_from_string,
    double_number,
    convert_to_string,
)

if __name__ == "__main__":
    result = (
        Ok("5")
        .and_then(get_number_from_string)
        .and_then(double_number)
        .and_then(convert_to_string)
    )

    match result:
        case Ok(value=s):
            print(f"Success: {s}")
        case Err(value=exc):
            print(f"Error: {exc}")
