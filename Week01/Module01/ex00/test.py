from book import Book
from recipe import Recipe

try:
    recipe = Recipe("cake", 4, 8, ["farin", "chocolat"], "", "dessert")
    print(str(recipe))
except TypeError:
    print("Enter all args")
