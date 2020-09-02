
def main():
    emails = {}
    user_email = input("Email: ")
    while user_email != "":
        user_name = name_from_email(user_email)
        is_name = input("Is your name {}? (Y/n)".format(user_name))
        if is_name.upper() != "Y":
            user_name = input("Name: ")
        emails[user_email] = user_name
        user_email = input("Email: ")
    for user_email, user_name in emails.items():
        print("{} ({})".format(user_name, user_email))


def name_from_email(new_email):
    name_split = new_email.split("@")[0]
    first_last = name_split.split(".")
    name = " ".join(first_last).title()
    return name


main()
