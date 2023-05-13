from pydantic import validate_arguments
from bs4 import Tag

from .mission import MissionParser

class NodeParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, tag: Tag) -> None:
        self._tag = tag

    @property
    def number(self) -> int:
        number = int(self._tag
            .select_one(".nnh")
            .text
            .split("-")[1]
            .strip()
            .removeprefix("Node"))

        return number

    @property
    def missions(self) -> list[dict]:
        missions_selector = self._tag.select(".ml")
        missions = [
            MissionParser(mission_selector).get()
            for mission_selector in missions_selector
        ]
        
        return missions

    def get(self) -> dict:
        return dict(
            number = self.number,
            missions = self.missions
        )