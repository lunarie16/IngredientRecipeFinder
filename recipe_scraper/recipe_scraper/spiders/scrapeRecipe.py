import scrapy
from bs4 import BeautifulSoup
import jsonlines


class ScrapeRecipeSpider(scrapy.Spider):
    name = "scrapeRecipe"

    def __init__(self):
        self.recipeName = ''
        self.recipeURL = ''

    def start_requests(self):
        f = open('names_urls.txt')
        lines = f.readlines()
        for line in lines:
            self.recipeName, self.recipeURL = line.split(';')
            self.recipeURL = self.recipeURL.replace('\n', '')
            yield scrapy.Request(url=f'{self.recipeURL}', callback=self.parse)


    def parse(self, response):
        bs = BeautifulSoup(response.body, 'lxml')
        div = bs.find_all('div', class_="wprm-recipe-ingredient-group")
        ingredients = []
        for d in div:
            lists = d.find_all('li')
            for ing in lists:
                spans = ing.find_all('span')
                ingredient = []
                for i, span in enumerate(spans):
                    if i != 0:
                        ingredient.append(span.get_text().strip())
                ingredients.append(" ".join(ingredient).strip())
        with jsonlines.open('../RecipeWithIngredients.jsonl', mode='a') as writer:
            writer.write({
                'name': self.recipeName,
                'url': self.recipeURL,
                'ingredients': ingredients
                 })
