from pydantic import validate_arguments
from PIL import Image

from .spawn_time import SpawnTimeImageMaker

class SpawnTimesImageMaker:
    @validate_arguments
    def __init__(
        self,
        spawn_time: dict,
    ) -> None:
        self._spawn_time = spawn_time

        self._bg = Image.new("RGBA", (120, 52))

        self.__build()

    def __build(self):
        self.__put_time_one()
        self.__put_time_all()

    def __put_time_one(self):
        label_text = "p/item"
        img = SpawnTimeImageMaker(self._spawn_time["one"], label_text).get()
        coord = (0, 0)

        self._bg.paste(img, coord, img)
    
    def __put_time_all(self):
        label_text = "Total"
        img = SpawnTimeImageMaker(self._spawn_time["all"], label_text).get()
        coord = (0, 27)

        self._bg.paste(img, coord, img)

    def get(self) -> Image.Image:
        return self._bg