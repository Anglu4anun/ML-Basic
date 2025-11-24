"""
Создайте класс `Plane`, наследник `Vehicle`
"""

"""решение"""
from vehicle import Vehicle
from exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        """
        Инициализирует самолёт заданными параметрами.
        
        :param weight: Вес самолёта.
        :param fuel: Количество топлива.
        :param fuel_consumption: Расход топлива на единицу расстояния.
        :param max_cargo: Максимально допустимый вес перевозимого груза.
        """
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0              # Начальное значение груза равно нулю
        self.max_cargo = max_cargo  # Максимальная грузоподъёмность самолета

    def load_cargo(self, added_weight: float):
        """
        Загружает указанный вес груза на самолет, предварительно проверяя отсутствие перегрузки.
        
        :param added_weight: Дополнительный вес груза.
        :raises CargoOverload: Если суммарный вес превышает максимальную грузоподъемность.
        """
        new_total = self.cargo + added_weight
        if new_total <= self.max_cargo:
            self.cargo = new_total
        else:
            raise CargoOverload(f'Перегрузка груза: максимальная вместимость {self.max_cargo}, '
                                f'предложено загрузить {new_total}')

    def remove_all_cargo(self):
        """
        Полностью разгружает груз и возвращает массу выгруженного груза.
        
        :return: Масса выгруженного груза.
        """
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
