"""
In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
"""

str = input() # Takes the input from the user

print(str.replace(" ", "...")) # here, str.replace() replaces the space with "..."