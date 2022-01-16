def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in range(1, n):
        for j in range(n - 1):
            if i > j:
                if (ar[i] + ar[j]) % k == 0:
                    counter += 1
    return counter
