t = (19, 42, 21)

chaine = "The " + str(len(t)) + " numbers are: "
i = 0

while i < len(t):
    chaine += str(t[i])
    i += 1
    if i < len(t):
        chaine += ", "

print(chaine)
