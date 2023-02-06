txt = input()
lst = [list(map(lambda x: (int(x) if x.isdigit() else x), x.split())) for x in iter(input, 'end')]

for token in lst:
    if len(token) == 2:
        com, n = token
        if com == 'Left':
            for _ in range(n):
                txt = txt[1:] + txt[:1]
        else:  # right
            for _ in range(n):
                txt = txt[-1:] + txt[:-1]

    else:
        com, i1, i2 = token
        if com == 'Delete':
            txt = txt[:i1] + txt[i2 + 1:]
        else:  # insert
            txt = txt[:i1] + i2 + txt[i1:]
print(txt)

'''
input:
The Lone Ranger
Delete 0 7
Insert 0 Power
Insert 12 s
end
outupt:

'''
