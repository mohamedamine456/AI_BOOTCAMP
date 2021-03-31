cookbook = {}
sandwich = {"ingredients":["ham", "break", "cheese", "tomates"], "meal": "lunch", "prep_time": 10}
cake = {"ingredients": ["floour", "sugar", "eggs"], "meal": "desser", "prep_time": 60}
salad = {"ingredients": ["avocado", "arugula", "tomates", "spinach"], "meal": "lunch", "prep_time": 15}

def print_recipe(name):
    try:
        recipe = cookbook[name]
        print("")
        print("Recipe for {}:".format(name))
        print("Ingredients list: {}".format(recipe["ingredients"]))
        print("To be eaten for {}.".format(recipe["meal"]))
        print("Takes {} minutes of cooking.".format(recipe["prep_time"]))
        print("")
    except KeyError:
        print("The recipe you entered is not in the list! You can add it if you want.")

def delete_recipe(name):
    del(cookbook[name])

def add_recipe(name, ingredients, meal, prep_time):
    recipe = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    cookbook[name] = recipe
        
def print_cookbook():
    print("")
    if len(cookbook) != 0 :
        print("The Cookbook contains:")
        for key, recipe in cookbook.items():
            print_recipe(key)
    else:
        print("CookBook is Empty")
    print("")

def switcher(choice):
    try:
        choice = int(choice)
    except ValueError:
        choice = 0
    if choice == 1:
        print("Please Enter The Recipe's name to Add")
        name = raw_input(">> ")
        if name  == "sandwich":
            add_recipe(name, sandwich["ingredients"], sandwich["meal"], sandwich["prep_time"])
        elif name == "cake":
            add_recipe(name, cake["ingredients"], cake["meal"], cake["prep_time"])
        elif name == "salad":
            add_recipe(name, salad["ingredients"], salad["meal"], salad["prep_time"])
        else:
            print ('Please enter a recipe within this list : ["sandwich", "cake", "salad"]')
    elif choice == 2:
        print("Please Enter The Recipe's name to Delete")
        name = raw_input(">> ")
        delete_recipe(name)
    elif choice == 3:
        print("Please Enter The Recipe's name To get its Details")
        name = raw_input(">> ")
        if name in ["sandwich", "cake", "salad"]:
            print_recipe(name)
        else:
            print("There is no recipe by this name {}".format(name))
    elif choice == 4:
        print_cookbook()
    elif choice == 5:
        print("Glad to have you in our app!")
        exit()
    else:
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5")
        choice = raw_input(">> ")
        switcher(choice)

choice = 0

while True :
    print("Please select an option by typing the corresponding number:")
    print("1: Add a Recipe")
    print("2: Delete a Recipe")
    print("3: Print a recipe")
    print("4: Print the Cookbook")
    print("5: Quit")
    choice  = raw_input(">> ")
    switcher(choice)

