#!usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input date is {temp_str}")
    return int(temp_str)

def test_temperature(temperature: str) -> None:
    try:
        temp_int = input_temperature(temperature)
        print(f"Temperature is now {temp_int}°C")
    except ValueError:
        print("NO")


if __name__ == "__main__":
    print(" === Garden temperature === \n")
    test_temperature("25")
    test_temperature("abc")
