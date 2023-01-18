
class Recipe:

    def __init__(self):
        self.name: str = ''
        self.ingredients: list[str] = []
        self.instructions: list[str] = []
        self.author: str = ''
        self.avg_rate: float = 0.0
        self.ratings: list[int] = []
        self.comments: list[int] = []
        self.calculate_ratings = lambda x: sum(x)/len(x)

    def setName(self, name: str):
        self.name = name

    def getName(self) -> str:
        return self.name

    def addIngredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def getIngredients(self) -> list:
        return self.ingredients

    def setInstructions(self, instructions: list):
        self.instructions = instructions

    def getInstructions(self) -> list:
        return self.instructions

    def setAuthor(self, author_name: str):
        self.author = author_name

    def getAuthor(self) -> str:
        return self.author

    def addRating(self, rating: int):
        self.ratings.append(rating)
        self.avg_rate = self.calculate_ratings(self.ratings)

    def getAvgRate(self) -> float:
        return self.avg_rate

    def addComment(self, comment: str):
        self.comments.append(comment)

    def getComments(self) -> list:
        return self.comments





