class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not name or not isinstance(name, str):
            print("You didn't enter a string Name!")
            exit()
        elif not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            print("Enter a Cooking level number  in range 1 to 5!")
            exit()
        elif not isinstance(cooking_time, int) or cooking_time < 0:
            print("You Should enter a positive number for Cooking time!")
            exit()
        elif not isinstance(ingredients, list) or not ingredients:
            print("You didn't enter a list of  ingredients for recipe!")
            exit()
        elif not isinstance(description, str):
            print("description can be empty but can't be something else than a string")
            exit()
        elif not isinstance(recipe_type, str) or recipe_type not in ["starter", "lunch", "dessert"]:
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
        return f"Recipe for {self.name}:\n" \
               f"level of Cooking: {self.cooking_lvl}\n" \
               f"Takes {self.cooking_time} minutes of cooking.\n" \
               f"Ingredients list: {self.ingredients}\n" \
               f"The description of this recipe: {self.description}\n" \
               f"To be eaten for {self.recipe_type}."
