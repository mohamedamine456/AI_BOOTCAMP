import random

guess = 0
tries = 0
secret = random.randint(1, 99)

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
while True:
    tries += 1
    print("What's Your guess between 1 and 99?")
    guess = input(">> ")
    if guess == "exit":
        print("Goodbye!")
        exit()
    elif not guess.isdigit():
        print("That's not a number")
    else:
        guess = int(guess)
        if guess == secret:
            if secret == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if tries == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"Congratulations, you've got it!\nYou won in {tries} attempts!")
            break
        else:
            print("To high!") if guess > secret else print("To low!")
