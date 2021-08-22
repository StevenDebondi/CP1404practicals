"""Password Checker"""

password = input("Password: ")
password_length = 6

while len(password) < password_length:
    print("Invalid Length")
    password = input("Password: ")
print("*" * len(password))  # Prints asterisks to match the amount of characters in the given password