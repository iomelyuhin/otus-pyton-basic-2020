class Ferrari:
    MAX_FUEL = 60

    def __init__(self, fuel=30, fuel_consumption=20):
        self.__fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def fuel(self):
        return self.__fuel

    def go(self, distance):
        fuel_to_spend = distance * self.fuel_consumption
        if fuel_to_spend > self.__fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spend}")
            return
        self.__fuel -= fuel_to_spend
        print(f"Going {distance}, spent {fuel_to_spend}, left {self.__fuel}")

    def add_fuel(self, value):
        print("Adding", value, "of fuel")
        self.__fuel += value
        if self.__fuel > self.MAX_FUEL:
            print("lost", self.__fuel - self.MAX_FUEL, "of fuel")
            self.__fuel = self.MAX_FUEL
        return self.__fuel
