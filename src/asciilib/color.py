class Color:
    def __init__(self, value: str | tuple[int, int, int]) -> None:
        if isinstance(value, tuple):
            r, g, b = value
            self.value = f"#{r:02x}{g:02x}{b:02x}"
        elif value == "":
            self.value = None
        else:
            self.value = value

    def __str__(self) -> str:
        return self.value if self.value is not None else ""
