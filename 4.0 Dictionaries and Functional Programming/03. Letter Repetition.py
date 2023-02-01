lst = [x for x in input()]
uniq = sorted(set(lst), key=lst.index )
[print(n ,'->', lst.count(n)) for n in uniq]


'''
input:
The quick brown fox jumps over the lazy dog
output:
T -> 1
h -> 2
e -> 3
  -> 8
q -> 1
u -> 2
...
'''