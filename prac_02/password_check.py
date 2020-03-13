"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
CHARACTERS = "abcdefghijklmnopqrstuvwyz"
CHARACTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMERALS = "1234567890"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")

    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    global password

    # TODO: if length is wrong, return False
    length_password_valid = False
    while not length_password_valid:
        if len(password) < 5 or len(password) > 15:
            print("Invalid length. Please enter a password between {} and {} characters long".format(MIN_LENGTH, MAX_LENGTH))
            password = input("> ")
        else:
            length_password_valid = True


        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
            # TODO: count each kind of character (use str methods like isdigit)
            pass

        # TODO: if any of the 'normal' counts are zero, return False

        # TODO: if special characters are required, then check the count of those
        # and return False if it's zero

        # if we get here (without returning False), then the password must be valid
        return True


main()