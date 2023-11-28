import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author_name = quote.css('span small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()

            yield {
                'text': text,
                'author': author_name,
                'tags': tags,
            }

            yield {
                'name': author_name,
                'birth_date': '',
                'birth_place': '',
                'bio': '',
            }