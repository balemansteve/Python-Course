class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    return print(f"{self.brand} {self.model} {self.year}")

my_car = Car("Toyota", "Corolla", 2020)

my_car.display_info()