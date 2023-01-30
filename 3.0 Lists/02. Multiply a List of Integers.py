lst = [int(x) for x in input().split()]
mul = int(input())
print(*[mul * x for x in lst])

'''
input:
1 3 12 4
4
output:
4 12 48 16

'''
