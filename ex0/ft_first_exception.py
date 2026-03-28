#!usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_temperature() -> None:
    temp_str: str = "25"
    try:
        temp_int: int = input_temperature(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except ValueError:
        print(f"Caught input_temperature error : invalid literal for int() \
with base 10: '{temp_str}'")

    temp_str: str = "abc"
    try:
        temp_int: int = input_temperature(temp_str)
        print(f"Temperature is now {temp_int}°C")
    except ValueError:
        print(f"Caught input_temperature error : invalid literal for int() \
with base 10: '{temp_str}'")

    print("\nAll tests completed - program didn't crash !")


if __name__ == "__main__":
    print(" === Garden temperature === \n")
    test_temperature()
