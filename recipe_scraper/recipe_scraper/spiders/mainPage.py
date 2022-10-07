import scrapy
from bs4 import BeautifulSoup


class MainPageSpider(scrapy.Spider):
    name = "mainPage"

    def start_requests(self):
        url = 'https://biancazapatka.com/de/rezepte/hauptgerichte/page/'

        # while self.continueCrawling:
        # 26
        for i in range(1, 26):
            yield scrapy.Request(url=f'{url}{i}', callback=self.parse)

    def parse(self, response):
        bs = BeautifulSoup(response.body, 'lxml')
        div = bs.find_all(rel="bookmark")
        f = open("names_urls.txt.txt", 'a')
        for entry in div:
            url = entry.get('href')
            recipeName = entry.get_text()
            f.write(f'{recipeName};{url}\n')
