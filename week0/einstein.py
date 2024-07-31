"""
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""

c = 300000000 # speed of light taken approx.

m = input("M: ") # Takes the input from the user

E = int(m) * (c**2) # calculate 

print("E:", E)