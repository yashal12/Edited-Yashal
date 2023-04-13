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
        product_name = self.get_product_name(response)
        product_url = response.url
        brand_name = "Kate Spade"
        description = self.get_description(response)
        currency = "GBP"
        category = self.get_category(response)
        image_urls = self.get_image_urls(response)
        gender = "women"
        market = "UK"
        retailer = "katespade-uk"
        retailer_sku = self.get_retailer_sku(response)
        color = self.get_color(response)
        sizes = self.get_sizes(response)
        price = self.get_price(response)
        skus = self.get_skus(color, sizes, currency, price)

        product = {
            "product_name": product_name,
            "product_url": product_url,
            "brand_name": brand_name,
            "description": description,
            "currency": currency,
            "category": category,
            "image_urls": image_urls,
            "gender": gender,
            "market": market,
            "retailer": retailer,
            "retailer_sku": retailer_sku,
            "skus": skus,
        }

        for i in product:
            print(i, product[i])
        yield product

    def get_product_name(self, response):
        return response.css('.name-link::text').extract_first().strip()

    def get_description(self, response):
        return "\n".join(elem.strip() for elem in response.css('.description-details *::text').getall() if elem.strip())

    def get_category(self, response):
        return response.css(".navigation-wrap a::text").get()

    def get_image_urls(self, response):
        return response.css('img::attr(src)').get()

    def get_retailer_sku(self, response):
        return response.css(".product-number span::text").get()

    def get_color(self, response):
        return response.css(
            '#product-content > div.product-variations > div.attribute.color> h3 > span.attr-value::text').get()

    def get_sizes(self, response):
        return [size.strip() for size in response.css('.attribute.size .value .swatchanchor::text').getall()]

    def get_price(self, response):
        return [float(p.replace('£', '')) for p in response.css(".price-sales::text").extract() if p.strip()]

    def get_skus(self, color, sizes, currency, price):
        skus = []
        skus.append({"colour": color, "size": sizes, "currency": currency, "price": price})
        return skus






