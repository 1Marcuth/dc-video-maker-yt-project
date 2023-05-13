from pydantic import validate_arguments
from bs4 import Tag

from ..utils.time_parser import parse_spawn_time

MISSION_TYPES = {
    "Collect Gold": "gold",
    "Hatch Eggs": "hatch",
    "Collect Food": "food",
    "Feed Dragons": "feed",
    "Breed Dragons": "breed",
    "Battle Dragons": "fight",
    "League Battles": "pvp"
}

class MissionParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, tag: Tag) -> None:
        self._tag = tag

    @property
    def name(self) -> str:
        name = self._tag.select_one(".mh").text
        return name

    @property
    def type(self) -> str:
        name = self.name
        type_ = MISSION_TYPES[name]
        return type_

    @property
    def goal_points(self) -> int:
        goal_points = int(self._tag.select_one(".mz:nth-child(1) .m2").text)
        return goal_points

    @property
    def pool_size(self) -> int:
        pool_size = int(self._tag.select_one(".mz:nth-child(2) .m2").text)
        return pool_size

    @property
    def spawn_time(self) -> int:
        spawn_time_for_one = parse_spawn_time(self._tag.select_one(".mz:nth-child(3) .m2").text)
        spawn_time_for_all = parse_spawn_time(self._tag.select_one(".mz:nth-child(5) .m2").text)

        return dict(
            one = spawn_time_for_one,
            all = spawn_time_for_all
        )

    @property
    def spawn_chance(self) -> float:
        spawn_chance = int(self._tag.select_one(".mz:nth-child(4) .m2").text.removesuffix("%")) / 100
        return spawn_chance

    def get(self) -> dict:
        return dict(
            name = self.name,
            type = self.type,
            goal_points = self.goal_points,
            pool_size = self.pool_size,
            spawn_time = self.spawn_time,
            spawn_chance = self.spawn_chance
        )