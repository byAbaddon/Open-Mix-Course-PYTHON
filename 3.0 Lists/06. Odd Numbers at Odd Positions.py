[print(f'Index {i} -> {x}') if i & 1 and int(x) & 1 else None for i, x in enumerate([x for x in input().split()])]

'''
input:
2 3 5 2 7 9 -1 -7
output:
Index 1 -> 3
Index 5 -> 9
Index 7 -> -7

'''
