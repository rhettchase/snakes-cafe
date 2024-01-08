welcome_message = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
"""

appetizers = ["Wings", "Cookies", "Spring Rolls"]
appetizers_menu = f"""
Appetizers
----------
"""

for appetizer in appetizers:
    appetizers_menu += f"{appetizer}\n"

entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
entrees_menu = """
Entrees
-------
"""

for entree in entrees:
    entrees_menu += f"{entree}\n"

desserts = ["Ice Cream", "Cake", "Pie"]
desserts_menu = """
Desserts
--------
"""

for dessert in desserts:
    desserts_menu += f"{dessert}\n"

drinks = ["Coffee", "Tea", "Unicorn Tears"]
drinks_menu = """
Drinks
------
"""

for drink in drinks:
    drinks_menu += f"{drink}\n"
    
order_prompt = "***********************************\n** What would you like to order? **\n***********************************\n"

print(welcome_message)
print(appetizers_menu)
print(entrees_menu)
print(desserts_menu)
print(drinks_menu)
print(order_prompt)

# create variable for user input
user_order = ''
# create list to store order
# orders = []
# create dictionary to store teh counts of each item ordered
order_counts = {}

while user_order.lower() != 'quit':
    if user_order:
        # orders.append(user_order.lower())
        # update count for the current item in the dictionary. default value of 0 if key is not found
        order_counts[user_order] = order_counts.get(user_order, 0) + 1
        if order_counts[user_order] < 2:
            print(f"{order_counts[user_order]} order of {user_order} has been added to your meal")
        else: print(f"{order_counts[user_order]} orders of {user_order} have been added to your meal")
    # prompt user for new order
    user_order = input("> ").lower()

order_summary = """
Here is your complete order:
------
"""

for key, value in order_counts.items():
    order_summary += f"{key} x {value}\n"
    
print(order_summary)