'''
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
'''

def main():
    cart_list = []

    while True:
        try:
            buy_input = input('').upper()
            cart_list.append(buy_input)    
        except EOFError:
            print('Exicted successfully.')
            break
    
    cart_dict = {}
    for item in cart_list:
        if item in cart_dict:
            cart_dict[item] += 1
        else:
            cart_dict[item] = 1
            
    for item in sorted(cart_dict):
        print(f'{cart_dict[item]} {item}')
        
        
main()