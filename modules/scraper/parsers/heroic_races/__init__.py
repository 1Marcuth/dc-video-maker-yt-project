from pydantic import validate_arguments
from bs4 import BeautifulSoup

from ..settings import DRAGON_ELEMENTS, SECONDS_PER_DAY
from .lap import LapParser

class HeroicRacesParser:
    @validate_arguments
    def __init__(self, html: str) -> None:
        self._soup = BeautifulSoup(html, "html.parser")

    @property
    def name(self) -> str:
        name = (self._soup
            .select_one("h1")
            .text
            .strip()
            .removesuffix(" Heroic Race Guide"))

        return name

    @property
    def duration(self) -> int:
        duration = int(self._soup
            .select_one(".dur_text")
            .text
            .strip()
            .removeprefix("This event lasts ")
            .removesuffix(" days")) * SECONDS_PER_DAY

        return duration

    @property
    def dragons(self) -> list[dict]:
        dragons_selector = self._soup.select(".over")

        dragons = []

        for dragon_selector in dragons_selector:
            dragon_name = (dragon_selector
                .select_one(".pan_ic")
                .text
                .strip())

            dragon_rarity = (dragon_selector
                .select_one(".img_rar")
                .attrs["class"][0]
                .removeprefix("img_rp_")
                .upper())
            
            dragon_elements = [
                DRAGON_ELEMENTS[element_selector
                    .attrs["class"][1]
                    .removeprefix("tb_")] for element_selector in dragon_selector.select(".typ_i")
            ]

            dragon_image_url = (dragon_selector
                .select_one(".pan_img")
                .attrs["src"]
                .replace(" ", "%20")
                .replace("../../", "https://deetlist.com/dragoncity/"))

            dragon_page_url = (dragon_selector
                .select_one(".aitm a")
                .attrs["href"]
                .replace(" ", "%20")
                .replace("../../", "https://deetlist.com/dragoncity/"))

            dragons.append(dict(
                name = dragon_name,
                rarity = dragon_rarity,
                elements = dragon_elements,
                image_url = dragon_image_url,
                page_url = dragon_page_url
            ))

        return dragons

    @property
    def laps(self) -> list[dict]:
        laps_selector = self._soup.select(".hl")
        laps = [ LapParser(lap_selector).get() for lap_selector in laps_selector ]
        return laps

    def get(self) -> dict:
        return dict(
            name = self.name,
            duration = self.duration,
            dragons = self.dragons,
            laps = self.laps
        )

__all__ = [ "HeroicRacesParser" ]