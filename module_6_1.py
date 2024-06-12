class Car:

    price=1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля не указано"

class Nissan(Car):

    price = 1500000

    def horse_powers(self):
        return 'Количество лошадиных сил Nissan', 180

class Kia(Car):

    price = 700000

    def horse_powers(self):
        return 'Количество лошадиных сил Kia', 125


c = Car()
print('Стоимость автомобиля на старте продаж автомобилей: ', c.price)
print(c.horse_powers())
n = Nissan()
print('Стоимость автомобиля на старте продаж Nissan: ', n.price)
print(n.horse_powers())
k = Kia()
print('Стоимость автомобиля на старте продаж Kia: ', k.price)
print(k.horse_powers())