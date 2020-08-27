"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint


def main():
    score = float(input("Enter score: "))
    print(score_check(score))
    random_score = randint(1, 100)
    # print(random_score) # check what the number is
    print(score_check(random_score))


def score_check(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


main()
