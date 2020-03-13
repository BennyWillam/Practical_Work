"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    menu = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
    """
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2F}".format(temp_cel(celsius)))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print("Result: {:.2f} C".format(temp_fa(fahrenheit)))
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you.")


def temp_cel(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def temp_fa(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


main()
