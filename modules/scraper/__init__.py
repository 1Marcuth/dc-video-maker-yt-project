from pydantic import validate_arguments
import requests

from .parsers import parse_html

ISLAND_URLS = {
    "heroic_races": "https://deetlist.com/dragoncity/events/race/"
}

@validate_arguments
def scrape_island(content: dict) -> None:
    island_type = content["island_type"]
    url = ISLAND_URLS[island_type]
    content = content
    response = requests.get(url)
    html = response.text
    content["island_data"] = parse_html(html, island_type)