import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    s = 0
    b = 0
    arr.sort()
    s = arr.pop(0)
    b = arr.pop(-1)
    for i in arr:
        s += i
        b += i
    print(s, b)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
