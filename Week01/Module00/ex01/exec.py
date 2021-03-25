import sys

str = ""
i = len(sys.argv) - 1;
while i > 0 :
    j = len(sys.argv[i]) - 1
    while j >= 0:
        if sys.argv[i][j].isalpha():
            if sys.argv[i][j].isupper():
                str += sys.argv[i][j].lower()
            elif sys.argv[i][j].islower():
                str += sys.argv[i][j].upper()
        else:
            str += sys.argv[i][j]
        j -= 1
    i -= 1
    if i > 0:
        str += " "
print(str)
