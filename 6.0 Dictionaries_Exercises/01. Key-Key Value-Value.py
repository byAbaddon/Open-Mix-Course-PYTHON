k, v, n = [input() for _ in range(3)]
lst = [input().split(' => ') for _ in range(int(n))]

for key, val in lst:
    if k in key:
        print(f'{key}:')
        [print(f"-{x}") for x in val.split(";") if v in x]

'''
input:

bug
X
3
invalidkey => testval;x;y
debug => XUL;ccx;XC
buggy => testX;testY;XtestZ

output:
debug:
-XUL
-XC
buggy:
-testX
-XtestZ
'''
