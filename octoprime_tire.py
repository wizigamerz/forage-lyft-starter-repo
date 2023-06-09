from abc import ABC

from car import Car


class OctoprimeTire(Car, ABC):
    def __init__(self, tire):
        self.tire = tire

    def needs_tire_service(self):
        return sum(self.tire) >= 3