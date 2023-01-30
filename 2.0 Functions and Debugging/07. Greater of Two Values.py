type_val, a, b = [input() for _ in range(3)]

if type_val == 'int':
    print(max(int(a), int(b)))
elif type_val == 'char':
    print(chr(max(ord(a), ord(b))))
else:
    print( max(str(a), str(b)))


'''
input:
int
2
16
output:
16

'''
