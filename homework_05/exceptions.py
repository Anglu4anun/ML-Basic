"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    pass
class NotEnoughFuel(LowFuelError):
    pass
class CargoOverload(Exception):
    pass
