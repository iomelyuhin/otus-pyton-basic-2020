from dataclasses import dataclass
from loguru import logger


@dataclass
class RetroCar:
    fuel: int
    distance: int
    fuel_consumption: int = 20

    def going(self):
        fuel_required = self.distance / self.fuel_consumption
        before_fuel = self.fuel - fuel_required
        if self.fuel > fuel_required:
            return logger.info('Вы проехали {} километров. До заправли осталось {} километров', self.distance,
                               before_fuel)

        return logger.error("Не хватает топлива")
