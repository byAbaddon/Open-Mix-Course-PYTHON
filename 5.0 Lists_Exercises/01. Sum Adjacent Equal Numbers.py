lst = list(map(float, input().split()))

index = 0
while True:
    if index == len(lst) - 1:
        print([float(x) if str(x)[:1] == '0' else int(x) for x in lst])
        break

    if lst[index] == lst[index + 1]:
        lst[index] *= 2
        lst.pop(index + 1)
        index = 0
    else:
        index += 1

'''
input:
0.1 0.1 5 -5
output:
0.2
5
-5
'''
