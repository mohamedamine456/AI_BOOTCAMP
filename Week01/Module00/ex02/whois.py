import sys


def check_number(num):
    try:
        num = int(num)
    except ValueError:
        print("AssertionError: argument must be an integer")
        return
    if num == 0:
        print("I'm Zero")
    elif num % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


if len(sys.argv) == 1:
    print("Usage: python program.py [integer]")
else:
    check_number(sys.argv[1])
