import time

from scrapy import Request, Spider


class KateSpadeSpider(Spider):
    name = 'Katespade-bot'
    start_urls = ['https://www.katespade.co.uk/en-gb/']

    def parse(self, response):
        navbar_links = response.css('#navigation > ul > li > a::attr(href)').extract()
        yield from [Request(response.urljoin(link), callback=self.parse_category) for link in navbar_links]

    def parse_category(self, response):
        product_links = response.css('.product-tile a::attr(href)').getall()
        yield from [Request(response.urljoin(link), callback=self.parse_product) for link in product_links]

    def parse_product(self, response):
        product = {
            "brand": "Kate Spade",
            "care": self.product_care(response),
            "category": self.product_category(response),
            "currency": "GBP",
            "date": time.time(),
            "description": self.product_description(response),
            "gender": "women",
            "image_urls": self.product_image_urls(response),
            'industry': None,
            "market": "UK",
            "name": self.product_name(response),
            "price": self.product_price(response),
            "retailer": "katespade-uk",
            "retailer_sku": self.product_retailer_sku(response),
            "skus": self.get_skus(response),
            'trail': [],
            "url": response.url,
            "url_original": self.start_urls,
            "uuid": None
        }

        yield product

    def product_name(self, response):
        return response.css('.name-link::text').extract_first().strip()

    def product_care(self, response):
        care = response.css("#small-details p::text").extract()
        material = response.css("ul~ ul li::text").extract()

        return care, material

    def product_description(self, response):
        return "\n".join(elem.strip() for elem in response.css('.description-details *::text').getall() if elem.strip())

    def product_category(self, response):
        return [response.css(".navigation-wrap a::text").get()]

    def product_image_urls(self, response):
        return [response.css('img::attr(src)').get()]

    def product_retailer_sku(self, response):
        return response.css(".product-number span::text").get()

    def product_color(self, response):
        return response.css(
            '#product-content > div.product-variations > div.attribute.color> h3 > span.attr-value::text').get()

    def product_sizes(self, response):
        return [size.strip() for size in response.css('.attribute.size .value .swatchanchor::text').getall()]

    def product_price(self, response):
        return [float(p.replace('£', '')) for p in response.css(".price-sales::text").extract() if p.strip()]

    def get_skus(self, response):
        skus = {}
        colour = self.product_color(response)
        price = self.product_price(response)
        sizes = self.product_sizes(response) or ['One Size']
        sku = {"colour": colour, "currency": "GBP", "price": price[0], "size": sizes}

        return {f"{colour}_{sizes[0]}": sku}
