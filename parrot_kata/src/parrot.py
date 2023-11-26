from enum import Enum  # Enum is introduced in Python 3.4.
from abc import ABC, abstractmethod


class ParrotType(Enum):  # If it is not available, just remove it.
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot(ABC):
    @abstractmethod
    def speed(self):
        raise NotImplementedError()

    @abstractmethod
    def cry(self):
        raise NotImplementedError()

    def _load_factor(self):
        return 9.0

    def _base_speed(self):
        return 12.0


class EuropeanParrot(Parrot):
    def speed(self):
        return self._base_speed()

    def cry(self):
        return "Sqoork!"


class AfricanParrot(Parrot):
    def __init__(self, number_of_coconuts):
        self._number_of_coconuts = number_of_coconuts

    def speed(self):
        return max(
            0, self._base_speed() - self._load_factor() * self._number_of_coconuts
        )

    def cry(self):
        return "Sqaark!"


class NorwegianBlueParrot(Parrot):
    def __init__(self, voltage, nailed):
        self._voltage = voltage
        self._nailed = nailed

    def speed(self):
        return (
            0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)
        )

    def cry(self):
        return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])


class ParrotFactory:
    @staticmethod
    def create(type_of_parrot, number_of_coconuts, voltage, nailed):
        if type_of_parrot == ParrotType.EUROPEAN:
            return EuropeanParrot()
        elif type_of_parrot == ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts)
        elif type_of_parrot == ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(voltage, nailed)
        else:
            raise KeyError(f"Invalid parrot type: {type_of_parrot}")
