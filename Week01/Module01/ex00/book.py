import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if not name or isinstance(name, str) == False:
            print("Please Enter a string Name for the Book!")
            exit()
        elif not last_update or isinstance(last_update, datetime.datetime) == False:
            print("Please Enter a datetime for last_update")
            exit()
        elif not creation_date or isinstance(creation_date, datetime.datetime) == False:
            print("Please Enter a datetime for creation_date")
            exit()
        elif not recipes_list or isinstance(recipes_list, list) == False:
            print("Please Enter a list of recipes for recipes_list")
            exit()
        else:
            self.name = name
            self.last_update = last_update
            self.creation_date = creation_date
            self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if name and isinstance (name, str) == True:
            for recipe in self.recipes_list:
                if recipe.name == name:
                    return str(recipe)
            print("The recipe name You are looking for doesn't exist in this list!")
        else:
            print("Please enter proper stringi name to search for!")
    
    
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type and isinstance(recipe_type, str) == True and recipe_type in ["starter", "lunch", "dessert"]:
            for recipe in self.recipes_list:
                if recipe.recipe_type == recipe_type:
                    return str(recipe)
        else:
            print("Please enter a proper string recipe_type in ['starter', 'lunch', 'dessert']")
    
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if recipe and isinstance(recipe, Recipe) == True:
            self.recipes_list.append(recipe)
            last_update = datetime.now()
        else:
            print("Please enter a proper instance of Recipe class!")
