class Car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")
    @classmethod
    def is_motor_vehicle(cls):
        return True
    @staticmethod
    def honk():
        print("HONK!")

my_car = Car("Toyota", "Corolla", 2020)

my_car.display_info()
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
