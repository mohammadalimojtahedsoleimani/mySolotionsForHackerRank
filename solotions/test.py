import itertools

# lip = [3, 4, 5]
# sire = []
# for i in lip:
#     sire.append(4 + i)
#
# print(sire)
#
# check = "salam 12 13"
# x = check.split()
# lastchar = x[-1]
# lastchar = int(lastchar)
# print(x[-1], x[-2],type(lastchar))

# numbers = [ 1 , 2 , 3 , 4 ]
# result = itertools.product ( numbers , repeat = 4 )
# for item in result:
# 	print(item)
#
# import itertools
#
# A = [int(x) for x in input().split()]
# B = [int(y) for y in input().split()]
#
# print(*itertools.product(A, B))
lip = [1, 2, 3, 4, 5]
lip = map(str, lip)
print(type(lip[0]))
