"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter your score: "))
    print(result(score))

    score = random.randint(0, 100)
    print("Random score: {}".format(score))
    print(result(score))


def result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        score < 50
        return "Bad"


main()
