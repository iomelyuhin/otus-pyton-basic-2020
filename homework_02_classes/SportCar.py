from BaseCars import BaseCars


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

    def __str__(self):
        return f'Было заправлено {self.fuel_add} бензина. Проверка сигнала - {self.honk_the_horn()}'
