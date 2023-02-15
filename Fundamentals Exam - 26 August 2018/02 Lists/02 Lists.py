for l in [list(map(int, x.split())) for x in iter(input, 'stop playing')]:
    if len(l) == len(set(l)):
        result = [x if x & 1 else x + 2 for x in l]
        print(f'Unique list: {",".join(map(str, sorted(result)))}\nOutput: {sum(result) / len(result):.2f}')
    else:
        result = [x + 3 if x & 1 else x for x in l]
        print(f'Non-unique list: {":".join(map(str,sorted(result)))}\nOutput: {sum(result) / len(result):.2f}')

'''
input:
1      1 1
stop playing

output:
Non-unique list: 4:4:4
Output: 4.00

'''
