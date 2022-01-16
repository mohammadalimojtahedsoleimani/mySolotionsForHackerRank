if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

counter = 0
rid = 0
for x in student_marks:
    if x == query_name:
        for i in student_marks[x]:
            counter += i
    rid = counter // 3

format_float = "{:.2f}".format(rid)
print(format_float)
