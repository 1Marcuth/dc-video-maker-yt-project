from pydantic import validate_arguments
from PIL import Image

from ...base import ImageMaker
from .title import NodeTitleImageMaker
from .titles import NodeTitlesImageMaker
from ..mission import MissionImageMaker

class NodeImageMaker(ImageMaker):
    @validate_arguments
    def __init__(self, node: dict, node_index: int) -> None:
        self._node = node
        self._node_index = node_index

        self._bg = Image.new("RGBA", (600, 200), "#0000FF50")

        self.__build()

    def __build(self):
        self.__put_title_number()
        self.__put_titles()
        self.__put_missions()

    def __put_title_number(self):
        number = self._node_index + 1
        img = NodeTitleImageMaker(number).get()
        coord = (15, 0)

        self._bg.paste(img, coord, img)

    def __put_titles(self):
        has_spawn_time = False

        for mission in self._node["missions"]:
            if mission["spawn_time"]["one"]:
                has_spawn_time = True
                break
        
        img = NodeTitlesImageMaker(has_spawn_time).get()
        coord = (70, int(img.height / 2))

        self._bg.paste(img, coord, img)

    def __put_missions(self):
        for i, mission in enumerate(self._node["missions"]):
            img = MissionImageMaker(mission).get()

            x = 70
            y = 58 + (i * 75)

            coord = (x, y)

            self._bg.paste(img, coord, img)