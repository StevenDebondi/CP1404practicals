"""
CP1404 Practical
Emails program that stores users emails and names in a dictionary
"""


def main():
    """Creates dictionary of emails with names"""
    emails_with_names = {}
    email = input("Email: ")
    while email != "":
        full_name = get_name_from_email(email)
        check = input(f"Is your name {full_name}? (Y/N)").upper()
        if check != "" and check != "Y":
            full_name = input("Name: ")
        emails_with_names[email] = full_name
        email = input("Email: ")
    for email, full_name in emails_with_names.items():
        print(f"{full_name} ({email})")


def get_name_from_email(email):
    """Gets the name from the given email"""
    name = email.split('@')[0]
    extras = name.split('.')
    full_name = " ".join(extras).title()
    return full_name


main()
