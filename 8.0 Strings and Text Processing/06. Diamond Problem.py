import re

lst = [list(filter(lambda x: x.isdigit(), x)) for x in re.findall('<(.*?)>', input())]
if lst:
    [print(f'Found {sum(map(int, x))} carat diamond') for x in lst]
else:
    print('Better luck next time')

'''
input:
empty<2big32diamond>useless<1another02Diamond>
output:
Found 7 carat diamond
Found 3 carat diamond
'''
