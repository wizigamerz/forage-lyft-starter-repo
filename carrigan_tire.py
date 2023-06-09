from abc import ABC

from car import Car


class CarriganTire(Car, ABC):
    def __init__(self, tire):
        self.tire = tire

    def needs_tire_service(self):
        service = False
        for i in range(4):
            if self.tire[i] >= 0.9:
                service = True
        return service