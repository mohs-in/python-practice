# Exceptions
'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

def get_fuel(prompt):
    try:
        [a, b] = prompt.split('/')
        ratio = (int(a) / int(b)) * 100
        
        match ratio:
            case 0.0:
                return 'E'
            case 25.0:
                return '25%'
            case 50.0:
                return '50%'
            case 75.0:
                return '75%'
            case 100.0:
                return 'F'
            case _:
                pass
    except ValueError:
        print('Provided fraction is not a number')
    except ZeroDivisionError:
        print("Denominator can't be a zero")
        

def main():
    while True:
        try:
            fraction_input = input('Fraction: ')
        except:
            pass
        else:
            if get_fuel(fraction_input):
                print(get_fuel(fraction_input))
                break
        



main()
