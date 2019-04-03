
meal0 = {'2019-02-07 20:10:48 meal0': "['pizza']", '2019-02-08 21:12:35 meal0': "['chicken', 'rice', 'milk', 'milk', 'salad dressing', 'carrot']", '2019-02-09 20:40:10 meal0': "['chicken', 'rice']", '2019-02-11 10:34:56 meal0': "['subway', 'chicken']", '2019-02-11 18:38:08 meal0': "['cheese', 'cheese', 'milk']", '2019-02-12 09:49:45 meal0': '', '2019-02-12 15:19:42 meal0': '', '2019-02-12 17:57:39 meal0': "['chicken', 'potato']", '2019-02-13 18:12:06 meal0': "['chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'shreddies', 'milk']"}
meal1= {'2019-02-07 20:10:48 meal0': "['pizza']", '2019-02-08 21:12:35 meal0': "['chicken', 'rice', 'milk', 'milk', 'salad dressing', 'carrot']", '2019-02-09 20:40:10 meal0': "['chicken', 'rice']", '2019-02-11 10:34:56 meal0': "['subway', 'chicken']", '2019-02-11 18:38:08 meal0': "['cheese', 'cheese', 'milk']", '2019-02-12 09:49:45 meal0': '', '2019-02-12 15:19:42 meal0': '', '2019-02-12 17:57:39 meal0': "['chicken', 'potato']", '2019-02-13 18:12:06 meal0': "['chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'chicken', 'shreddies', 'milk']", '2019-02-07 20:10:48 meal1': '', '2019-02-08 21:12:35 meal1': "['chicken', 'rice', 'salad', 'salad dressing']", '2019-02-09 20:40:10 meal1': '[\'milk\', \'milk\', \'milk\', \'milk\', "\'meat lasagna’", \'oranges\', \'oranges\']', '2019-02-11 10:34:56 meal1': "['chicken', 'rice', 'cheese']", '2019-02-11 18:38:08 meal1': "['subway']", '2019-02-12 09:49:45 meal1': '', '2019-02-12 15:19:42 meal1': '', '2019-02-12 17:57:39 meal1': "['chicken', 'rice']", '2019-02-13 18:12:06 meal1': ''}
meal2= 



def merge_dicts(*dict_args):
           
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

print(merge_dicts(meal0,meal1,meal2))
