def variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    r = sum((x - mean) ** 2 for x in data) / (n - ddof)
    return r