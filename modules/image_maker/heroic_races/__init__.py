from pydantic import validate_arguments
from urllib.request import urlretrieve
from PIL import Image, ImageFilter
from pyfilter import FromDictList
import pathutil
import os

from .lap import LapImageMaker

@validate_arguments
def make_images(content: dict) -> None:
    island_type = content["island_type"]
    island_data = content["island_data"]

    if island_type == "heroic_races":
        laps = island_data["laps"]

        heroic_dragon = FromDictList(island_data["dragons"]).get_with_key_value("rarity", "H")

        island_dirname = (island_type + "_" +
            heroic_dragon["name"]
            .lower()
            .replace(" ", "_"))
        
        output_dir = f"content/{island_dirname}"
        laps_output_dir = os.path.join(output_dir, "laps")
        heroic_dragon_img_file_path = os.path.join(output_dir, "heroic_dagon.png")

        if not os.path.exists(output_dir):
            pathutil.mktree(output_dir)

        urlretrieve(heroic_dragon["image_url"], heroic_dragon_img_file_path)

        lap_bg = (Image
            .open("assets/imgs/background.jpg")
            .convert("RGBA")
            .filter(ImageFilter.BoxBlur(2.5)))

        effect_img = Image.open("assets/imgs/effects/satin.png")

        lap_bg.paste(effect_img, (0, 0), effect_img)

        for lap_index, lap in enumerate(laps):
            lap_number = lap_index + 1
            lap_filename = "lap_{:02d}.png".format(lap_number)
            lap_file_path = os.path.join(laps_output_dir, lap_filename)

            if not os.path.exists(laps_output_dir):
                pathutil.mktree(laps_output_dir)
            
            maker = LapImageMaker(
                lap_index,
                lap,
                heroic_dragon_img_file_path,
                lap_bg.copy()
            )

            maker.save(lap_file_path)