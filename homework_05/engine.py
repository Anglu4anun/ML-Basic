"""
Создайте dataclass `Engine`
"""

"""решение"""
from dataclasses import dataclass
@dataclass
class Engine:
    volume: float           # Объем двигателя
    pistons: int            # Количество цилиндров
