def text_analyzer(*args):
    '''This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.'''
    if len(args) > 1:
        print("Error")
    else:
        if len(args) == 0:
            print("What is the text to analyse?")
            str_cal = raw_input(">> ")
        elif len(args) == 1:
            str_cal = args[0]
        i = 0
        nb_maj = 0
        nb_min = 0
        nb_pun = 0
        nb_space = 0
        punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~"
        while i < len(str_cal):
            if str_cal[i] in punctuation:
                nb_pun += 1
            elif str_cal[i].isspace():
                nb_space += 1
            elif str_cal[i].islower():
                nb_min += 1
            elif str_cal[i].isupper():
                nb_maj += 1
            i += 1
        print("The text contains " + str(len(str_cal)) + " characters:")
        print("- " + str(nb_maj) + " upper letters")
        print("- " + str(nb_min) + " lower letters")
        print("- " + str(nb_pun) + " punctuation marks")
        print("- " + str(nb_space) + " spaces")
