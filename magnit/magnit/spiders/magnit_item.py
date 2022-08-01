import scrapy
import csv

class MarketSpider(scrapy.Spider):
    name = "smm"
    start_urls = ["https://sbermegamarket.ru/catalog/noutbuki/"]

    def parse(self, response, **kwargs):
        for link in response.css("div.item-title a::attr(href)"):
            yield response.follow(link, callback=self.parse_laptop)

        for page in range(1, 5):
            next_page = f'https://sbermegamarket.ru/catalog/noutbuki/page-{page}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_laptop(self, response):
        yield {
            # "title": response.css("span.pdp-header__title.page-title ::text").get(),
            "title": response.xpath('//article/div[1]/header/span/text()').get(),
            # "new_price": response.css("span.pdp-sales-block__price-final ::text").get(),
            "new_price": response.xpath("//div[@class='prod-buy']/div[1]/div[3]/div[1]/span/text()").get(),
            # "old_price": response.css("div.pdp-sales-block__old-price-small ::text").get(),
            "old_price": response.xpath("//div[@class='prod-buy']/div[1]/div[2]/div[2]/text()").get(),
            # "sale": response.css("div.discount-percentage__value ::text").get()
            "sale": response.xpath("//div[@class='prod-buy']/div[1]/div[2]/div[1]/div[2]/text()").get()

        }

