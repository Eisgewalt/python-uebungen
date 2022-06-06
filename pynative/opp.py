# oop - objekt orientrierte Programmierung

# %% Nr1 - Create a Class with instance attributes
class Vehicle:
    """"New Class"""
    def __init__(self, name, max_speed, mileage) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


car1 = Vehicle("Auto", 200, 1000)
print(car1.max_speed, car1.mileage)


# %% Nr2 - Create a Vehicle class without any variables and methods
class Car:
    """Empty class"""
    pass

# %% Nr3 - Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


Bus1 = Bus("School Volvo", 120, 12)
print(f"Vehicle Name: {Bus1.name} Speed: {Bus1.max_speed} Mileage: {Bus1.mileage}")
print(Bus1.seating_capacity())

# %%
