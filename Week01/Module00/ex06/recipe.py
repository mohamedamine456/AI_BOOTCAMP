cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}

recipe_values = ["ingredients", "meal", "prep_time"]


def start():
    choices = [
        "Add a recipe",
        "Delete a recipe",
        "Print a recipe",
        "Print the cookbook",
        "Quit",
    ]
    while True:
        try:
            print("Please select an option by typing the corresponding number:")
            for i, choice in enumerate(choices):
                print("{}: {}".format(i + 1, choice))
            choice = int(input(">> "))

            if choice == 1:
                user_add_recipe()
                continue

            if choice == 2:
                recipe_name = input("Enter the name of the recipe you want to delete: ")
                delete_recipe(recipe_name)
                continue

            if choice == 3:
                recipe_name = input("Please enter the recipe's name to get its details: ")
                print_recipe(recipe_name)
                continue

            if choice == 4:
                print_all_recipe_names()
                continue

            if choice == 5:
                print("Cookbook closed.")
                break
            else:
                print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        except ValueError:
            print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")


def user_add_recipe():
    user_inputs = list()
    recipe_name = input("Enter the recipe name: ")
    for v in recipe_values:
        user_input = input("Enter the {}: ".format(v))
        if v == recipe_values[0]:
            user_input = user_input.split(" ")
        user_inputs.append(user_input)
    add_recipe(recipe_name, user_inputs[0], user_inputs[1], user_inputs[2])
    user_inputs.clear()


def print_recipe(name: str):
    if cookbook.get(name):
        recipe = cookbook[name]
        print(f"Recipe for {name}:")
        print(f"Ingredients list: {recipe['ingredients']}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
        print()
    else:
        print("No such recipe name")

def delete_recipe(name: str):
    if cookbook.get(name):
        cookbook.pop(name)
    else:
        print("No such recipe name")


def add_recipe(recipe_name: str, ingredients: list, meal_type: str, prep_time: str):
    recipe = dict(ingredients=ingredients, meal=meal_type, prep_time=prep_time)
    cookbook[recipe_name] = recipe


def print_all_recipe_names():
    for recipe_name in cookbook.keys():
        print_recipe(recipe_name)

if __name__ == "__main__":
    start()
