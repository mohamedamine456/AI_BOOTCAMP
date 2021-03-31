import sys
if len(sys.argv) != 3 or sys.argv[1].isdigit() == True or sys.argv[2].isdigit() == False:
    print("ERROR")
else:
    tab_words = sys.argv[1].split()
    filter_tab = []
    for i in range(len(tab_words)):
        if len(tab_words[i]) > int(sys.argv[2]):
            filter_tab.append(tab_words[i])
    for i in range(len(filter_tab)):
        for char in filter_tab[i]:
            if char in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~":
                filter_tab[i] = filter_tab[i].replace(char, '')
    print(filter_tab)
