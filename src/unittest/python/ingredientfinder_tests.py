import unittest
try:
    from ingredientFinder import IngredientRecipeFinder

except ModuleNotFoundError:
    from ...main.python.ingredientFinder import IngredientRecipeFinder


class IngredientRecipeFinderGermanTest(unittest.TestCase):

    def setUp(self):
        self.irf = IngredientRecipeFinder('data/RecipeWithIngredients.jsonl')

    def test_typoInTerm(self):
        terms = ['Basilikuum']
        result = self.irf.search(terms)
        self.assertEqual(len(result), 0)

    def test_amountDefaultResults(self):
        terms = ['Nudeln']
        results = self.irf.search(terms)
        self.assertEqual(len(results), 5)

    def test_inputResult(self):
        terms = ['Nudeln']
        amountResults = 10
        results = self.irf.search(terms, amountResults)
        self.assertEqual(len(results), 10)

    def test_stringAsInputType(self):
        terms = 'Nudeln'
        result = self.irf.search(terms)
        self.assertIsNotNone(result)

    def test_orderOfResults(self):
        terms = ['Nudeln', 'Butter', 'Basilikum']
        result = self.irf.search(terms)
        self.assertGreaterEqual(result[0]['score'], result[1]['score'])

