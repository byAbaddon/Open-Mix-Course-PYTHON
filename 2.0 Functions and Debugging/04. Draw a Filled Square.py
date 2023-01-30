def draw(n):
    print('-' * n * 2)
    for _ in range(n - 2):
        print('-',end='')
        [print('\\' + '/', end='') for i in range(n - 1)]
        print('-')
    print('-' * n * 2)


draw(int(input()))


'''
input:
4
output:
--------
-\/\/\/-
-\/\/\/-
--------

'''
