#!usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int: int = int(temp_str)
        print(f"Temperature is now {temp_int}°C")
        if temp_int >= 0 and temp_int <= 40:
            return temp_int
        elif temp_int < 0:
            raise ValueError(f"Caught input_temperature error : {temp_int}°C is too cold for plants ! (min 0°C)")
        else:
            raise ValueError(f"Caught input_temperature error : {temp_int}°C is too hot for plants ! (max 40°C)")

    except ValueError:
        print(f"Caught input_temperature error : invalid literal for int() \
with base 10: '{temp_str}'")


def test_temperature() -> None:
    temp_list: list[str] = ["25", "abc", "100", "-50"]

    for temp_str in temp_list:
        input_temperature(temp_str)

#         try:
#             temp_int: int = input_temperature(temp_str)
#             print(f"Temperature is now {temp_int}°C")
#         except ValueError:
#             print(f"Caught input_temperature error : invalid literal for int() \
# with base 10: '{temp_str}'")

    print("\nAll tests completed - program didn't crash !")


if __name__ == "__main__":
    print(" === Garden temperature checker === \n")
    test_temperature()
