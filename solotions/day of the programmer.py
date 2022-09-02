year = int(input())
mm = 9
hh = 13
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    hh = 12
    print('{:02}.{:02}.{:4}'.format(hh, mm, year))
else:
    hh = 13
    print('{:02}.{:02}.{:4}'.format(hh, mm, year))
