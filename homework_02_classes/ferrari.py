from main import BaseCars


class Ferrari(BaseCars):
    MAX_FUEL = 60
    SPEED = 300

    def __init__(self, fuel=30, fuel_consumption=20):
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def go(self, distance):
        fuel_to_spend = distance * self.fuel_consumption
        if fuel_to_spend > self.fuel:
            print(f"Cannot go, not enough fuel {self.fuel}, need {fuel_to_spend}")
            return
        self.fuel -= fuel_to_spend
        print(f"Going {distance}, spent {fuel_to_spend}, left {self.fuel}")
