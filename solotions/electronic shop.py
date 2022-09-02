sib = [10, 2, 3]
key = [3, 1]
usb = [5, 2, 8]
suber = []
container = 0
for i in key:
    for j in usb:
        suber.append(i + j)

suber.sort()
for i in sib:
    for j in suber:
        if i >= j >= container:
            container = j

# if container == 0:
#     return -1
print(container)