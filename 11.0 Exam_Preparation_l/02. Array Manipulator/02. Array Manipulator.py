lst = [int(x) for x in input().split()]

while True:
    try:
        command, token = input().split(None, 1)
        if command == 'exchange':
            token = int(token)
            if token > len(lst) or token <= 0:
                print('Invalid index')
            else:
                lst = lst[token + 1:] + lst[:token + 1]
        elif command in ['max', 'min']:
            try:
                if token == 'odd':
                    el = (eval(f'{command}' + f'([x for x in lst if x & 1])'))
                else:
                    el = (eval(f'{command}' + '([x for x in lst if not x & 1])'))
                inx = [x[0] for x in enumerate(lst) if x[1] == el][-1]
                print(inx)
            except:
                print('No matches')
        else:
            if command in ['first', 'last']:
                try:
                    n, o_e = token.split()
                    if int(n) > len(lst):
                        print('Invalid count')
                        continue
                    odd_lst = [x for x in lst if x & 1]
                    even_lst = [x for x in lst if not x & 1]
                    if command == 'first':
                        print(eval(f'{o_e}' + '_lst')[:int(n)])
                    if command == 'last':
                        print(eval(f'{o_e}' + '_lst')[-int(n):])
                except:
                    print('[]')
    except:
        print(lst)
        break



'''
input:
1 3 5 7 9
exchange 1
max odd
min even
first 2 odd
last 2 even
exchange 3
end

output:
2
No matches
[5, 7]
[]
[3, 5, 7, 9, 1]
'''
