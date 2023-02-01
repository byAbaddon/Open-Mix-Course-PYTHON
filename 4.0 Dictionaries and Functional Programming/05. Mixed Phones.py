obj = {}

while True:
    try:
        key, val = input().split(' : ')
        if val.isnumeric():
            obj[key] = val
        else:
            obj[val] = key
    except:
        sort_lst = sorted(obj.items(), key= lambda x: x[0])
        [print(k,'->' ,v) for k, v in sort_lst]
        break

'''
input:
Ivan : 13213456
GeorgeThe2nd : 131313
Johnny : 5556322312
Donald : 32

output:
Donald -> 3212
GeorgeThe2nd -> 131313
Ivan -> 13213456
Johnny -> 5556322312

'''