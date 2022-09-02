

s = "beabeefeab"
a = ''
for i in s:
    b = a
    a = i
    if b == i:
        s.replace(i,"")

print(s)
