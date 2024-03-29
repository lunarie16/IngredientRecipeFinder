from ingredientFinder import IngredientRecipeFinder
from recipePrinter import Printer
import re
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find recipes with given ingredients.')
    parser.add_argument('-lang', default='en', type=str, choices=['en', 'de'],
                        help='language to use: de (for german) or en (for english, default)')

    args = parser.parse_args()
    if args.lang == 'en':
        irf = IngredientRecipeFinder()
    else:
        irf = IngredientRecipeFinder('data/RecipeWithIngredients.jsonl')
        search = irf.search
    printer = Printer()

    while True:
        search_for = input("\n\nPlease enter your search terms (comma seperated):\n> ")
        search_terms = search_for.split(',')
        amount_results = input('Default results are 5, if you want more/less, please type in a number\n>')
        result = None
        if re.match(r"\d", amount_results):
            numberResults = int(amount_results)
            print(f'Results will be having {numberResults} results')
            result = search(search_terms, numberResults)

        else:
            print(f'Results will have 5 recipes (default)')
            result = search(search_terms)

        if result:
            printer.print_results(search_terms, result)
            break
        else:
            print(f"Ooops, we didn't find anything matching your ingredients: {search_for}")

