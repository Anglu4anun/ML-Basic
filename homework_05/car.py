"""
Создайте класс `Car`, наследник `Vehicle`
"""

"""решение"""
from vehicle import Vehicle
from engine import Engine
class Car(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None
    def set_engine(self, engine: Engine):
        self.engine = engine
