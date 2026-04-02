#!usr/bin/env python3

class Plant:
    all_plants = []

    def __init__(self, plant_name: str):
        self.plant_name = plant_name
        Plant.all_plants.append(self)

    def water_plant(plant_name: str) -> None:
        if plant_name == plant_name.capitalize():
            print(f"Watering {plant_name} : [OK]")
        else:
            raise PlantError(f"Caught PlantError : Invalid plant name to \
water : '{plant_name}'")

    @staticmethod
    def test_watering_system() -> None:
        print("Opening watering system")
        try:
            for plant in Plant.all_plants:
                Plant.water_plant(plant.plant_name)
        except PlantError as e:
            print(f"{e}")
            print("... ending tests and returning to main")
            return
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

    print("\nTesting invalid plants ...")
    lettuce = Plant("lettuce")
    carrots = Plant("Carrots")
    Plant.test_watering_system()

    print("\nCleanup always happen, even with errors !")
