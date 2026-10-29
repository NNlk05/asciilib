from ..color import Color
from ..grid import Grid
from .shape import Shape


class Triangle(Shape):
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
        if self.height == 0:
            return
        center_x = self.width // 2
        for y in range(self.height):
            if self.height == 1:
                half = self.width // 2
            else:
                half = int(
                    round((self.width - 1) * y / (2 * (self.height - 1)))
                )
            left = center_x - half
            right = center_x + half
            for x in range(left, right + 1):
                if x < 0 or x >= self.width:
                    continue
                on_border = x == left or x == right or y == self.height - 1
                if on_border:
                    grid.set(x, y, self.border, self.border_color)
                else:
                    grid.set(x, y, self.fill, self.fill_color)
