"""
CP1404/CP5632 Practical
Data file -> lists program
"""


FILENAME = "subject_data.txt"


def main():
    get_data()
    print_data()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_data.append(parts)
    print(subject_data)
    input_file.close()
    return subject_data


def print_data():
    for i in get_data():
        print("{} is taught by {:^13} and has {:>3} students".format(i[0], i[1], i[2]))


main()
