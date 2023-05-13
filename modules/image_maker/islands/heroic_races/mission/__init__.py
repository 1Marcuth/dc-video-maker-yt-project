from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments
import os

from .spawn_times import SpawnTimesImageMaker
from .input_points import InputPointsImageMaker

ImageObject = Image.Image

class MissionImageMaker:
    @validate_arguments
    def __init__(
        self,
        mission: dict
    ) -> None:
        self._mission = mission

        self._bg = Image.new("RGBA", (530, 50))
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self):
        self.__put_icon()
        self.__put_type_name()
        self.__put_goal_points()
        self.__put_pool_size()

        if self._mission["spawn_time"]["one"]:
            self.__put_spawn_times()

    def __put_icon(self):
        task_type = self._mission["type"]
        img_path = os.path.join("assets/imgs/heroic_races/mission/items/", f"{task_type}.png")
        img = Image.open(img_path).resize((50, 50))
        coord = (0, 0)

        self._bg.paste(img, coord, img)

    def __put_type_name(self):
        type_name = self._mission["name"]
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 17)
        coord = (125, self._bg.height / 2)

        self._draw.text(
            coord,
            type_name,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_goal_points(self):
        img = InputPointsImageMaker(self._mission["goal_points"]).get()

        x = 200
        y = int((self._bg.height / 2) - (img.height / 2))

        coord = (x, y)

        self._bg.paste(img, coord, img)

    def __put_pool_size(self):
        img = InputPointsImageMaker(self._mission["pool_size"]).get()

        x = 305
        y = int((self._bg.height / 2) - (img.height / 2))

        coord = (x, y)

        self._bg.paste(img, coord, img)

    def __put_spawn_times(self):
        img = SpawnTimesImageMaker(self._mission["spawn_time"]).get()

        x = 410
        y = int((self._bg.height / 2) - (img.height / 2))

        coord = (x, y)

        self._bg.paste(img, coord, img)

    def get(self) -> Image.Image:
        return self._bg