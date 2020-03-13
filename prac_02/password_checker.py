"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
import string

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    prompt = "Please enter a valid password. \nYour password must be between {} and {} characters, and must contain:"
    print(prompt.format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(is_valid_password.password),
                                                           is_valid_password.password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    password_length_valid = False
    while not password_length_valid:
        if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
            print("Invalid length. Please enter a password between {} and {} characters long".format(MIN_LENGTH,
                                                                                                     MAX_LENGTH))
            password = input("> ")
        else:
            password_length_valid = True

    password_char_valid = False
    count_lower = 0
    count_lowercase = 0
    count_upper = 0
    count_uppercase = 0
    count_digit = 0
    count_digits = 0
    count_special = 0
    count_non_alphanumeric = 0

    while not password_char_valid:
        for char in password:
            # TODO: count each kind of character (use str methods like isdigit)
            if char.islower():
                count_lowercase = count_lower + 1
            if char.isupper():
                count_uppercase = count_upper + 1
            if char.isdigit():
                count_digits = count_digit + 1
            if SPECIAL_CHARS_REQUIRED:
                if not char.isalpha() and char.isdigit():
                    count_non_alphanumeric = count_special + 1

        if count_lowercase > 0:
            if count_uppercase != 0:
                if count_digits != 0:
                    if SPECIAL_CHARS_REQUIRED:
                        if count_non_alphanumeric != 0:
                            password_char_valid = True
                        else:
                            print("Invalid combination of characters. Please input: ")
                            print("\t1 or more lowercase characters")
                            print("\t1 or more uppercase characters")
                            print("\t1 or more numbers")
                            if SPECIAL_CHARS_REQUIRED:
                                print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
                            password = input("> ")
                    else:
                        password_char_valid = True
                else:
                    print("Invalid combination of characters. Please input: ")
                    print("\t1 or more lowercase characters")
                    print("\t1 or more uppercase characters")
                    print("\t1 or more numbers")
                    if SPECIAL_CHARS_REQUIRED:
                        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
                    password = input("> ")
            else:
                print("Invalid combination of characters. Please input: ")
                print("\t1 or more lowercase characters")
                print("\t1 or more uppercase characters")
                print("\t1 or more numbers")
                if SPECIAL_CHARS_REQUIRED:
                    print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
                password = input("> ")
        else:
            print("Invalid combination of characters. Please input: ")
            print("\t1 or more lowercase characters")
            print("\t1 or more uppercase characters")
            print("\t1 or more numbers")
            if SPECIAL_CHARS_REQUIRED:
                print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
            password = input("> ")

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    is_valid_password.password = password
    if password_length_valid and password_char_valid:
        return True


main()
