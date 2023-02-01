lst = [x for x in input().lower().split()]
obj = {}
for l in lst:
    if l not in obj:
        obj[l] = 0
    obj[l] += 1

print(', '.join([k for k,v  in obj.items() if v & 1]))

'''
input:
Java C# PHP PHP JAVA C java
output:
java c# c
'''