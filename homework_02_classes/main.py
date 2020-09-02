# from BaseCars import BaseCars
from SportCar import SportCar
from TruckCar import TruckCar
# from exceptions import WeightValueError
from loguru import logger
import traceback




# print(SportCar.__name__)
print(SportCar(10).go(50))
print("============================")
print(SportCar(10))
# print(TruckCar().loading(9000, 4))


def loading_truck(weight, volume):
    logger.info("Начинаем загрузку {} тонн, {} кубометров...", weight, volume)
    try:
        truck = TruckCar().loading(weight, volume)
    except ValueError:
        logger.error('Была ошибка - {}', traceback.format_exc())
    else:
        logger.success("Груз отправлен...")
    finally:
        logger.info("До скорой встречи!")


loading_truck(1000, 5)
loading_truck(11000, 5)
loading_truck(10000, 55)


