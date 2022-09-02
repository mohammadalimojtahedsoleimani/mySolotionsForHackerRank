def viralAdvertising(n):
    shared = 5
    day = 1
    liked = 2
    total = 2
    while day < n:
        shared = shared // 2 * 3
        liked = shared // 2
        total += liked
        day += 1

    return total


print(viralAdvertising(3))
