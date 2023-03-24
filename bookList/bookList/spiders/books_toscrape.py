import scrapy


class BooksToscrapeSpider(scrapy.Spider):
    name = "books.toscrape"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        pass
