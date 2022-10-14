class Printer:

    def printResults(self, searchTerms: list, results: dict):
        """
        :param searchTerms: list of terms which were searched in the recipe ingredients
        :param results: list of results with dict obj of recipe, ordered by match score with ingredient
        :return: None
        """
        print(
            f'Your searched terms: "{", ".join(searchTerms)}" have been found in the following {len(results)} recipes:\n')
        for i, results in enumerate(results):
            print(
                f'{i + 1}. {int(results["score"] * 100)}% match   {results["name"]}  ({results["url"]})\n    -> containing "{", ".join(results["foundIngredients"])}"\n')
        print()

        # TODO: write while input() to not make it exit after wrong input
        more = input(
            'Do you want some introductions for a recipe? Type the given number for the recipe or enter "no":\n>')
        if more.lower() == 'no':
            exit()
        try:
            numb = int(more)
            numb = numb - 1
            if numb > len(results):
                print(f"You requested recipe No. {numb} but only searched for {amount_results} results.")
                exit()
            else:
                self.printIngredients(results[numb]["name"], results[numb]['ingredients'])
                print('\n')
                self.printIntroductions(results[numb]['instructions'])

        except Exception as e:
            print(e)
            print("Sorry, it seems like this wasn't a number or was exceeding your results index")

    def printIngredients(self, recipeName: str, ingredients: list):
        """
        :param recipeName: recipe name from which ingredients will be printed
        :param ingredients: ingredients to the given recipeName
        :return:
        """
        header = f'For "{recipeName.upper()}" you need:'
        border = len(header) * '-'
        print(border)
        print(header)
        print(border)
        for ing in ingredients:
            print(f"->    {ing.strip()}\n")

    def printIntroductions(self, instructions: list):
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