from pydantic import validate_arguments
from bs4 import Tag

from .node import NodeParser

class LapParser:
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(self, tag: Tag) -> None:
        self._tag = tag

    @property
    def number(self) -> int:
        number = int(self._tag
            .select_one(".nnh")
            .text
            .strip()
            .split("-")[0]
            .removeprefix("Lap"))

        return number

    @property
    def nodes(self) -> list[dict]:
        nodes_selector = self._tag.select(".nn")
        nodes = [ NodeParser(node_selector).get() for node_selector in nodes_selector ]
        return nodes

    def get(self) -> dict:
        return dict(
            number = self.number,
            nodes = self.nodes
        )