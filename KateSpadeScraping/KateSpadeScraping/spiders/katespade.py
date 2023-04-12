from scrapy import Request, Spider


class KateSpadeSpider(Spider):
    name = 'Katespade-bot'
    start_urls = ['https://www.katespade.co.uk/en-gb/']

    def parse(self, response):
        navbar_links = response.css('#navigation > ul > li > a::attr(href)').extract()

        for link in navbar_links:
            yield Request(response.urljoin(link), callback=self.parse_category)

    def parse_category(self, response):
        product_links = response.css('.product-tile a::attr(href)').getall()

        for link in product_links:
            yield Request(response.urljoin(link), callback=self.parse_product)

    def parse_product(self, response):
        skus = []
        product_name = response.css('.name-link::text').extract_first().strip()
        product_url = response.url
        brand_name = "Kate Spade"
        description = [elem.strip() for elem in response.css('.description-details *::text').getall() if elem.strip()]
        currency = "GBP"
        category = response.css(".navigation-wrap a::text").get()
        image_urls = response.css('img::attr(src)').get()
        gender = "women"
        market = "UK"
        retailer = "katespade-uk"
        retailer_sku = response.css(".product-number span::text").get()

        for variant in response.css('.product-variations-select option'):
            color = variant.css('.color::text').get()
            size = variant.css('.size::text').get()
            price = variant.css('.product-price::text').get()
            if color and size:
                sku = {
                    "colour": color,
                    "size": size,
                    "currency": currency,
                    "price": price,
                    "sku": f"{color}-{size}"
                }
                skus.append(sku)

        product = {
            "product_name": product_name,
            "product_url": product_url,
            "brand_name": brand_name,
            "description": "\n".join(description),
            "currency": currency,
            "category": category,
            "image_urls": image_urls,
            "gender": gender,
            "market": market,
            "retailer": retailer,
            "retailer_sku": retailer_sku,
            "skus": skus,
        }
        print("-------------------------------------PRODUCTS-----------------------------------------")
        for i in product:
            print(i, product[i])
            yield product
