lst = list(map(int,input().split()))
uniq = sorted(list(set(lst)))
[print(f'{x} -> {lst.count(x)}') for x in uniq]

'''
input:
8 2 2 8 2 2 3 7
output:
2 -> 4
3 -> 1
7 -> 1
8 -> 2
'''
