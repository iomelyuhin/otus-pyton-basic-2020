# from BaseCars import BaseCars
from sport_car import SportCar
from truck_car import TruckCar
from retro_car import RetroCar
from loguru import logger
import traceback


def loading_truck(weight, volume):
    logger.info("Начинаем загрузку {} тонн, {} кубометров...", weight, volume)
    try:
        TruckCar().loading(weight, volume)
    except ValueError:
        logger.exception('Была ошибка:')
    else:
        logger.success("Груз отправлен...")
    finally:
        logger.info("До скорой встречи!")


SportCar(20).go(400)
SportCar(10).go(600)
SportCar(10).beep()

RetroCar(40, 100, 20).going()
TruckCar().go(distance=100)

loading_truck(1000, 5)
loading_truck(11000, 5)
loading_truck(10000, 55)



