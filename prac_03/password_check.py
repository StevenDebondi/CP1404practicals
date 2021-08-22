"""Password Checker"""


def main():
    """"""
    password = get_password()
    password_length = 6

    while len(password) < password_length:
        print("Invalid Length")
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))  # Prints asterisks to match the amount of characters in the given password


def get_password():
    """Gets the password from the user"""
    password = input("Password: ")
    return password


main()
