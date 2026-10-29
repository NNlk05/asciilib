def __getattr__(name: str) -> object:
    if name == "Game":
        from .game import Game

        return Game
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
