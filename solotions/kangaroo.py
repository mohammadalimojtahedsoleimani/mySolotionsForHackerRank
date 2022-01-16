def kangaroo(x1, v1, x2, v2):
    check = False
    for i in range(5):
        x1 += v1
        x2 += v2
        if x1 == x2:
            check = True
            break
        else:
            check = False

    if check:
        return "YES"
    else:
        return "NO"


x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

print(kangaroo(x1, v1, x2, v2))
