class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"Автомобіль марка: {self.brand}, рік випуску: {self.year}"

my_car = Car("Honda", 2007)

print(my_car)