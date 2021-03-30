t = (19, 42, 21)

"""
# First solution
chaine = "The " + str(len(t)) + " numbers are: "
i = 0

while i < len(t):
    chaine += str(t[i])
    i += 1
    if i < len(t):
        chaine += ", "

print(chaine)
"""

# Second solution

print("The 3 numbers are: %(first)d, %(second)d, %(third)d" % {"first":t[0], "second":t[1], "third":t[2]})
