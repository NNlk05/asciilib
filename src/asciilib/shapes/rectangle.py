from ..color import Color
from ..grid import Grid
from .shape import Shape


class Rectangle(Shape):
    def __init__(
        self,
        width: int,
        height: int,
        fill: str = "",
        border: str = "",
        fill_color: Color = Color(""),
        border_color: Color = Color(""),
    ) -> None:
        self.width = width
        self.height = height
        self.fill = fill
        self.border = border
        self.fill_color = fill_color
        self.border_color = border_color

    def draw(self, grid: Grid) -> None:
        for y in range(self.height):
            for x in range(self.width):
                on_border = (
                    x == 0
                    or x == self.width - 1
                    or y == 0
                    or y == self.height - 1
                )
                if on_border:
                    grid.set(x, y, self.border, self.border_color)
                else:
                    grid.set(x, y, self.fill, self.fill_color)
