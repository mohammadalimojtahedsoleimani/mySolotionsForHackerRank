arr = [5, 2, 5, 4, 5, 3]
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0
lip = [0]*5
for i in arr:
    lip[i-1] += 1

k = max(lip)
sib = lip.index(k)
for i in lip:
    if i == k:
        print(sib)

