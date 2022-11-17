# IngredientRecipeFinder
This is a project for "Advanced Softwaretechnique" where a fixed website with vegan recipes is scraped and depending ingredients are extract. You can search by a (list of) ingredient(s) to find matching recipes. Let's reduce some food waste!
It is using the recipes from Bianca Zapatka (https://biancazapatka.com/de/), whom provides really good, easy and vegan recipes on her website/blog.

installing dependencies:
`pip install -r requirements.txt`


crawl data:
`sh start.sh`

start the program: 
`python main.py`

run tests with:
`python -m unittest tests.py`


Metrices:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
