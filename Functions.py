import random

def winningNumbers():
    winningNumbers = (random.sample(range(1, 46), 6))
    winningNumbers.sort()
    return winningNumbers