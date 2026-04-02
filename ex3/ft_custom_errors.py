#!usr/bin/env python3

class Plant:
    def __init__(self, name: str, wilting: bool, water: int) -> None:
        self.name = name
        self.wilting = wilting
        self.water = water

    def check_plant_error(self) -> None:
        if self.wilting == True:
            raise PlantError()

class GardenError(Exception):
    def __init__(self, error_message: str = "") -> None:
        super().__init__(error_message)


class PlantError(GardenError):
    def __init__(self, plant: Plant, error_message: str = f"The {plant.name} plant is "):
        super().__init__(error_message)

class WaterError(GardenError):


if __name__ == "__main__":
    print(" === Custon Garden Errors Demo === \n")

