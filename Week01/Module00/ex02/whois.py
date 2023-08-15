import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
elif sys.argv[1].isdigit() == False:
    print("AssertionError: argument is not an integer")
else:
    print("I'm Zero") if int(sys.argv[1]) == 0 else print("I'm Even") if int(sys.argv[1]) % 2 == 0 else print("I'm Odd")
