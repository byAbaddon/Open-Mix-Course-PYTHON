lst = list(map(float, input().split()))
uniq = sorted(set(lst))
lst = list(map(str, lst))
[print(n ,'->', lst.count(str(n)), 'times') for n in uniq]

'''
input:
8 2.5 2.5 8 2.5
output:
2.5 -> 3 times
8 -> 2 times

'''