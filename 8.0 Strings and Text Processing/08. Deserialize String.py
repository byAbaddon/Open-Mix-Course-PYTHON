lst = [x for x in iter(input, 'end')]
result = [x for x in range(1, 150)]

for token in lst:
    char, index = token.split(':')
    index = list(map(int, index.split('/')))
    for i in index:
        result[i] = char

[print(x, end='') for x in result if not str(x).isdigit()]

'''
input:
a:0/2/4/6
b:1/3/5
end

output:
abababa

'''
