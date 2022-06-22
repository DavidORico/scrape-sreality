import scrapy
import json


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]

    # url found through inspecting js queries with the networking tool on https://www.sreality.cz/hledani/prodej/byty
    start_urls = (
        'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=60&tms=1655716126496',
    )

    def parse(self, response):
        data = json.loads(response.text)
        count = 0
        for estate in data["_embedded"]["estates"]:
            yield {
                "name": estate["name"],
                "location": estate["locality"],
                "photo_urls": [url["href"] for url in estate["_links"]["images"]]}
            count += 1
            if count == 50:
                break
