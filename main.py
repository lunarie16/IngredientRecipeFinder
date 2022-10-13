import json

file = open('RecipeWithIngredients.jsonl', 'r')
data = file.readlines()


def search(searchTerms: list):
    results = []
    for d in data:
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
        return
    else:
        return results


def printResults(searchTerms: list, results: dict, amount_results: int = 5):
    results = results[:amount_results]
    print(
        f'Your searched terms: "{", ".join(searchTerms)}" have been found in the following {amount_results} recipes:\n')
    for i, results in enumerate(results):
        print(
            f'{i + 1}. {int(results["score"] * 100)}% match   {results["name"]}  ({results["url"]})\n    -> containing "{", ".join(results["foundIngredients"])}"\n')
    print()

    more = input('Do you want some introductions for a recipe? Type the given number for the recipe or enter "no":\n>')
    if more.lower() == 'no':
        exit()
    try:
        numb = int(more)
        numb = numb - 1
        printIngredients(results[numb]["name"], results[numb]['ingredients'])
        print('\n')
        printIntroductions(results[numb]['instructions'])

    except Exception as e:
        print(e)
        print("Sorry, it seems like this wasn't a number or was exceeding your results index")


def printIngredients(recipeName: str, ingredients: list):
    header = f'For "{recipeName.upper()}" you need:'
    border = len(header) * '-'
    print(border)
    print(header)
    print(border)
    for ing in ingredients:
        print(f"->    {ing.strip()}\n")


def printIntroductions(instructions: list):
    header = f'Introductions'
    border = len(header) * '-'
    print(border)
    print(header)
    print(border)
    for j, inst in enumerate(instructions):
        inst = inst.replace('.', '.\n     ')
        print(f"{j + 1}.    {inst.strip()}\n")


if __name__ == "__main__":
    searchFor = input("\n\nPlease enter your search terms (comma seperated):\n> ")
    searchFor = searchFor.split(',')
    amountResults = input('Default results are 5, if you want more/less, please type in a number\n>')
    try:
        numberResults = int(amountResults)
        print(f'Results will be having {numberResults} results')
        result = search(searchFor)
        if result:
            printResults(searchFor, result, numberResults)

    except Exception as e:
        print(f'Results will be having 5 results (default)')
        result = search(searchFor)

        if result:
            printResults(searchFor, result)


