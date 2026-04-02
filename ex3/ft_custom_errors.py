#!usr/bin/env python3

class Plant:
    def __init__(self, name: str, wilting: bool, water: int) -> None:
        self.name = name
        self.wilting = wilting
        self.water = water

    def check_plant_error(self) -> None:
        if self.wilting is True:
            raise PlantError(f"The {self.name} plant is wilting !")

    def check_water_error(self) -> None:
        if self.water < 5:
            raise WaterError(f"Not enough water in the \
tank ! (for {self.name})")

    def check_garden_error(self) -> None:
        try:
            self.check_plant_error()
        except PlantError as e:
            print(f"Caught GardenError : {e}")
        try:
            self.check_water_error()
        except WaterError as e:
            print(f"Caught GardenError : {e}")


class GardenError(Exception):
    def __init__(self, error_message: str = "Unknown Garden error") -> None:
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, error_message: str = "Unknown Plant error"):
        super().__init__(error_message)


class WaterError(GardenError):
    def __init__(self, error_message: str = "Unknown Water error"):
        super().__init__(error_message)


if __name__ == "__main__":
    print(" === Custon Garden Errors Demo === \n")
    Rose = Plant("Rose", True, 3)

    print("Testing PlantError ...")
    try:
        Rose.check_plant_error()
    except PlantError as e:
        print(f"Caught PlantError : {e}")

    print("Testing WaterError ...")
    try:
        Rose.check_water_error()
    except WaterError as e:
        print(f"Caught WaterError : {e}")

    print("Testing catching all garden errors ...")
    Rose.check_garden_error()

    print("\nAll custom error types work correctly !")
