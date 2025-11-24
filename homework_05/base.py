"""
Доработайте класс `Vehicle`
"""

from abc import ABC


class Vehicle(ABC):
    pass

from typing import Optional

"""решение"""
class Vehicle:
    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        self.weight = weight       # вес автомобиля
        self.started = False      # состояние двигателя 
        self.fuel = fuel          # текущее количество топлива
        self.fuel_consumption = fuel_consumption   # потребляемое топливо
    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError('нет топлива для запуска')
            self.started = True
    def stop(self):
        self.started = False
    def move(self, distance: float):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel('недостаточно топлива для перемещения')
class LowFuelError(Exception):
    """низкий уровень топлива"""
    pass
class NotEnoughFuel(Exception):
    """недостаточно топлива для движения"""
    pass
