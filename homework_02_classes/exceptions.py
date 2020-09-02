from loguru import logger


class WeightValueError(ValueError):

    def __init__(self, excess_weight, wheels_qty):
        # excess_weight, wheels_qty = args
        self._excess_weight = excess_weight
        self._wheels_qty = wheels_qty

    def __str__(self):
        res = self._excess_weight
        return logger.error('Очень тяжелый груз, надо убрать {}.', res)


class VolumeValueError(ValueError):

    def __init__(self, volume, max_volume):
        # excess_weight, wheels_qty = args
        self._volume = volume
        self._max_volume = max_volume

    def __str__(self):
        res = self._volume - self._max_volume
        return logger.error('Очень большой объём, надо убрать {} кубометров.', res)

