MAX_LENGTH = 12
MIN_LENGTH = 3


def main():
    password = get_password()
    turn_asterisks(password)


def turn_asterisks(password):
    star_number = len(password)
    print(star_number * "*")


def get_password():
    password = input("What is your password? ")
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("What is your password? ")
    return password


main()
