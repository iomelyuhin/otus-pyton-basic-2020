# from BaseCars import BaseCars
from SportCar import SportCar
from TruckCar import TruckCar
from loguru import logger
import traceback


def loading_truck(weight, volume):
    logger.info("Начинаем загрузку {} тонн, {} кубометров...", weight, volume)
    try:
        TruckCar().loading(weight, volume)
    except ValueError:
        logger.error('Была ошибка - {}', traceback.format_exc())
    else:
        logger.success("Груз отправлен...")
    finally:
        logger.info("До скорой встречи!")


SportCar(10).go(400)
SportCar(10).go(600)
SportCar(10).beep()

loading_truck(1000, 5)
loading_truck(11000, 5)
loading_truck(10000, 55)


