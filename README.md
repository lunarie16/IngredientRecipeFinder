# IngredientRecipeFinder
This is a project for "Advanced Softwaretechnique" where a fixed website with vegan recipes is scraped and depending ingredients are extracted. You can search by a (list of) ingredient(s) to find matching recipes. Let's reduce some food waste!
It is using the recipes from Bianca Zapatka (https://biancazapatka.com/de/), whom provides really good, easy and vegan recipes on her website/blog.

installing dependencies:
`pip install -r requirements.txt`


crawl data:
`sh start.sh`

start the program: 
`python src/main/python/main.py`


## 1. Git
&rarr; [See commit history here](https://github.com/lunarie16/IngredientRecipeFinder/commits/main)

## 2. UML 
&rarr; [PNGs and Planttext-Files](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/uml-diag)

## 3. DDD
&rarr; [PDF-file with Event Storming, Diagram and DDD](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/Domain-Driven-Design.pdf)

## 4. Metrices
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=bugs)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder)
<!-- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lunarie16_IngredientRecipeFinder&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lunarie16_IngredientRecipeFinder) -->

## 5. Clean Code Dev
### A)
&rarr; [parameter and return types](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L13)

&rarr; [docstrings](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L15)

&rarr; [explanatory variable names](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L25)

&rarr; [throw exception with context](https://github.com/lunarie16/IngredientRecipeFinder/blob/4fdee32c880bd9b0ddc84ddf32752fb916c3f81f/ingredientFinder.py#L7)

&rarr; [one assert per test](https://github.com/lunarie16/IngredientRecipeFinder/blob/053c05a87481155602432f135db364b8468c7a3e/src/unittest/python/ingredientfinder_tests.py#L130)

### B)
&rarr; [Cheat Sheet](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/ccd-cheat-sheet.md)

## 6. Build
&rarr; [with Pybuilder](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/target/dist/IngredientRecipeFinder-1.0.dev0)

## 7. UnitTests
! tests will be executed automatically with every push to respository -> with github actions (see 8.)
&rarr; [find tests here](https://github.com/lunarie16/IngredientRecipeFinder/blob/main/src/unittest/python/ingredientfinder_tests.py)

run tests manually with:
`python3 -m unittest -v src/unittest/python/ingredientfinder_tests.py`

## 8. Continuous Delivery
&rarr; [GitHub Action - Test](https://github.com/lunarie16/IngredientRecipeFinder/tree/main/.github/workflows)

## 9. IDE
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
&rarr; TODO

## 11. Functional Programming
&rarr; TODO

