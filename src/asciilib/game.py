import tkinter as tk

from .color import Color
from .grid import Grid
from .shapes.shape import Shape  # Pylance is bugging out here


class Game:
    @staticmethod
    def _prevent_selection(event) -> str:  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]  # noqa: ANN001
        return "break"

    def __init__(
        self,
        width: int = 80,
        height: int = 24,
        title: str = "asciilib game",
        fg: Color = Color("white"),
        bg: Color = Color("black"),
        filler: str = " ",
    ) -> None:
        self.width = width
        self.height = height

        self.default_bg = bg
        self.default_fg = fg

        self.filler = filler
        self.title = title

        self.grid = Grid(width, height, filler)

    def draw(self, shape: Shape) -> None:
        shape.draw(self.grid)

    def start(self) -> None:
        root = tk.Tk()
        root.title(self.title)
        self.root = root

        self.area = tk.Text(
            self.root,
            width=self.width,
            height=self.height,
            font=("Courier", 10),
            bg=str(self.default_bg),
            fg=str(self.default_fg),
            padx=0,
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        )
        self.area.pack()

        self.area.bind("<Button-1>", self._prevent_selection)
        self.area.bind("<B1-Motion>", self._prevent_selection)

        self._render()
        self.root.mainloop()

    def _render(self) -> None:
        self.area.delete("1.0", tk.END)
        for y, row in enumerate(self.grid.content):
            self.area.insert(f"{y + 1}.0", "".join(row) + "\n")
        for y, row in enumerate(self.grid.colors):
            for x, color in enumerate(row):
                if color is not None:
                    color_str = str(color)
                    if color_str:
                        self.area.tag_add(
                            color_str, f"{y + 1}.{x}", f"{y + 1}.{x + 1}"
                        )
                        self.area.tag_config(color_str, foreground=color_str)

    def _set_char(
        self,
        x: int,
        y: int,
        char: str = "",
        color: Color | None = None,
    ) -> None:
        self.grid.set(x, y, char, color)


if __name__ == "__main__":
    Game().start()
