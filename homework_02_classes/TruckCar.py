from BaseCars import BaseCars
from loguru import logger
from exceptions import WeightValueError
from exceptions import VolumeValueError


class TruckCar(BaseCars):
    MAX_WEIGHT = 10000
    MAX_VOLUME = 20
    WHEELS = 8

    def __init__(self, fuel_add=30):
        self._fuel_add = fuel_add

    # @property
    def fuel_add(self):
        return self._fuel_add

    def loading(self, weight=11000, volume=5):
        excess_weight = weight - self.MAX_WEIGHT
        wheels_qty = self.WHEELS
        if weight > self.MAX_WEIGHT:
            raise WeightValueError(excess_weight, wheels_qty)
        elif volume > self.MAX_VOLUME:
            raise VolumeValueError(volume, self.MAX_VOLUME)
            # logger.info('Кузов не резиновый! Надо убрать {}.', volume - self.MAX_VOLUME)

        return logger.success("Всё влезло! Я поехал!")

    def __str__(self):
        res = super().honk_the_horn()
        return logger.info('Завершена погрузка. {}', res)
