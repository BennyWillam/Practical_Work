name = str(input("Hello! Whats your name? "))
choice = str(input("(H)ello \n(G)oodbye \n(Q)uit \n"))

while choice != str('Q'):
    if choice == str('H'):
        print("Hello", name, end=' \n')
    elif choice == str('G'):
        print("Goodbye", name, end=' \n',)
    else:
        print("Sorry, that's not an answer.")
    choice = str(input("(H)ello \n(G)oodbye \n(Q)uit \n"))
print("Thank you. Have a nice day!")
