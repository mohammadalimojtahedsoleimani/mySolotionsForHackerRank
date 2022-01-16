n = int(input())


def compute(n):
    mainlist = []
    for i in range(n):
        check = input()
        if "append" in check:
            x = check.split()
            last_char = x[-1]
            mainlist.append(int(last_char))
        if "print" in check:
            print(mainlist)
        if "remove" in check:
            last_char = check[-1]
            last_char = int(last_char)
            mainlist.remove(last_char)
        if "sort" in check:
            mainlist.sort()
        if "pop" in check:
            mainlist.pop()
        if "reverse" in check:
            mainlist.reverse()
        if "insert" in check:
            x = check.split()
            last_char = x[-1]
            second_char = x[-2]
            mainlist.insert(int(second_char), int(last_char))


compute(n)
