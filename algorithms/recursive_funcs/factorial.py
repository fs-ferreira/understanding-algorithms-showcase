def calculateFactorial(num):
    if num == 1 or num == 0:
        return 1
    return num * calculateFactorial(num-1) 