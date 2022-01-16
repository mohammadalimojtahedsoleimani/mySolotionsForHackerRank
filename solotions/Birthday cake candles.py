import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    maxi = 0
    counter = 0
    for i in candles:
        if i > maxi:
            maxi = i
    for i in candles:
        if maxi == i:
            counter += 1

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
