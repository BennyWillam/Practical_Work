"""
Program designed for a primary school teacher to help kids learn number sequences
"""


value_x = int(input("Please enter a start number: "))
value_y = int(input("Please enter a finish number: "))

question = str(input("What would you like to know? \n(O)dd numbers? \n(E)ven numbers? \n(S)quares? \n(Q)uit \n"))
while question != str('Q'):
    if question == str('O'):
        print("The odd values between", value_x, "and", value_y, "are: ", end=' ')
        if value_x % 2 == 0:
            for i in range(value_x + 1, value_y, 2):
                print(i, end=', ')
            print()
        else:
            for i in range(value_x, value_y, 2):
                print(i, end=', ')
            print()
    elif question == str('E'):
        print("The even values between", value_x, "and", value_y, "are: ", end=' ')
        if value_x % 2 != 0:
            for j in range(value_x + 1, value_y, 2):
                print(j, end=', ')
            print()
        else:
            for j in range(value_x, value_y, 2):
                print(j, end=', ')
            print()
    elif question == str('S'):
        print("The squares between", value_x, "and", value_y, "are: ", end=' ')
        for k in range(value_x, value_y):
            print(k**2, end=', ')
    else:
        print("Please select a valid option.")

    question_2 = str(input("Would you like different numbers? \n(Y)es or (N)o: "))
    if question_2 == str('Y'):
        value_x = int(input("Please enter a start number: "))
        value_y = int(input("Please enter a finish number: "))
        question = str(input("What would you like to know? \n(O)dd numbers? \n(E)ven numbers? \n(S)quares? \n(Q)uit \n"))
    elif question_2 == str('N'):
        question = str(input("What would you like to know? \n(O)dd numbers? \n(E)ven numbers? \n(S)quares? \n(Q)uit \n"))
    else:
        print("Please select a valid option")
print("Hope you learned something today!")
