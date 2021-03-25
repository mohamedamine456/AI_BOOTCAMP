import sys

if len(sys.argv) > 2 or sys.argv[1].isdigit() == False:
    print("Error")
else:
    if int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even")
    elif int(sys.argv[1]) % 2 == 1:
        print("I'm Odd")
