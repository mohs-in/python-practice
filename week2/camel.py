"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
"""


def main():
    camel = input('camel: ')
    res = ''
    for i in range(0, len(camel)):
        if i == 0:
            res += camel[i].lower()
        elif camel[i].isupper():
            res += '_'
            res += camel[i].lower()
        elif not camel[i].isupper():
            res += camel[i]
    print(res)

main()





# FileNameIs

# file_name_is