k = 1
lip = [3, 10, 2, 9]
counter = 0
b = 12
sib = sum(lip) // 2
for i in lip:
    if i != lip[k]:
        counter += i

counter //= 2
rib = sib - counter
if counter == b:
    print("Bon Appetit")
else:
    print(rib)
