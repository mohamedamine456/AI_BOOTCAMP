import random

def generator(text, sep=" ", option=None):
    if not text or isinstance(text, str) == False:
        print("ERROR: You Should Enter a text to work on")
        exit()
    elif option not in ["shuffle", "unique", "ordered", None]:
        print("ERROR: Please enter an option within this list['shuffle', 'unique', 'ordered']")
        exit()
    else:
        list_words = text.split(sep)
        new_list = []
        if option == "shuffle":
            random_numbers = []
            i = 0
            while i < len(list_words):
                n = random.randint(0, len(list_words) - 1)
                if n not in random_numbers:
                    random_numbers.append(n)
                    i += 1

            for j in random_numbers:
                new_list.append(list_words[j])
        elif option == "ordered":
            list_words.sort()
            new_list = list_words
        elif option == "unique":
            list_words = set(list_words)
            new_list = list(list_words)
        else:
            new_list = list_words

        for word in new_list:
            yield word
        
