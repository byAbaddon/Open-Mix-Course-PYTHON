import math

lst = sorted([int(x) for x in input().split()],reverse=True)

for n in lst:
    try:
        sqrt = math.sqrt(n)
        if sqrt - int(sqrt) == 0:
            print(n, end=' ')
    except:
        ''



'''
-1 2 -5 100 121 81 49 36 25 24 169 -169
Input:
3 16 4 5 6 8 9
Output:
16 9 4

'''