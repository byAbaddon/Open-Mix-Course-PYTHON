result_obj = {}

for k, x in [x.split(' -> ') for x in iter(input, 'end')]:
    if x in result_obj:
        result_obj[k] = result_obj[x]
        continue
    if k not in result_obj and not x.isalpha():
        result_obj[k] = x
    else:
        if k in result_obj:
            result_obj[k] += (', '+ x)


[print(f'{x[0]} === {x[1]}') for x in result_obj.items()]


'''
input:
Donald -> 2, 2, 2
Isacc -> 1
George -> John
John -> Isacc
end
output:
Donald === 2, 2, 2
Isacc === 1
John === 1
'''