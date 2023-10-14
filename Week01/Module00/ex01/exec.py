import sys


def reverse_and_swap_case(string):
    return string[::-1].swapcase()


if len(sys.argv) == 1:
    print("Usage: python exec.py [string1] [string2] ...")
else:
    string = " ".join(sys.argv[1:])
    result = reverse_and_swap_case(string)
    print(result)
