import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    #allowed_domains = ["booktoscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        for livros in response.css('.col-lg-3'):
            yield{
                'title' : livros.css('h3 a::text').get(),
                'preco' : livros.css('.price_color ::text').get()
            }
        pass
