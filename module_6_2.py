class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля не указано"


class Nissan(Vehicle, Car):
    price = 1500000
    vehicle_type = 'Седан'

    def __init__(self, age):
        self.age = age

    def horse_powers(self):
        return 'Количество лошадиных сил', 120


n = Nissan(5)
print(n.vehicle_type, n.price)
