_MODIFIER_MAP = {
    "ctrl": "Control",
    "shift": "Shift",
    "alt": "Alt",
    "meta": "Meta",
}

_MODIFIER_ORDER = ("ctrl", "shift", "alt", "meta")


def _expand_keybinding(keybinding: str) -> list[tuple[frozenset[str], str]]:
    combinations: list[tuple[frozenset[str], str | None]] = []
    for pattern in keybinding.split(" or "):
        pattern_combos: list[tuple[frozenset[str], str | None]] = [
            (frozenset(), None)
        ]

        for token in [token.strip() for token in pattern.split("+")]:
            if token.startswith("[") and token.endswith("]"):
                modifier = token[1:-1]
                expanded: list[tuple[frozenset[str], str | None]] = []

                for modifiers, key in pattern_combos:
                    expanded.append((modifiers, key))
                    expanded.append((modifiers | {modifier}, key))
                pattern_combos = expanded
            elif token.startswith("{") and token.endswith("}"):
                choices = [choice.strip() for choice in token[1:-1].split(",")]
                expanded = []\
                
                for modifiers, key in pattern_combos:
                    for choice in choices:
                        expanded.append((modifiers | {choice}, key))
                pattern_combos = expanded
            elif token in _MODIFIER_MAP:
                pattern_combos = [
                    (modifiers | {token}, key)
                    for modifiers, key in pattern_combos
                ]
            else:
                pattern_combos = [
                    (modifiers, token) for modifiers, key in pattern_combos
                ]
        
        combinations.extend(
            (modifiers, key)
            for modifiers, key in pattern_combos
            if key is not None
        )
    return combinations


def _keybinding_to_events(keybinding: str, event_type: str) -> list[str]:
    events: list[str] = []
    for modifiers, key in _expand_keybinding(keybinding):
        ordered = [
            _MODIFIER_MAP[modifier]
            for modifier in _MODIFIER_ORDER
            if modifier in modifiers
        ]
        parts = [*ordered, event_type, key]
        events.append(f"<{'-'.join(parts)}>")
    return events
