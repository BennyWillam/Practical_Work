import random

quick_picks_number = int(input("How many tickets today? "))
NUMBERS_IN_TICKET = 6
MINIMUM = 1
MAXIMUM = 45

if quick_picks_number == 0:
    print("Nothing today? Thats ok, carry on.")
else:
    for number in range(quick_picks_number):
        ticket_numbers = []
        for i in range(NUMBERS_IN_TICKET):

        TICKET_NUMBERS = [random.randint(1, 45) for i in range(6) if i + 1 != i]
        print(TICKET_NUMBERS)
