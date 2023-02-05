def distance():
    x1, y1 = map(int,input().split())
    x2, y2 = map(int,input().split())
    return f'{(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5):.3f}'

print(distance())


'''
input:
3 4
6 8
output:
5.000

'''