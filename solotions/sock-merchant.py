n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
js = ar
counter = 0
countersec = 0
ar.sort()
ar = list(dict.fromkeys(ar))
lip = []
for i in ar:
    lip.append(0)
for i in ar:
    for j in js:
        if i == j:
            jib = ar.index(i)
            lip[jib] += 1
for i in range(len(lip)):
    lip[i] //= 2

for i in lip:
    for j in range(i):
        counter += 1
        if counter >= 1:
            countersec += 1

print(countersec)
