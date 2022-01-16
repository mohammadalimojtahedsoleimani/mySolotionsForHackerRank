if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

my_array = list(arr)
a = 0
b = []
k = max(my_array)
for i in my_array:
    if i < k:
        b.append(i)
print(max(b))
