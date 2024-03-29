# IngredientRecipeFinder
This is a project for "Advanced Softwaretechnique" where a fixed website with vegan recipes is scraped and depending ingredients are extracted. You can search by a (list of) ingredient(s) to find matching recipes. Let's reduce some food waste!
It is using the recipes from Bianca Zapatka (https://biancazapatka.com/de/), whom provides really good, easy and vegan recipes on her website/blog.

installing dependencies:
`pip install -r requirements.txt`


crawl data:
`sh start.sh`

start the program (default english recipes): 
`python src/main/python/main.py`
for german option add: 
`-l de`


## 1. Git
usage of GitHub for the whole project time

&rarr; [See commit history here](https://github.com/lunarie16/IngredientRecipeFinder/commits/main)

## 2. UML 
UML Diagramm created with Planttext (Class, Component and User Diagrams for the project with Edlich's Fund)

&rarr; [PNGs and Planttext-Files](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/uml-diag)

## 3. DDD
Creation with Miro of Event Storming file and resulting Diagrams and DDD 

&rarr; [PDF-file with Event Storming, Diagram and DDD](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/Domain-Driven-Design.pdf)

## 4. Metrices
Creation of SonarCloud account and connecting to repository (with advanced settings) for metric badges:

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=bugs)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
<!-- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder) -->

## 5. Clean Code Dev
Adding clen code developemnt for improved usage and readabilty as well as for better maintance of code.

### A)
&rarr; [parameter and return types](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L13)

&rarr; [docstrings](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L15)

&rarr; [explanatory variable names](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L25)

&rarr; [throw exception with context](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L7)

&rarr; [one assert per test](https://github.com/lunarie16/IngredientRecipeFinder/blob/053c05a87481155602432f135db364b8468c7a3e/src/unittest/python/ingredientfinder_tests.py#L130)

### B)
Creation of a Cheat Sheet for upcoming projects 

&rarr; [Cheat Sheet](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/ccd-cheat-sheet.md)

## 6. Build
Usage of Pybuilder to build Project and have the ability to install and import as a package for usage in other projects 

&rarr; [with Pybuilder](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/target/dist/IngredientRecipeFinder-1.0.dev0): find files [here](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/target)

## 7. UnitTests
Writing UnitTests to keep correctness and desired functionality of algortihm 

! tests will be executed automatically with every push to respository -> with github actions (see 8.)
&rarr; [find tests here](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/src/unittest/python/ingredientfinder_tests.py)

run tests manually with:
`python3 -m unittest -v src/unittest/python/ingredientfinder_tests.py`

## 8. Continuous Delivery
Adding Github Action Test exectuion on every push to verify correctness of algorithm

&rarr; [GitHub Action - Test](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/.github/workflows)

## 9. IDE
Adding most favorite shortcuts here and create own to allow faster developemnt without lifting hands from keyboard

### Pycharm 
&rarr; *own Shortcut*: 
- ```option + r``` (run) 
  
&rarr; *build-in*:
- ```cmd + f``` (find)
- ```cmd + r``` (replace) 
- ```option + c/v/x``` (copy/paste/cut)
- ```cmd + /``` (comment (out))  
- ``` shift + ctrl + d``` (start debugger)

## 10. DSL
Usage of DSL like 'HTML' and 'regex' 

&rarr; [extraction of information from HTML content](https://github.com/lunarie16/IngredientRecipeFinder/blob/bb87c812dc109c53609cfde8f5f05a906a3e8672/recipe_scraper/recipe_scraper/spiders/scrapeRecipe.py#L19)

&rarr; [extraction of words with regex](https://github.com/lunarie16/IngredientRecipeFinder/blob/bb87c812dc109c53609cfde8f5f05a906a3e8672/src/main/python/main.py#L23)

## 11. Functional Programming
Apply functional programming for it's understanding and adding a class for Recipe as learned in Prog. I for java

&rarr; [only final data structures](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L5)

&rarr; [(mostly) side effect free functions](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L14)

&rarr; [use closures / anonymous functions](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/recipe.py#L12)

&rarr; [the use of higher-order functions/functions as parameters and return values](https://github.com/lunarie16/IngredientRecipeFinder/blob/1ee0024ea1816d2a820f3439ed63d91c83b5b9b6/src/main/python/main.py#L16)

