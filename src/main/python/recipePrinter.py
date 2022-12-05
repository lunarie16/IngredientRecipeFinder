import re


class Printer:

    def print_results(self, search_terms: list, results: list):
        """
        :param search_terms: list of terms which were searched in the recipe ingredients
        :param results: list of results with dict obj of recipe, ordered by match score with ingredient
        :return: None
        """
        print(
            f'Your searched terms: "{", ".join(search_terms)}" '
            f'have been found in the following {len(results)} recipes:\n')
        for i, result in enumerate(results):
            print(
                f'{i + 1}. {int(result["score"] * 100)}% match   {result["name"]}  ({result["url"]})\n    '
                f'-> containing "{", ".join(result["foundIngredients"])}"\n')
        print()
        while True:
            more = input(f'Do you want some introductions for a recipe? '
                         f'Type the given number (1-{len(results)}) for the recipe or enter "no" to exit:\n>')
            if more.lower() == 'no':
                break
            if re.match(r"\d", more):
                numb = int(more)
                numb = numb - 1
                if numb >= len(results):
                    print(f"You requested recipe No. {more} but only have {len(results)} results.")
                else:
                    self.print_ingredients(results[numb]["name"], results[numb]['ingredients'])
                    print('\n')
                    self.print_introductions(results[numb]['instructions'])

            else:
                print("Sorry, it seems like this wasn't a number or was exceeding your results index")
        exit()

    def print_ingredients(self, recipe_name: str, ingredients: list):
        """
        :param recipe_name: recipe name from which ingredients will be printed
        :param ingredients: ingredients to the given recipeName
        :return:
        """
        header = f'For "{recipe_name.upper()}" you need:'
        border = len(header) * '-'
        print(border)
        print(header)
        print(border)
        for ing in ingredients:
            print(f"->    {ing.strip()}\n")

    def print_introductions(self, instructions: list):
        """
        :param instructions: instructions list of before selected recipe
        :return:
        """
        header = f'Introductions'
        border = len(header) * '-'
        print(border)
        print(header)
        print(border)
        for j, inst in enumerate(instructions):
            inst = inst.replace('.', '.\n     ')
            print(f"{j + 1}.    {inst.strip()}\n")