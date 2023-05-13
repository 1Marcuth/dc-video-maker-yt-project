from pydantic import validate_arguments
import logging

from . import heroic_races

@validate_arguments(config=dict(arbitrary_types_allowed=True))
def make_island_images(content: dict, logger: logging.Logger) -> None:
    logger.info("> [island-image-maker] Starting...")

    island_type = content["island_type"]

    logger.info(f"> [island-image-maker] Creating island event images of type '{island_type}'...")

    if island_type == "heroic_races":
        heroic_races.make_images(content)

    else:
        raise Exception("Island type not acceptable!")

    logger.info(f"> [island-image-maker] Island event images of type '{island_type} have been successfully created!")