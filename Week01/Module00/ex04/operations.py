import sys


def arithmetic_operations(num1, num2):
    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    try:
        quot_result = num1 / num2
        mod_result = num1 % num2
    except ZeroDivisionError:
        quot_result = "ERROR (div by zero)"
        mod_result = "ERROR (modulo by zero)"
    return sum_result, diff_result, prod_result, quot_result, mod_result


if len(sys.argv) > 3:
    print("Input Error: too many arguments\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
elif len(sys.argv) < 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        sum_result, diff_result, prod_result, quot_result, mod_result = arithmetic_operations(num1, num2)
        print(f"Sum:         {sum_result}")
        print(f"Difference:  {diff_result}")
        print(f"Product:     {prod_result}")
        print(f"Quotient:    {quot_result}")
        print(f"Remainder:   {mod_result}")
    except ValueError:
        print("Input Error: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
