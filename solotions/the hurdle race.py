import numpy as np

k = 4
a = [1, 6, 3, 5, 2]
maximum = 0
for i in a:
    if i > maximum:
        maximum = i
if maximum > k:
    print(maximum - k)
else:
    print(0)
