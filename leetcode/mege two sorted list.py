
# it isn't correct
def merging(list1, list2):
    c = []
    if len(list1) == 0 and len(list2) == 0:
        return c
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    for i in range(0, len(list1)):
        c.append(list1[i])
        c.append(list2[i])

    return c


list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(merging(list1, list2))
