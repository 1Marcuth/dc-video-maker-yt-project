from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments

from ...base import ImageMaker

class InputPointsImageMaker(ImageMaker):
    @validate_arguments
    def __init__(self, quantity: int) -> None:
        self._quantity = quantity

        self._bg = Image.new("RGBA", (85, 25), "#fff")
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self):
        self.__put_quantity()

    def __put_quantity(self):
        quantity = str(self._quantity)
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 17)
        coord = (
            self._bg.width / 2,
            self._bg.height / 2
        )

        self._draw.text(
            coord,
            quantity,
            "#000",
            font,
            "mm"
        )