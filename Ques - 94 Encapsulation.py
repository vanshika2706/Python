class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model
        self._year = year

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

    def set_year(self, year):
        if year > 1885:  # The first car was invented around 1885
            self._year = year
        else:
            print("Invalid year")


my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")


