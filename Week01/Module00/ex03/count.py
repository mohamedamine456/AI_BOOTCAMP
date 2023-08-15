import sys

def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if len(args) > 1:
        print("Error")
    # verify if the argument is a string
    elif not isinstance(args[0], str):
        print("AssertionError: argument is not a string")
    else:
        str_cal = input("What is the text to analyze?\n>> ") if not args else args[0]
        
        nb_maj = sum(1 for char in str_cal if char.isupper())
        nb_min = sum(1 for char in str_cal if char.islower())
        nb_pun = sum(1 for char in str_cal if char in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~")
        nb_space = sum(1 for char in str_cal if char.isspace())
        
        print(f"The text contains {len(str_cal)} characters:")
        print(f"- {nb_maj} upper letters")
        print(f"- {nb_min} lower letters")
        print(f"- {nb_pun} punctuation marks")
        print(f"- {nb_space} spaces")

if __name__ == "__main__":
    text_analyzer(*sys.argv[1:])