##import csv
##
##food_database = []
##with open('/home/c/Desktop/py/food_spreadsheet_v3.csv') as file:
##    file_csv = csv.DictReader(file)
####    something = next(file_csv)
####    print(file_csv)
####    for col in file_csv:
####        print(col)
##    for row in file_csv:
##        try:
##            
####                    print(row[0])
##            food_database.append(row)
##        except IndexError:
##            next
##print(food_database)
d = {'2019-02-07 20:10:48': "['pizza']", '2019-02-08 21:12:35': "['chicken', 'rice', 'milk', 'milk', 'salad dressing', 'carrot']", '2019-02-09 20:40:10': "['chicken', 'rice']", '2019-02-11 10:34:56': "['subway', 'chicken']", '2019-02-11 18:38:08': "['cheese', 'cheese', 'milk']", '2019-02-12 09:49:45': '', '2019-02-12 15:19:42': '', '2019-02-12 17:57:39': "['chicken', 'potato']"}

for x, z, a in d.values():
    print(x,z,a)
