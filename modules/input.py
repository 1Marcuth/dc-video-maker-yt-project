from pydantic import validate_arguments
import questionary

ISLAND_TYPES = [
    "heroic_races"
]

@validate_arguments
def ask_island_type(content: dict) -> None:
    choices = [
        dict(
            name = island_type.upper()
        )
        for island_type in ISLAND_TYPES
    ]

    question = questionary.select("Choose one island type: ", choices)
    content["island_type"]: str = question.ask().lower()