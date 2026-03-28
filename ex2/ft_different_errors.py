#!usr/bin/env python3

def garden_operations(operation_number) -> None:
    if operation_number == 0:
        print("Caught ValueError : ", end="")
        raise ValueError
    # if operation_number == 1:


def test_error_type() -> None:
    for i in range(4):
        print(f"Testing operation {i} ...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"{e}")
        except ZeroDivisionError as e:

if __name__ == "__main__":
    print(" === Garden error types demo === ")
    test_error_type()
