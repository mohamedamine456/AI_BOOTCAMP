import sys
import string

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
    print("ERROR")
else:
    words = sys.argv[1]
    n = int(sys.argv[2])
    filter_tab = [word.translate(str.maketrans('', '', string.punctuation)) for word in words.split() if len(word) > n]
    print(filter_tab)
