from Statistics.Numbers import numbers
from collections import counter


def mode(data, data_size):
    list_numbers = numbers(data, data_size)
    length = len(list_numbers)
    count = counter(list_numbers)
    find_mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(find_mode) == length:
        get_mode = "No mode found"
    else:
        get_mode = "Mode is / are: " + ', '.join(map(str, find_mode))
    return get_mode
