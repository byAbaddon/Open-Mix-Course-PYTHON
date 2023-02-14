for l in [list(map(int, x.split())) for x in iter(input, 'stop playing')]:
    if len(l) == len(set(l)):
        result = [x if x & 1 else x + 2 for x in l]
        print(f'Unique list: {",".join(map(str, sorted(result)))}\nOutput: {sum(result) / len(result):.2f}')
    else:
        result = [x + 3 if x & 1 else x for x in l]
        print(f'Non-unique list: {":".join(map(str,sorted(result)))}\nOutput: {sum(result) / len(result):.2f}')



'''
input:
1 2  3   4 5 6
1 1 2   2 1 4 7 7 8 8 
 5 5 5 5  
stop playing

output:
Unique list: 1,3,4,5,6,8
Output: 4.50
Non-unique list: 2:2:4:4:4:4:8:8:10:10
Output: 5.60
Non-unique list: 8:8:8:8
Output: 8.00

'''
