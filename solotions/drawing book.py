def pageCount(n, p):
    counter = 0
    counter2 = 0
    temp = 0
    temp1 = 0
    for i in range(1, n + 1):
        if i == p:
            temp = counter
            break
        if i != p and i % 2 == 0 or i == 1:
            counter += 1

    for j in range(n, 0, -1):
        if j != p:
            if j % 2 == 0:
                counter2 += 1
            else:
                if j - 1 != p:
                    counter2 += 1
        else:
            temp1 = counter2
            break
    if temp >= temp1:
        return temp1
    else:
        return temp


n = 15603
p = 6957
print(pageCount(n, p))
