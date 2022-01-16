def birthday(s, d, m):
    tp = (len(s) - m) + 1
    return len([i for i in range(tp) if sum(s[i:i+m])==d])


s = [2, 2, 1, 3, 2]
d = 4
m = 2
birthday(s, d, m)
