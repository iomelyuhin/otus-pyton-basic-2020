# from BaseCars import BaseCars
from SportCar import SportCar
from TruckCar import TruckCar


print(SportCar.__name__)
print(SportCar(10, 50).go())
print("============================")
print(SportCar(10, 50))
print("============================")
print(TruckCar.__name__)
print(TruckCar(20, 4000))
