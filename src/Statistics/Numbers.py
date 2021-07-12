import random


def numbers(data, data_size):
    random_value = random.choices(data, k=data_size)
    return random_value
