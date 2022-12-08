import scrapy
from bs4 import BeautifulSoup
import jsonlines


class ScrapeRecipeSpider(scrapy.Spider):
    name = "scrapeRecipe"

    def start_requests(self):
        f = open('names_urls.txt')
        lines = f.readlines()
        for line in lines:
            nameUrl = line.split(';')
            information = {'name': nameUrl[0], 'url': nameUrl[1].replace('\n', '')}
            yield scrapy.Request(url=f'{information["url"]}', callback=self.parse, cb_kwargs=information)

    def parse(self, response, name, url):
        bs = BeautifulSoup(response.body, 'lxml')
        div = bs.find_all('div', class_="wprm-recipe-ingredient-group")
        ingredients = []
        for d in div:
            lists = d.find_all('li', class_="wprm-recipe-ingredient")
            for ing in lists:
                spans = ing.find_all('span')
                ingredient = []
                for i, span in enumerate(spans):
                    if i != 0:
                        ingredient.append(span.get_text().strip())
                ingredient = list(filter(None, ingredient))
                ingredient = [words for segments in ingredient for words in segments.split()]
                ingredients.append(ingredient)

        div2 = bs.find_all('li', class_="wprm-recipe-instruction")
        instructions = []
        for d in div2:
            span = d.get_text()
            if span:
                instructions.append(span.strip())

        with jsonlines.open('../RecipeWithIngredients.jsonl', mode='a') as writer:
            writer.write({
                'name': name,
                'url': url,
                'ingredients': ingredients,
                'instructions': instructions
                 })
