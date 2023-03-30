import scrapy


class BooksToscrapeSpider(scrapy.Spider):
    name = "books.toscrape"
    #allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/index.html"]

    def parse(self, response):
        for livros in response.css('.col-lg-3'):
            yield{
                'title' : livros.css('h3 a::text'),
                'preco' : livros.css('.price_color ::text')
            }
        pass
