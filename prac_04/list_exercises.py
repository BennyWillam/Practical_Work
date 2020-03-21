usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    username_verification()
    printing(numbers=inquiry())


def inquiry():
    numbers = []
    number_of_numbers = int(input("So how many numbers did ya want today bud?\n> "))
    print("Aight lay em out for me")
    for number in range(1, number_of_numbers + 1):

        number = str(input("> "))
        numbers.append(number)

    return numbers


def printing(numbers):
    print("Your chosen numbers were: \n{}".format(numbers))
    print("The first number is {:>3}".format(numbers[0]))
    print("The last number is {:>4}".format(numbers[-1]))
    print("The smol boi is {:>7}".format(min(numbers)))
    print("Le thicc boi is {:>7}".format(max(numbers)))
    print("The average is {:>10}".format(average(numbers)))


def average(numbers):
    counter = 0
    for i in numbers:
        numbers[counter] = int(numbers[counter])
        counter += 1
    number_average = float(sum(numbers) / len(numbers))
    return number_average


def username_inquiry():
    username = str(input("Please enter username: \n> "))
    return username


def username_verification():
    username = username_inquiry()
    verified_user = False
    while not verified_user:
        for i in usernames:
            if username in usernames:
                verified_user = True
            else:
                print("Access denied. Please enter registered username")
                username = username_inquiry()
        print("Access granted")


main()
