from BaseCars import BaseCars
from loguru import logger


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
            excess_fuel = (length - power_reserve) / self.CONSUMPTION
            logger.error("Не хватает топлива, заправьте {} литров", excess_fuel)
            return
        logger.info('Вы проехали {} километров. До заправли осталось {} километров', length, power_reserve - length)

    def beep(self):
        hong = super().honk_the_horn()
        sport_hong = "Бааааааап"
        res = hong + sport_hong
        return logger.success('Было заправлено {} бензина. Проверка сигнала - {}', self._fuel_add, res)

    def __str__(self):
        res = super().honk_the_horn()
        return logger.info('Было заправлено {} бензина. Проверка сигнала - {}', self.fuel_add, res)
