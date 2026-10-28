from abc import ABC, abstractmethod
from asciilib.grid import Grid


class Shape(ABC):
    @abstractmethod
    def draw(self, grid: Grid) -> None:
        pass
