from random import randint

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

picks_amount = int(input("How many quick picks? "))
for o in range(picks_amount):
    picks_number = []
    for i in range(NUMBERS_PER_LINE):
        number = randint(MINIMUM, MAXIMUM)
        while number in picks_number:
            number = randint(MINIMUM, MAXIMUM)
        picks_number.append(number)
    picks_number.sort()
    print(" ".join("{:2}".format(number) for number in picks_number))
