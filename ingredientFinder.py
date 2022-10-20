import json


class IngredientRecipeFinder:
    def __init__(self, fileName: str = 'RecipeWithIngredients.jsonl'):
        if fileName.split('.')[-1] != "jsonl":
            raise ValueError('Invalid file-ending! Please provide an .jsonl file.')
        else:
            file = open(fileName, 'r')
            self.data = file.readlines()
            file.close()

    def search(self, searchTerms: list, numberResults: int = 5) -> list:
        """
        :param searchTerms:  list of terms with which to search in the recipe ingredients
        :param numberResults: amount of resulting recipes
        :return: results of len=numberResults
        """
        results = []
        for d in self.data:
            d = json.loads(d)
            ingredients = ' '.join(d['ingredients']).lower()
            score = 0
            found = []
            for term in searchTerms:
                ingredient = term.lower().strip()
                if ingredient in ingredients:
                    score += 1
                    found.append(ingredient.capitalize())
            finalScore = score / len(searchTerms)
            if finalScore > 0:
                d['score'] = finalScore
                d['foundIngredients'] = found
                results.append(d)
        results = sorted(results, key=lambda d: d['score'], reverse=True)
        if not results:
            print(f'Sorry, seems like we did not find ANY recipe with your searched terms: "{", ".join(searchTerms)}"')
            return []
        else:
            return results[:numberResults]
