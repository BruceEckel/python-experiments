# flatmap.py
from result import Ok, Err
from operations import get_number, double, to_string

if __name__ == "__main__":
    result = (
        Ok("5")  # Try Ok("Bob")
        .and_then(get_number)
        .and_then(double)
        .and_then(to_string)
    )

    match result:
        case Ok(value):
            print(f"Success: {value}")
        case Err(exc):
            print(f"Error: {exc}")
