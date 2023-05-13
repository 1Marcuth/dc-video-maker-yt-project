from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments
import time

ImageObject = Image.Image

class SpawnTimeImageMaker:
    @validate_arguments
    def __init__(self, seconds: int, label_text: str) -> None:
        self._seconds = seconds
        self._label_text = label_text

        self._bg = Image.new("RGBA", (60, 25))
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self):
        self.__put_frame()
        self.__put_time()
        self.__put_label()

    def __put_frame(self):
        img = Image.new("RGBA", (57, 25), "#fff")
        coord = (0, 0)
        self._bg.paste(img, coord, img)

    def __put_label(self):
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 13)

        x = int(self._bg.width * 1.5)
        y = int(self._bg.height / 2)

        coord = (x, y)

        self._draw.text(
            coord,
            self._label_text,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=1
        )

    def __put_time(self):
        formated_time = time.strftime("%H:%M", time.gmtime(self._seconds))
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 13)

        x = (57 / 2)
        y = self._bg.height / 2

        coord = (x, y)

        self._draw.text(
            coord,
            formated_time,
            "#000",
            font,
            "mm"
        )

    def get(self) -> ImageObject:
        return self._bg

__all__ = [ "SpawnTimeMaker" ]