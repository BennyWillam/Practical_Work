"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Can't divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("{:.4f}".format(fraction))
print("Finished.")

# Value errors occur when a float value is entered, as the code is expecting integers
# Zero division errors occurred when 0 was entered as the denominator.
# This is to prevent a system crash as it is not possible to divide by 0
# A while loop could be implemented to prevent any zero value being entered as the denominator
