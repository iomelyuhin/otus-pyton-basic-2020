from abc import ABCMeta, abstractmethod


class BaseCar(metaclass=ABCMeta):
    SOUND = 'Бибииип'
    WHEELS = 4

    def honk_the_horn(self):
        return self.SOUND

    @abstractmethod
    def go(self, distance: int) -> int:
        """
        Write to file
        :param distance:
        :return:
        """
        raise NotImplementedError

    def __str__(self):
        return self.honk_the_horn()
