from re import finditer

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
numbers = input()
results = finditer(pattern, numbers)
[print(result.group(0), end=' ') for result in results]

'''
input:
1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5
output:
1 -1 123 -123 123.456 -123.456
'''