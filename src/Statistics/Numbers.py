import random


def numbers(random_list):
    random_list = []
    for i in range(0, 10):
        random_num = random.randint(1, 100)
    random_list.append(random_num)
    return random_list

