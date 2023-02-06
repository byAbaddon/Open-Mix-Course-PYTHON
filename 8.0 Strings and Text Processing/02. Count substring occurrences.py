text, st = [input().lower() for _ in range(2)]

count = 0
for i in range(len(text)):
    if text[i:i + len(st)] == st:
        count += 1

print(count)

'''
input:
aaaaaa
aa
output:
5
'''
