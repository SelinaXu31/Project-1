from Calculator.Subtraction import subtraction
from Calculator.Square import square
from Statistics.Mean import mean


def variance(data):
    varMean = mean(data)

    Diffs = []
    for Nums in data:
        everyDiff = subtraction(Nums, varMean)
        Diffs.append(everyDiff)

    listSquares = []
    for everyDiff in Diffs:
        everySquare = square(everyDiff)
        listSquares.append(everySquare)

    return mean(listSquares)
