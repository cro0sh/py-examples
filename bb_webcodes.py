def sum_numbers_or_phone_numbers(code):

    s = [code, ]
    count = 0
    
    for z in s:
        for zee in z:
            zee = zee.strip('-')
            if zee == ' ':
                next
            else:
                if zee == 0 or zee == '':
                    next
                else:
                
##                    print(type(zee))
                    zee = int(zee)
                    count += zee
##            print(zee)
    ##        add = z + (z+1)
    ##print(add)
    print(count)
    return count
##webcode_sum_best_buy('20972388')

sum_numbers_or_phone_numbers('250-571-9099')
