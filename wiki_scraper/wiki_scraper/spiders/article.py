import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Featured_articles']
    token_count = 0


    def parseArticle(self, response):
        text = ''.join(response.css('p ::text').extract())
        text_parts = text.split();
        self.token_count += len(text_parts)

        article = {
            'text': text
        }
        yield article

    def parse(self, response):
        host = self.allowed_domains[0]

        for link in response.css(".featured_article_metadata > a"):
            print(self.token_count)
            if self.token_count < 1000000:
                next_page_url = f"http://{host}{link.attrib.get('href')}"
                if next_page_url:
                    yield scrapy.Request(url=next_page_url, callback=self.parseArticle)
