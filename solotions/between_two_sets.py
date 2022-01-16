def getTotalX(a, b):
    n = len(a)
    m = len(b)
    count = 0
    for i in range(1, 101):
        ok = True
        for j in range(n):
            if i % a[j] != 0 and ok:
                ok = False
        if ok:
            for j in range(m):
                if b[j] % i != 0:
                    ok = False
        if ok:
            count += 1
    return count


a = [2, 4]
b = [16, 32, 96]
print(getTotalX(a,b))
