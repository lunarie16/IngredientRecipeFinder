from ingredientFinder import IngredientRecipeFinder
from recipePrinter import Printer


if __name__ == "__main__":
    searchFor = input("\n\nPlease enter your search terms (comma seperated):\n> ")
    searchFor = searchFor.split(',')
    amountResults = input('Default results are 5, if you want more/less, please type in a number\n>')
    irf = IngredientRecipeFinder()
    printer = Printer()
    try:
        numberResults = int(amountResults)
        print(f'Results will be having {numberResults} results')
        result = irf(searchFor, numberResults)
        if result:
            printer.printResults(searchFor, result)

    except Exception as e:
        print(f'Results will be having 5 results (default)')
        result = irf.search(searchFor, numberResults)

        if result:
            printer.printResults(searchFor, result)
