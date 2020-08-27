MAX_LENGTH = 12
MIN_LENGTH = 3

password = input("What is your password? ")
while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
    print("Invalid password")
    password = input("What is your password? ")
star_numb = len(password)
print(star_numb * "*")