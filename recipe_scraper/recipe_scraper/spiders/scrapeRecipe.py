import scrapy
from bs4 import BeautifulSoup


class ScrapeRecipeSpider(scrapy.Spider):
    name = "scrapeRecipe"

    def start_requests(self):
        f = open('names_urls.txt')
        lines = f.readlines()
        # for line in lines:
        #     url = line.split(';')[1]
        #     yield scrapy.Request(url=f'{url}', callback=self.parse)
        url = lines[0].split(';')[1]
        yield scrapy.Request(url=f'{url}', callback=self.parse)

    def parse(self, response):
        bs = BeautifulSoup(response.body, 'lxml')
        div = bs.find_all("wprm-recipe-ingredients")
        print(div)
        # f = open("names_urls.txt", 'a')
        # for entry in div:
        #     url = entry.get('href')
        #     recipeName = entry.get_text()
        #     f.write(f'{recipeName};{url}\n')
