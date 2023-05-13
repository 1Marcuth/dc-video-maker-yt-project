from pydantic import validate_arguments
import requests
import logging

from .parsers import parse_html

ISLAND_URLS = {
    "heroic_races": "https://deetlist.com/dragoncity/events/race/"
}

@validate_arguments(config=dict(arbitrary_types_allowed=True))
def scrape_island(content: dict, logger: logging.Logger) -> None:
    logger.info("> [scrape-island] Starting...")

    island_type = content["island_type"]
    url = ISLAND_URLS[island_type]

    logger.info(f"> [scrape-island] Getting HTML data from url '{url}'...")

    response = requests.get(url)
    html = response.text

    if response.status_code != 200:
        logger.error(f"A status code error '{response.status_code}' occurred while trying to get the HTML for the page from url '{url}'!")
        raise Exception(f"A status code error '{response.status_code}' occurred while trying to get the HTML for the page from url '{url}'!")

    logger.info(f"> [scrape-island] HTML of page url '{url}' successfully fetched!")
    logger.info(f"> [scrape-island] Extracting data from page HTML from url '{url}'...")

    content["island_data"] = parse_html(html, island_type)

    logger.info(f"> [scrape-island] HTML data extraction from page url '{url}' completed successfully!")