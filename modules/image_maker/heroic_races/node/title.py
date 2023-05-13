from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments

from ...base import ImageMaker

class NodeTitleImageMaker(ImageMaker):
    @validate_arguments
    def __init__(self, number: int) -> None:
        self.__number = number

        self._bg = Image.new("RGBA", (200, 200))
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self):
        self.__put_title_number()
        self.__rotate_img()
        self.__crop_img()

    def __put_title_number(self):
        title_label_text = "Node"
        title = f"{title_label_text} {self.__number}"
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 35)
        coord = (self._bg.width / 2, self._bg.height / 2)

        self._draw.text(
            coord,
            title,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=2
        )

    def __rotate_img(self):
        self._bg = self._bg.rotate(90)

    def __crop_img(self):
        self._bg = self._bg.crop((80, 0, 127, 200))