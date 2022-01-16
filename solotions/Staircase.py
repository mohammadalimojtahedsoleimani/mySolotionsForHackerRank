n = int(input())
rap = n
for i in range(1, n + 1):
    if rap > 1:
        rap -= 1
        print(" " * rap, "#" * i)
    else:
        print("#"*i)
