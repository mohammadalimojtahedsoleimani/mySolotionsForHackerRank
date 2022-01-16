n = int(input())
res = []
grade = []
for i in range(n):
    name = input()
    score = float(input())
    res.append([name, score])
    grade.append(score)

grade = sorted(set(grade))
m = grade[1]
name = []
for i in res:
    if m == i[1]:
        name.append(i[0])
name.sort()
for i in name:
    print(i)

