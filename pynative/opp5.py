# %% Nr5
class Vehicle:
    """Nothing"""
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    """Nothing"""
    pass


class Car(Vehicle):
    """Nothing"""
    pass


if __name__ == "__main__":
    bus = Bus("School Volvo", 180, 12)
    car = Car("Audi Q5", 240, 18)

    print(f"Color {bus.color}, Vehicle Name: {bus.name} Speed: {bus.max_speed} Mileage: {bus.mileage}")