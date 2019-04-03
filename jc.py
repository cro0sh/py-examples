years = []

for year in range (1990, 2019+1):
    years.append(year)
print(years)

from datetime import datetime

a = datetime(1990, 12, 25)
b = datetime(1991, 3, 9)

d = b - a
print(d.days)

diffs = []

for year in years:
    a = datetime(year, 12, 25)
    b = datetime(year + 1, 3, 9)
    d = b - a
    print('b is ', b, 'a is ', a, 'which means d is ', d)
    diffs.append(d.days)

print(diffs)
print(sum(diffs) / float(len(diffs)))
print(sum(diffs))
