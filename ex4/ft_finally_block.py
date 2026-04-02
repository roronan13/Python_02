#!usr/bin/env python3

class Plant:
    all_plants = []

    def __init__(self, plant_name: str):
        self.plant_name = plant_name
        Plant.all_plants.append(self)

    def water_plant(self, plant_name: str) -> None:
        if str.capitalize(plant_name):
            print(f"Watering {self.plant_name} : [OK]")
        else:
            raise PlantError(f"Caught PlantError : Invalid plant name to \
water : '{self.plant_name}'")

    def test_watering_system() -> None:
        print("Opening water system")
        for plant in Plant.all_plants:
            try:
                Plant.water_plant(plant.plant_name)
            except PlantError as e:
                print(f"{e}")
                print("... ending tests and returning to main")
            finally:
                print("Closing watering system")


class PlantError(Exception):
    def __init__(self, error_message: str = "Unknown Plant error"):
        super().__init__(error_message)


if __name__ == "__main__":
    print(" === Garden Watering System === \n")

    print("Testing valid plants ...")
    rose = Plant("Rose")
    lila = Plant("Lila")
    tomato = Plant("Tomato")
    Plant.test_watering_system()

    print("Testing invalid plants ...")
    lettuce = Plant("lettuce")
    carrots = Plant("Carrots")
    Plant.test_watering_system()

    print("Cleanup always happen, even with errors !")
