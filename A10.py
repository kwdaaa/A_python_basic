import random


def dice():
    number = [1, 2, 3, 4, 5, 6]
    result = random.choice(number)
    return result


print(dice())
