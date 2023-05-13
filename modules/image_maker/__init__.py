from pydantic import validate_arguments
from urllib.request import urlretrieve

from .islands.heroic_races.lap import LapImageMaker

@validate_arguments
def make_island_images(content: dict):
    island_data = content["island_data"]
    laps = island_data["laps"]

    urlretrieve(island_data["dragons"][0]["image_url"], "image.png")

    for i, lap in enumerate(laps):
        maker = LapImageMaker(i, lap, "image.png")
        maker.save("imgs/{:02d}.png".format(i+1))