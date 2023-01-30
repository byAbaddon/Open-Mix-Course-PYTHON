result = [x for x in input().split() if int(x) > 0][::-1]
print(' '.join(result) if len(result) else 'empty')


'''
input:
7 -2 -10 1
output:
50 9 7 10
'''
