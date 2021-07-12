import Statistics.Numbers import numbers

class median():
    n = len(numbers)
    numbers.sort()

    if n % 2 == 0:
        median1 = numbers[n // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[n // 2]
