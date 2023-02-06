lst = [input() for x in range(int(input()))]

char = ''
max_len = 0
pyramid_list = []

for word in lst:
    for c in word:
        if max_len < word.count(c):
            max_len = word.count(c)
            char = c
    count = 0
    for c in word:
        if c == char:
            count += 1
        else:
            if count > 0:
                pyramid_list.append(count)
            count = 1
    pyramid_list.append(count)

[print(i * char) for i in range(1, max(pyramid_list) + 1, 2)]

'''
input:
3
abacd
bbbcd
bbbbb

output:
b
bbb
bbbbb
'''
