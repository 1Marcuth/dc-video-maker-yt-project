from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments

ImageObject = Image.Image

class NodeTitlesImageMaker:
    @validate_arguments
    def __init__(self, has_spawn_time: bool) -> None:
        self._has_spawn_time = has_spawn_time

        self._bg = Image.new("RGBA", (538, 30))
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self):
        self.__put_icon_title()
        self.__put_task_title()
        self.__put_goal_points_title()
        self.__put_pool_size_title()

        if self._has_spawn_time:
            self.__put_spawn_time_title()

    def __put_icon_title(self):
        title = "Ícone"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 20)
        coord = (25, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_task_title(self):
        title = "Tarefa"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 20)
        coord = (125, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_goal_points_title(self):
        title = "Itens"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 20)
        coord = (242.5, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_pool_size_title(self):
        title = "Máximo"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 20)
        coord = (347.5, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_spawn_time_title(self):
        title = "Espere"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 20)
        coord = (452.5, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def get(self) -> ImageObject:
        return self._bg