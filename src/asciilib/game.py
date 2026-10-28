import tkinter as tk


class Game:
    @staticmethod
    def _prevent_selection(event) -> str:  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]  # noqa: ANN001
        return "break"

    def __init__(
        self,
        width: int = 80,
        height: int = 24,
        title: str = "asciilib game",
        fg: str = "white",
        bg: str = "black",
        filler: str = " ",
    ) -> None:
        self.width = width
        self.height = height

        self.default_bg = bg
        self.default_fg = fg

        self.filler = filler
        self.title = title

        self.content = [
            [self.filler for _ in range(width)] for _ in range(height)
        ]

        self.colors = [[None for _ in range(width)] for _ in range(height)]

    def start(self) -> None:
        root = tk.Tk()
        root.title(self.title)
        self.root = root

        self.area = tk.Text(
            self.root,
            width=self.width,
            height=self.height,
            font=("Courier", 10),
            bg=self.default_bg,
            fg=self.default_fg,
            padx=0,
            pady=0,
            borderwidth=0,
            highlightthickness=0,
        )
        self.area.pack()

        self._render()
        self.root.mainloop()

    def _render(self) -> None:
        self.area.delete("1.0", tk.END)
        for y, row in enumerate(self.content):
            self.area.insert(f"{y + 1}.0", "".join(row) + "\n")
        for y, row in enumerate(self.colors):
            for x, color in enumerate(row):
                if color is not None:
                    self.area.tag_add(
                        color, f"{y + 1}.{x}", f"{y + 1}.{x + 1}"
                    )
                    self.area.tag_config(color, foreground=color)

    def _set_char(
        self,
        x: int,
        y: int,
        char: str = "",
        color: str | None = None,
    ) -> None:
        self.content[y][x] = char
        self.colors[y][x] = color
