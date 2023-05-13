from modules import input_, scraper, image_maker

def main():
    content = {}

    input_.ask_island_type(content)
    scraper.scrape_island(content)
    image_maker.make_island_images(content)

    print(content)

if __name__ == "__main__":
    main()