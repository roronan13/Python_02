#!usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("allo")
    elif operation_number == 1:
        13 / 0
    elif operation_number == 2:
        open("NoFile")
    elif operation_number == 3:
        13 + "allo"
    else:
        return


def test_error_type() -> None:
    for i in range(5):
        print(f"Testing operation {i} ...")
        try:
            garden_operations(i)
            print("Operation completed successfully !")
        except ValueError as e:
            print(f"Caught ValueError : {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError : {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNorFoundError : {e}")
        except TypeError as e:
            print(f"Caught TypeError : {e}")

    print("\nAll error types were tested successfully !")


if __name__ == "__main__":
    print(" === Garden error types demo === \n")
    test_error_type()
