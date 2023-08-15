import sys

result = ""
for i, arg in enumerate(reversed(sys.argv[1:])):
    if i > 0:
        result += " "
    result += "".join(char.lower() if char.isupper() else char.upper() if char.islower() else char for char in reversed(arg))

print(result)