'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''
def main():
    amount_due = 50
    
    while amount_due != 0:
        print(f'Amount Due: {amount_due}')
        entered_amount = int(input('Insert Coin: '))
        if entered_amount == 5 or entered_amount == 10 or entered_amount == 25:
            amount_due -= entered_amount

    print(f'Amount Due: {amount_due}')

main()