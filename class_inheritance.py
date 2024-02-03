# -*- confing: utf-8 -*-

class Car:
    price = 1000000

    def horse_powers(self):
        return 140

    def __str__(self):
        return '{} Автомобиль стоит {}, у автомобиля лошадинных сил {}'.format(self.__class__.__name__, self.price,
                                                                               self.horse_powers())


class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return 240


class Kia(Car):
    price = 900000

    def horse_powers(self):
        return 200


car = Car()
print(car)
nissan = Nissan()
print(nissan)
kia = Kia()
print(kia)
