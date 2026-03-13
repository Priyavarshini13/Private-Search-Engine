import scrapy

class WebSpider(scrapy.Spider):
    name = "pages"
    start_urls = [
        "https://example.com",
        "https://wikipedia.org"
    ]

    def parse(self, response):
        title = response.css("title::text").get()
        yield {
            "url": response.url,
            "title": title,
            "content": response.text
        }

        links = response.css("a::attr(href)").getall()
        for link in links:
            yield response.follow(link, self.parse)