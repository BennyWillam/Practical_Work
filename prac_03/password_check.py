
MINIMUM_PASSWORD_LENGTH = 4
MAXIMUM_PASSWORD_LENGTH = 16
password = input("Please enter a password between {} and {}:  ".format(MINIMUM_PASSWORD_LENGTH, MAXIMUM_PASSWORD_LENGTH))

while not MINIMUM_PASSWORD_LENGTH <= len(password) <= MAXIMUM_PASSWORD_LENGTH:
    print(" Sorry, your password {} is not the correct length".format("*" * len(password)))
    password = input("Please enter a password: ")

print("Your password is: {}".format("*" * len(password)))
