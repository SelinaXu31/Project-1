import random


class EmptyListError(Exception):
    """Raised when the input value is too big"""
    pass


def random_seed(seed=None, decimal=1, start=0, stop=100, step=1):
    if seed is not None:
        random.seed(seed)

    if decimal == 1:
        random_num = random.uniform(start, stop)
    else:
        random_num = random.randrange(start, stop, step)

    return random_num


def list_generator(seed=None, decimal=1, start=0, stop=100):
    random_list = []

    list_seed = seed
    random.seed(list_seed)

    for i in range(start, stop):
        if decimal == 1:
            random_num = random.uniform(0, 100)
        else:
            random_num = random.randrange(start, stop, 1)
        random_list.append(random_num)
    check_for_list(random_list)

    return random_list


# for seed and not seed
def n_items_no_seed(test_list, sample_size, seed=None):
    if seed is not None:
        random.seed(seed)

    number_of_choices = sample_size

    sample = random.choices(test_list, k=number_of_choices)
    return sample


def check_for_list(list_to_check):
    try:
        if len(list_to_check) > 0:
            return list
    except:
        if not list_to_check:
            raise EmptyListError
    else:
        print("List is empty.")
