class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not name or isinstance(name, str) == False:
            print("You didn't enter a string Name!")
            exit()
        elif isinstance(cooking_lvl, int) == False or cooking_lvl not in range(1, 6):
            print("Enter a Cooking level number  in range 1 to 5!")
            exit()
        elif isinstance(cooking_time, int) == False or cooking_time < 0:
            print("You Should enter a positive number for Cooking time!")
            exit()
        elif isinstance(ingredients, list) == False or not ingredients:
            print("You didn't enter a list of  ingredients for recipe!")
            exit()
        elif isinstance(description, str) == False:
            print("description can be empty but can't be something else than a string")
            exit()
        elif isinstance(recipe_type, str) == False or recipe_type not in ["starter", "lunch", "dessert"]:
            print("Recipe Type should be a string in {'starter', 'lunch', 'dessert'}")
            exit()
        else:
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
    def __str__(self):
        """Return the string to print with the recipe info"""
        rinfo = ""
        rinfo += "Recipe for {}:\n".format(self.name)
        rinfo += "level of Cooking: {}\n".format(self.cooking_lvl)
        rinfo += "Takes {} minutes of cooking.\n".format(self.cooking_time)
        rinfo += "Ingredients list: {}\n".format(self.ingredients)
        if self.description:
            rinfo += "The description of this recipe: {}\n".format(self.description)
        rinfo += "To be eaten for {}.\n".format(self.recipe_type)
        return (rinfo)
