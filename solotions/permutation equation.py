a = [3, 2, 1, 2, 3]
c = []
for i in range(len(a)-1):
    for j in range((i + 1), len(a)):
        if a[i] == a[j]:
            d = j - 1
            c.append(d)

print(min(c))
