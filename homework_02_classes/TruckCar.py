from BaseCars import BaseCars


class TruckCar(BaseCars):
    MAX_WEIGHT = 10000
    MAX_VOLUME = 20
    WHEELS = 8

    def __init__(self, volume, weight):
        self.volume = volume
        self.weight = weight

    def loading(self):
        if self.weight > self.MAX_WEIGHT:
            print('Очень тяжелый груз, надо убрать {self.weight - self.MAX_WEIGHT}. Даже {self.WHEELS} колёс его не '
                  'выдержат. ')
        elif self.volume > self.MAX_VOLUME:
            print(f'Кузов не резиновый! Надо убрать {self.volume - self.MAX_VOLUME}. ')

    def __str__(self):
        self.loading()
        return f'Завершена погрузка. Загружено {self.weight} килограмм, объемом {self.volume} м3'
