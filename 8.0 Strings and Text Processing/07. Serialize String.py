obj = {}

for v, k in enumerate(input()):
    if not k in obj: obj[k] = []
    obj[k].append(v)

[print(f'{k}:{str(obj[k])[1:-1].replace(", ", "/")}') for k in obj.keys()]


'''
input:
abababa
output:
a:0/2/4/6
b:1/3/5
'''
