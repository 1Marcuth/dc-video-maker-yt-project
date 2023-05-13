from pydantic import validate_arguments
import questionary
import logging

ISLAND_TYPES = [
    "heroic_races"
]

@validate_arguments(config=dict(arbitrary_types_allowed=True))
def ask_island_type(content: dict, logger: logging.Logger) -> None:
    choices = [
        dict(
            name = island_type.upper()
        )
        for island_type in ISLAND_TYPES
    ]

    logger.info("> [island-type-questioner] Asked for the type of the island...")

    question = questionary.select("> [island-type-questioner] Choose one island type: ", choices)
    content["island_type"]: str = question.ask().lower()