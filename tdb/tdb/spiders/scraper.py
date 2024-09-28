import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ScraperSpider(CrawlSpider):
    name = "scraper"

    def __init__(self, start_url=None, *args, **kwargs):
        super(ScraperSpider, self).__init__(*args, **kwargs)
        

        # Ensure a URL is provided, otherwise raise an error
        if not start_url:
            raise ValueError("You must be provided valid url to start crawling.")

        # Set the provided start URL
        self.start_urls = [start_url]

    rules = (Rule(LinkExtractor(), callback='parse', follow=True),
    )



    def parse(self, response):
        print(f"Processing: {response.url}")
        links = response.xpath('//h1/text()').getall()


        for link in links:
            yield {
                'text': link,
                'page': response.url
            }