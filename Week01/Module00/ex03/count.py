import sys
import string


def text_analyzer(*args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if len(args) > 1:
        print("Error")
    # verify if the argument is a string
    elif args and not isinstance(args[0], str):
        print("AssertionError: argument is not a string")
    else:
        text = input("What is the text to analyze?\n>> ") if not args else args[0]
        upper_count = sum(1 for c in text if c.isupper())
        lower_count = sum(1 for c in text if c.islower())
        punct_count = sum(1 for c in text if c in string.punctuation)
        space_count = sum(1 for c in text if c.isspace())
        print(f"The text contains {len(text)} characters:")
        print(f"- {upper_count} upper letters")
        print(f"- {lower_count} lower letters")
        print(f"- {punct_count} punctuation marks")
        print(f"- {space_count} spaces")


if __name__ == "__main__":
    text_analyzer(*sys.argv[1:])
