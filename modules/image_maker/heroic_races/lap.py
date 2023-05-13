from PIL import Image, ImageDraw, ImageFont
from pydantic import validate_arguments
from typing import Optional

from ..base import ImageMaker
from .node import NodeImageMaker

class LapImageMaker(ImageMaker):
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def __init__(
        self,
        lap_index: int,
        lap: dict,
        dragon_img_file_path: str,
        bg: Optional[Image.Image] = None
    ) -> None:
        self._lap = lap
        self._lap_index = lap_index
        self._lap_number = lap_index + 1
        self._dragon_img_file_path = dragon_img_file_path

        self._bg = bg or Image.new("RGB", (1280, 720), "#fff")
        self._draw = ImageDraw.Draw(self._bg)

        self.__build()

    def __build(self) -> None:
        self.__put_title()
        self.__put_heroic_dragon_image()
        self.__put_nodes()

    def __put_nodes(self) -> None:
        initial_x = 30
        initial_y = 30

        for i, node in enumerate(self._lap["nodes"]):
            img = NodeImageMaker(node, i).get()

            match i:
                case 0:
                    x = initial_x
                    y = initial_y

                case 1:
                    x = initial_x
                    y = initial_y + img.height + 30
                
                case 2:
                    x = initial_x + img.width + 25
                    y = initial_y

                case 3:
                    x = initial_x + img.width + 25
                    y = initial_y + img.height + 30

                case 4:
                    x = initial_x + img.width + 25
                    y = initial_y + (img.height * 2) + 60

            coord = (x, y)

            self._bg.paste(img, coord, img)

    def __put_heroic_dragon_image(self) -> None:
        img = Image.open(self._dragon_img_file_path)
        img = img.resize((250, 250), Image.ANTIALIAS)
        coord = (38, 465)

        self._bg.paste(img, coord, img)

    def __put_title(self) -> None:
        lap_label_text = "Lap"
        formated_lap_number = f"{lap_label_text} {self._lap_number}"
        coord = (491, 590)
        font = ImageFont.truetype("assets/fonts/curse_casual.ttf", 80)

        self._draw.text(
            coord,
            formated_lap_number,
            "#fff",
            font,
            "mm",
            stroke_fill="#000",
            stroke_width=3
        )