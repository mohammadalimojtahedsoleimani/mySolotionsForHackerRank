import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    sire = []
    sirab = []
    conuts = 0
    counto = 0
    for i in apples:
        sire.append(a + i)
    for i in oranges:
        sirab.append(b + i)
    for i in sire:
        if i in range(s, t+1):
            conuts += 1
    for j in sirab:
        if j in range(s, t+1):
            counto += 1

    print(conuts)
    print(counto)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
