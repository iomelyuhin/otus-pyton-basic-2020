from BaseCars import BaseCars


class SportCar(BaseCars):
    FUEL = 40
    CONSUMPTION = 10
    SPEED = 200

    def __init__(self, fuel_add=30):
        self._fuel_add = fuel_add

    @property
    def fuel_add(self):
        return self._fuel_add

    def go(self, length):
        power_reserve = ((self.FUEL + self.fuel_add) / self.CONSUMPTION) * 100
        if length > power_reserve:
            print("Не хватает топлива")
            return
        print(f'Вы проехали {length} километров. До заправли осталось {power_reserve - length}')

    def __str__(self):
        res = super().honk_the_horn()
        return f'Было заправлено {self.fuel_add} бензина. Проверка сигнала - {res}'
