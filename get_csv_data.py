def get_meal_cols_to_dict(meal_number):
##def get_food_db():
    import csv
    count = 0
    food_database = []
    with open('/home/c/Desktop/py/food_spreadsheet_v3.csv') as file:
        file_csv = csv.DictReader(file)
    ##    something = next(file_csv)
    ##    print(file_csv)
    ##    for col in file_csv:
    ##        print(col)
        for row in file_csv:
            try:
                
    ##                    print(row[0])
                food_database.append(row['date'])
                food_database.append(row[meal_number])
    ##            food_database.append(row.keys())
    ##            food_database.append(row[' meal1'])
    ##            food_database.append(row[' meal2'])
    ##            food_database.append(row[' meal3'])
            except IndexError:
                count += 1               
                next
            
    print('food database is' , food_database)
##    return(food_database)
    print('count is ', count)
    ##print(list(food_database[1]))

    ##for z in food_database:
    ##    a = ''.join(z)
    ####    a = list(a)
    ##    print(a)

        
    new_lst = []

    s = ''
    for z in food_database:
    ##    print(z)
        for pos, zee in enumerate(z):
    ##        if zee == "'":
    ##            position = pos
    ##        else:
            new_lst.append(zee)
    ##print(new_lst)
    my_lst_str = ''.join(map(str, new_lst))
    ##print(type(my_lst_str))
    ##print('my_lst_str is ', my_lst_str)
    new = ''
    for z in my_lst_str:
        if z=="'":
            next
        else:
            new += z
    ##        print(new)

    positions = []

    for pos, z in enumerate(new):
        if z == "[" or z == "]":
            positions.append(pos)
    ##print(positions)
    ##print(new[8:57])
    ##print ('new is , ', new)
    good_lst = []
    ##word = ''
    for pos, z in enumerate(positions):
        if pos % 2 == 0:
            z = z + 1
    ##        print('pos is ', pos)
    ##        print('z is ', z)
    ##        print('new z (z += 1 ) is', new_z)

            good_lst.append(new[z:positions[pos+1]])
    ##    print('z is ', z)
    ##    print('z + 1 is ', z+1)
    ##    for s in new:
    ##    print(new[z+1:z])
    ##    print(z+1)
        
    ##    print(new)
    ##print(good_lst)
##    make_meal_dictionary(meal_number)
    print('good lst ', good_lst)
    itemsdr = {}
    d= {0: 'pizza', 1: 'chicken, rice, milk, milk, salad dressing, carrot',
    2: 'chicken, rice', 3: 'subway, chicken', 4: 'cheese, cheese, milk',
    5: 'chicken, potato'}

    d1= {0: 'oranges', 1: 'chicken, rice, milk, milk, salad dressing, carrot',
    }
##    itemsdr = {}
    for z, zee in enumerate(good_lst):
        itemsdr[z] = zee
    print('itemsdr inbetween', itemsdr)
##    for key in itemsdr.keys():
##    ##        for z in d.keys():
##        itemsdr[key] = meal_number
    print(itemsdr)
    return(itemsdr)
def something(d, meal):
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
        d[meal + a] = d.pop(items)
    print(d)
##app = chng()
fooddb = get_meal_cols_to_dict(meal_number = ' meal1')
something(d=fooddb, meal=' meal1 ')
##a = change_keys(d=food_database,meal=' meal0')
##d = change_keys(d1, ' meal1')
##get_meal_cols_to_dict(' meal0')

##    make_meal_dictionary('meal0')
    ##    word = new[z+
    ##    print(z)


    ##        if z == "]":
    ##            z.replace("]", ",")
            
    ##    

    ##            print(zee)
    ##        print(zee)
    ##        if zee == '[' or  zee == ']':
    ##            next
    ##        else:
    ##            a = ''.join(zee)
    ##            print(a)
    ##            new_lst.append(zee)
    ##        
    ##print(new_lst)
    ##    print(z)
