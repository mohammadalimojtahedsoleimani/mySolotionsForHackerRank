def breakingRecords(scores):
    check = scores[0]
    check_b = scores[0]
    counter_a = 0
    counter_b = 0
    for i in scores:
        if i > check:
            check = i
            counter_a += 1
        if i < check_b:
            check_b = i
            counter_b += 1

    print(counter_a, counter_b)


scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
breakingRecords(scores)
