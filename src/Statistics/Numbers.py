import random


random_without_seed_int = random.randint(1, 100) #int
random_without_seed_float = random.uniform(1.0, 100.0) #float

random.seed(20)
random_with_seed = random.randint(1, 100) #int
random_with_seed_float = random.uniform(1, 100) #float


def random_numbers(n, l=0, h=100):
    n = random.randint(1, 100)
    random_list = []
    for i in range(0, n):
        random_list.append(random.seed(l, h))
    return random_list

