from book import Book
from recipe import Recipe
import datetime

try:
    # Create some Recipe objects
    recipe1 = Recipe("Pasta Carbonara", 3, 30, ["pasta", "egg", "bacon"], "A classic Italian pasta dish", "lunch")
    recipe2 = Recipe("Chocolate Cake", 4, 60, ["flour", "cocoa", "sugar"], "A rich and moist chocolate cake", "dessert")
    recipe3 = Recipe("Salad", 2, 15, ["lettuce", "tomato", "cucumber"], "A healthy green salad", "starter")

    my_book = Book("My Recipe Book", datetime.datetime(2019, 1, 1), datetime.datetime(2019, 1, 2), [recipe1, recipe2, recipe3])
    my_book.add_recipe(recipe1)
    my_book.add_recipe(recipe2)
    my_book.add_recipe(recipe3)

    print(my_book.get_recipe_by_name("Pasta Carbonara"))
    print(my_book.get_recipes_by_types("dessert"))
except TypeError as e:
    print("Enter all args")
    print(e)
