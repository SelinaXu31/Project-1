from collections import Counter


def mode(data):
    mostfreq = Counter(data)
    get_mode = dict(mostfreq)
    r = [x for x, y in get_mode.items() if y == max(list(mostfreq.values()))]

    num_Values = len(data)
    num_Modes = len(r)

    if num_Modes == num_Values:
        return "No mode found"
    elif num_Modes != 1:
        return "Multiple modes found"
    else:
        return float(r[0])
