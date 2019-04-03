import csv
count = 0
food_database = []
food_names = []
food_dates = []
new_food_dates = []
def food_list_to_dict(meal):
    with open('/home/c/Desktop/py/food_spreadsheet_v3.csv') as file:
        file_csv = csv.DictReader(file)
    ##    something = next(file_csv)
    ##    print(file_csv)
    ##    for col in file_csv:
    ##        print(col)
        for row in file_csv:
            try:
                
    ##                    print(row[0])
                food_dates.append(row['date'])
                food_names.append(row[meal])
    ##            food_database.append(row.keys())
    ##            food_database.append(row[' meal1'])
    ##            food_database.append(row[' meal2'])
    ##            food_database.append(row[' meal3'])
            except IndexError:
                count += 1               
                next
    for item in food_dates:
        a = item.replace(item, item + meal)
##        print('****** a is ', a)
##        food_dates = []
        new_food_dates.append(a)
##            print('** new food dates **', food_dates)
    ##print(food_database[1])
    itemsdr = {}
    for z, k in zip(food_names, new_food_dates):
        itemsdr[k] = z
    return(itemsdr)
##            print('---- itemsdr -----', itemsdr)
##            print(itemsdr)
a = k = food_list_to_dict(' meal0')
b = k = food_list_to_dict(' meal1')
k = food_list_to_dict(' meal2')
print(a, b, k)
