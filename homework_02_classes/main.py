from ferrari import Ferrari


class BaseCars:
    SOUND = 'beep'
    WHEELS = 4

    def honk_the_horn(self):
        return self.SOUND


class SportCar(BaseCars):
    FUEL = 40
    CONSUMPTION = 10
    SPEED = 200

    def __init__(self, fuel_add, length):
        self.fuel_add = fuel_add
        self.length = length

    def go(self):
        power_reserve = ((self.FUEL + self.fuel_add) / self.CONSUMPTION) * 100
        if self.length > power_reserve:
            print("Не хватает топлива")
        return print(f'Вы проехали {self.length} километров. До заправли осталось {power_reserve - self.length}')

    # def honk_the_horn(self):
    #     return self.SOUND + "BEEP"

    def __str__(self):
        self.go()
        return f'Было заправлено {self.fuel_add} бензина. Проверка сигнала - {self.honk_the_horn()}'


class TruckCar(BaseCars):
    MAX_WEIGHT = 10000
    MAX_VOLUME = 20
    WHEELS = 8

    def __init__(self, volume, weight):
        self.volume = volume
        self.weight = weight

    def loading(self):
        if self.weight > self.MAX_WEIGHT:
            print('Очень тяжелый груз, надо убрать {self.weight - self.MAX_WEIGHT}. Даже {self.WHEELS} колёс его не '
                  'выдержат. ')
        elif self.volume > self.MAX_VOLUME:
            print(f'Кузов не резиновый! Надо убрать {self.volume - self.MAX_VOLUME}. ')

    def __str__(self):
        self.loading()
        return f'Завершена погрузка. Загружено {self.weight} килограмм, объемом {self.volume} м3'


print(SportCar.__name__)
print(SportCar(10, 50))
print(TruckCar.__name__)
print(TruckCar(20, 4000))
