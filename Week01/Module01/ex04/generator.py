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
            i = 0
            while i < len(list_words):
                rand = random.randint(0, len(list_words) - i)
                new_list.append(list_words[rand])
                list_words.remove(list_words[rand])
                i += 1
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
        
