import json


class IngredientRecipeFinder:
    def __init__(self, filename: str = 'RecipeWithIngredients.jsonl'):
        if filename.split('.')[-1] != "jsonl":
            raise ValueError('Invalid file-ending! Please provide an .jsonl file.')
        else:
            f = open(filename, 'r')
            self.data = f.readlines()
            f.close()

    def search(self, search_terms: list, number_results: int = 5) -> list:
        """
        :param search_terms:  list of terms with which to search in the recipe ingredients
        :param number_results: amount of resulting recipes
        :return: results of len=numberResults
        """
        results = []
        for d in self.data:
            d = json.loads(d)
            ingredients = ' '.join(d['ingredients']).lower()
            score = 0
            found = []
            for term in search_terms:
                ingredient = term.lower().strip()
                if ingredient in ingredients:
                    score += 1
                    found.append(ingredient.capitalize())
            final_score = score / len(search_terms)
            if final_score > 0:
                d['score'] = final_score
                d['foundIngredients'] = found
                results.append(d)
        results = sorted(results, key=lambda e: e['score'], reverse=True)
        if not results:
            return []
        else:
            return results[:number_results]
