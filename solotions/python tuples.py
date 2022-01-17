
# just for solve the error
def raw_input():
    pass


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    integer_list = map(int, integer_list)
    t = tuple(integer_list)
    print(hash(t))
