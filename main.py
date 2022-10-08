import json

file = open('RecipeWithIngredients.jsonl', 'r')
data = file.readlines()


def search(searchTerms: list, amount_results: int = 5):
    result = []
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
            result.append(d)
    result = sorted(result, key=lambda d: d['score'], reverse=True)
    if not result:
        print(f'Sorry, seems like we did not find ANY recipe with your searched terms: "{", ".join(searchTerms)}"')
    else:
        printResults(searchTerms, result, amount_results)


def printResults(searchTerms: list, results: list, amount_results: int):
    results = results[:amount_results]
    print(
        f'Your searched terms: "{", ".join(searchTerms)}" have been found in the following {amount_results} recipes:\n')
    for i, result in enumerate(results):
        print(
            f'{i + 1}. {int(result["score"] * 100)}% match   {result["name"]}  ({result["url"]})\n    -> containing "{", ".join(result["foundIngredients"])}"\n')
    print()

    more = input('Do you want some introductions for a recipe? Type the given number for the recipe or enter "no":\n>')
    if more.lower() == 'no':
        exit()
    try:
        number = int(more)
        number = number - 1
        print(len(f'For "{results[number]["name"].upper()}" you need:') * '-')
        print(f'For "{results[number]["name"].upper()}" you need:')
        print(len(f'For "{results[number]["name"].upper()}" you need:') * '-')
        for ing in results[number]['ingredients']:
            print(f"->    {ing.strip()}\n")
        print('\n')
        print(len(f'Introductions') * '-')
        print(f'Introductions')
        print(len(f'Introductions') * '-', '\n')
        for j, inst in enumerate(results[number]['instructions']):
            inst = inst.replace('.', '.\n     ')
            print(f"{j + 1}.    {inst.strip()}\n")

    except Exception as e:
        print(e)
        print("Sorry, it seems like this wasn't a number or was exceeding your results index")


if __name__ == "__main__":
    searchFor = input("\n\nPlease enter your search terms (comma seperated):\n> ")
    searchFor = searchFor.split(',')
    amountResults = input('Default results are 5, if you want more/less, please type in a number, else type "no"\n>')
    try:
        number = int(amountResults)
        print(f'Results will be having {number} results')
        search(searchFor, amount_results=number)

    except Exception as e:
        print(f'Results will be having 5 results (default)')
        search(searchFor)



