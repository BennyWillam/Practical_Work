"""
Program a 'cart' that can display the number of items and their price,
from which it can calculate a total.
If over $100, there is a 10% discount applied to the total
"""

# Asking for user input to begin the calculations
number_of_items = int(input("How many items are there? "))
# The total is zeroed off before the process to be able to add in sequence
total = 0

# A while loop is used so the user can't input incorrectly
while number_of_items < 0:
    print("Invalid number of items. Please enter a valid number")
    # A variable to input items
    number_of_items = int(input("How many items are there? "))

for price_of_item in range(1, number_of_items + 1):
    price_of_item = float(input("What is the item worth? $"))
    while price_of_item < 0:
        print("Invalid amount. Please re-evaluate")
        price_of_item = float(input("What is the item worth? $"))
    total += price_of_item
if total > 100:
    total = total * 0.9
else:
    total = total
print("$", "%.2f" % total)
