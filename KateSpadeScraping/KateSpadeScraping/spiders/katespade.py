import scrapy


class KatespadeBotSpider(scrapy.Spider):
    name = "katespade"
    url = ["https://www.katespade.co.uk/en-gb/"]

    def parse(self, response):
        navbar = response.css('#navigation > ul').extract()

        for link in navbar:
            yield scrapy.Request(navbar, callback=self.parse_products)

    def parse_products(self, response):
        names = self.parse_names(response)
        prices = self.parse_prices(response)
        images = self.parse_images(response)
        color = self.parse_color(response)
        description = self.parse_description(response)

    def parse_names(self, response):
        return response.css('.name-link::text').extract_first().strip()

    def parse_prices(self, response):
        return response.css('.product-price::text').extract()[-1].strip()

    def parse_images(self, response):
        return response.css('img::attr(src)').getall()

    def parse_color(self, response):
        return [c.split(': ')[1] for c in response.css('.swatchanchor::attr(title)').getall()]

    def parse_description(self, response):
        return [elem.strip() for elem in response.css('.description-details *::text').getall() if elem.strip()]
