from base_car import BaseCar
from loguru import logger


class SportCar(BaseCar):
    FUEL = 40
    CONSUMPTION = 10
    SPEED = 200

    def __init__(self, additional_fuel=30):
        self._additional_fuel = additional_fuel

    def fuel_add(self):
        total_fuel = self._additional_fuel + self.FUEL
        return total_fuel

    def go(self, distance: int) -> None:
        power_reserve = (self.fuel_add() / self.CONSUMPTION) * 100
        if distance > power_reserve:
            excess_fuel = (distance - power_reserve) / self.CONSUMPTION
            logger.error("Не хватает топлива, заправьте {} литров", excess_fuel)
            return
        logger.info('Вы проехали {} километров. До заправли осталось {} километров', distance, power_reserve - distance)

    def beep(self):
        hong = super().honk_the_horn()
        sport_hong = "Бааааааап"
        res = hong + sport_hong
        return logger.success('Было заправлено {} бензина. Проверка сигнала - {}', self.fuel_add, res)

    def __str__(self):
        res = super().honk_the_horn()
        return logger.info('Было заправлено {} бензина. Проверка сигнала - {}', self.fuel_add, res)
