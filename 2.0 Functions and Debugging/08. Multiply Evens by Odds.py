val = input()
if val[0] == '-': val = val[1:]
odd_sum = sum([int(x)  for x in val if int(x) & 1])
even_sum = sum([int(x) for x in val if not  int(x) & 1])
print(odd_sum * even_sum)



'''
input:
-12345
output:
54
'''