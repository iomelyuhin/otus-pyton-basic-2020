from base_car import BaseCar
from loguru import logger
from exceptions import WeightValueError
from exceptions import VolumeValueError


class TruckCar(BaseCar):
    MAX_WEIGHT = 10000
    MAX_VOLUME = 20
    WHEELS = 8
    FUEL = 50
    CONSUMPTION = 30

    def __init__(self, additional_fuel=30):
        self._additional_fuel = additional_fuel

    def fuel_add(self):
        total_fuel = self._additional_fuel + self.FUEL
        return total_fuel

    def loading(self, weight=11000, volume=5):
        excess_weight = weight - self.MAX_WEIGHT
        wheels_qty = self.WHEELS
        if weight > self.MAX_WEIGHT:
            raise WeightValueError(excess_weight, wheels_qty)
        elif volume > self.MAX_VOLUME:
            raise VolumeValueError(volume, self.MAX_VOLUME)
        return logger.success("Всё влезло! Я поехал!")

    def go(self, distance: int) -> None:
        power_reserve = (self.fuel_add() / self.CONSUMPTION) * 100
        if distance > power_reserve:
            excess_fuel = (distance - power_reserve) / self.CONSUMPTION
            logger.error("Не хватает топлива, заправьте {} литров", excess_fuel)
            return
        logger.info('Вы проехали {} километров. До заправли осталось {} километров', distance, power_reserve - distance)

    def __str__(self):
        res = super().honk_the_horn()
        return logger.info('Завершена погрузка. {}', res)
