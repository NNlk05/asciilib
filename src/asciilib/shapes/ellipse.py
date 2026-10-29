from ..color import Color
from ..grid import Grid
from .shape import Shape


class Ellipse(Shape):
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
        if self.width == 0 or self.height == 0:
            return
        cx = (self.width - 1) / 2
        cy = (self.height - 1) / 2
        rx = max((self.width - 1) / 2, 1e-9)
        ry = max((self.height - 1) / 2, 1e-9)

        def inside(x: int, y: int) -> bool:
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                return False
            dx = (x - cx) / rx
            dy = (y - cy) / ry
            return dx * dx + dy * dy <= 1

        for y in range(self.height):
            for x in range(self.width):
                if not inside(x, y):
                    continue
                on_border = not (
                    inside(x - 1, y)
                    and inside(x + 1, y)
                    and inside(x, y - 1)
                    and inside(x, y + 1)
                )
                if on_border:
                    grid.set(x, y, self.border, self.border_color)
                else:
                    grid.set(x, y, self.fill, self.fill_color)
