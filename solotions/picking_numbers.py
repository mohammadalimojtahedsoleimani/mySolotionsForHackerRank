a = [4, 6, 5, 3, 3, 1]
maximum = 0
for i in a:
    c = a.count(i)
    d = a.count(i - 1)
    c = c + d
    if c > maximum:
        maximum = c

print(maximum)
