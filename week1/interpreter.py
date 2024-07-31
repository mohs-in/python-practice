"""
In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!
"""

in_str = input("Expression: ")

elements = in_str.split(' ')

test_list = list(filter(None, elements))

x = int(test_list[0])

y = test_list[1]

z = int(test_list[2])

match y:
    case '+':
        result = float(x+z)
    case '-':
        result = float(x-z)
    case '*':
        result = float(x*z)
    case '/':
        result = float(x/z)

print(result)