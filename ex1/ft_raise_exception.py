#!usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")

    temp_int: int = int(temp_str)

    if temp_int >= 0 and temp_int <= 40:
        return temp_int
    elif temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants ! (min 0°C)")
    else:
        raise ValueError(f"{temp_int}°C is too hot for plants ! (max 40°C)")


def test_temperature() -> None:
    temp_list: list[str] = ["25", "abc", "100", "-50"]

    for temp_str in temp_list:

        try:
            temp_int: int = input_temperature(temp_str)
            print(f"Temperature is now {temp_int}°C")
        except ValueError as e:
            print(f"Caught input_temperature error : {e}")

    print("\nAll tests completed - program didn't crash !")


if __name__ == "__main__":
    print(" === Garden temperature checker === ")
    test_temperature()
