from modules import input_, scraper, image_maker
from utils.logger import get_logger
from utils.file import write_json

def main():
    content = {}

    logger = get_logger()

    input_.ask_island_type(content, logger)
    scraper.scrape_island(content, logger)
    image_maker.make_island_images(content, logger)

    write_json("content.json", content)

if __name__ == "__main__":
    main()