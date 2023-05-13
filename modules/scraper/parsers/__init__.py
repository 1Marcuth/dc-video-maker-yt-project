from .heroic_races import HeroicRacesParser

def parse_html(html: str, island_type: str) -> dict:
    if island_type == "heroic_races":
        parser = HeroicRacesParser(html)

    else:
        raise ValueError(f"O tipo de ilha '{island_type}' não é um tipo aceito pelo parser!")

    data = parser.get()
    return data