import csv
count = 8
with open('/home/c/Desktop/py/food_spreadsheet_v2.csv', newline='') as f:
##    row = csv.reader(f, delimiter='\t')
    row = csv.reader(f, delimiter='\t')
##    next(row, None)
##    next(row, None)
##    next(row, None)
##    next(row, None)
##    next(row, None)
##    next(row, None)
##    next(row, None)
##    next(row, None)
    for z in range(0, count):
##        print(z)
        next(row, None)
        
    for line in row:
        count += 1
        print(line)
##print(count)
##count=8
####count = 0
##with open('/home/c/Desktop/py/food_spreadsheet_v2.csv') as f:
##    reader = csv.reader(f, delimiter='\t')
##
##    [next(reader, None) for item in range(7)]
##
##    for row in reader:
##        print(row)

    
##    for line in row:
####        count += 1
##        print(line)

##with open('/home/c/Desktop/py/food_spreadsheet_v2.csv') as f:
##    file_csv = csv.DictReader(f)
##    for line in file_csv:
##        print(line)
##    writer = csv.writer(f)
##    
####    h = next(writerz)
##    for row in file_csv:
##        print(row)
##    for row in f:
##        print(row)
