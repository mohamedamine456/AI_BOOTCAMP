from book import Book
from recipe import Recipe
import datetime

try:
    recipe = Recipe("cake", 4, 8, ["farin", "chocolat"], "", "dessert")
    listofrecipes = [recipe]
    book = Book("book", datetime.datetime(2019, 1, 1), datetime.datetime(2019, 1, 2), listofrecipes)
    # book.add_recipe(recipe)
    print(book.get_recipe_by_name("cake"))
    print(book.get_recipes_by_types("dessert"))
    # print(book.get_recipes_by_types("lunch"))
    # print(book.get_recipes_by_types("starter"))
except TypeError as e:
    print("Enter all args")
    print(e)
