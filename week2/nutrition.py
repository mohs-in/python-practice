'''
The U.S. Food & Drug Adminstration (FDA) offers 
downloadable/printable[https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version] 
posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
'''

input_fruit = input('Item: ').lower()


def get_calories(input_fruit):
    match input_fruit:
        case 'apple':
            return 130
        case 'avocado':
            return 50
        case 'banana':
            return 110
        case 'cantaloupe':
            return 50
        case 'grapefruit':
            return 60
        case 'grapes':
            return 90
        case 'honeydew melon':
            return 50
        case 'kiwifruit':
            return 90
        case 'lemon':
            return 15
        case 'lime':
            return 20
        case 'nectarine':
            return 60
        case 'orange':
            return 80
        case 'peach':
            return 60
        case 'pear':
            return 100
        case 'pineapple':
            return 50
        case 'plums':
            return 70
        case 'strawberries':
            return 50
        case 'sweet cherries':
            return 100
        case 'tangenrine':
            return 50
        case 'watermelon':
            return 80
        case _:
            return None
        
    

print(f'Calories: {get_calories(input_fruit)}')