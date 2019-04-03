d= {0: 'pizza', 1: 'chicken, rice, milk, milk, salad dressing, carrot',
    2: 'chicken, rice', 3: 'subway, chicken', 4: 'cheese, cheese, milk',
    5: 'chicken, potato'}
from time import gmtime, strftime, localtime

##        time = strftime("%Y-%m-%d %H:%M:%S", localtime())

##for z, k in d:
count=0
for key in d.keys():
    count += 1
print(count)
import random
random.randint(0,1500000)
for items in range(0,count):
    a = random.randint(0,1500000)
    a = str(a)
##    time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    d['meal0 ' + a] = d.pop(items)
print(d)
