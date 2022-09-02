def angry(k, a):
    c = 0
    for i in a:
        if i <= 0:
            c += 1
    if k == c:
        return "YES"
    else:
        return "NO"


a = [-2, -1, 0, 1, 2]
k = 3
print(angry(k,a))
