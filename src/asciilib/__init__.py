def __getattr__(name: str) -> object:
    match name:
        case "Color":
            from .color import Color

            return Color
        case "Grid":
            from .grid import Grid

            return Grid
        case "CharLib":
            from .chars import CharLib

            return CharLib
        case "Shape":
            from .shapes.shape import Shape

            return Shape
        case "Rectangle":
            from .shapes.rectangle import Rectangle

            return Rectangle
        case "Ellipse":
            from .shapes.ellipse import Ellipse

            return Ellipse
        case "Triangle":
            from .shapes.triangle import Triangle

            return Triangle
        case "Line":
            from .shapes.line import Line

            return Line
        case "Game":
            from .game import Game

            return Game
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
