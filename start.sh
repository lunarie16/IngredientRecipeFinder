if [ -f recipe_scraper/names_urls.txt ]; then
  echo "Already crawled recipe names and urls"
else
  cd recipe_scraper
  scrapy crawl mainPage
  echo "Crawling recipe names and urls was successful"
  cd ..
fi

if [ -f RecipeWithIngredients.jsonl ]; then
  echo "Already crawled all information from recipes"
else
  cd recipe_scraper
  scrapy crawl scrapeRecipe
  echo "Crawling all recipe informations was successful"
  cd ..
fi
