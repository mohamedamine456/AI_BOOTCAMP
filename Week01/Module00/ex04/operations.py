import sys

if len(sys.argv) > 3:
    print("Input Error: too many arguments\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) < 3:
   print("age: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
    try:
        var1 = int(sys.argv[1])
        var2 = int(sys.argv[2])
        print("Sum:         " + str(var1 + var2))
        print("Difference:  " + str(var1 - var2))
        print("Product:     " + str(var1 * var2))
        try:
            print("Quotient:    " + str(float(var1) / float(var2)))
            print("Remainder:   " + str(var1 % var2))
        except ZeroDivisionError:
            print("Quotient:    ERROR (div by zero)")
            print("Remainder:   ERROR (modulo by zero)")

    except ValueError:
        print("Input Error: only numbers\n")
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("\tpython operations.py 10 3")
