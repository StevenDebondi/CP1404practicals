"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Gets the score from the user and prints the results"""
    score = float(input("Enter score: "))
    print(get_result(score))


def get_result(score):
    """Gets the result of the given score"""
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
