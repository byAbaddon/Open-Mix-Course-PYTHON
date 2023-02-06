lst = [x for x in iter(input, 'collapse')]

while lst:
    ste, fic = lst.pop(0), lst.pop(0)
    while fic:
        contains = ste.find(fic)
        ste = ste.replace(fic, '')
        if contains:
            fic = fic[1:-1]

    print(ste.strip()) if len(ste) > 0 else print("(void)")

'''
input:
astalavista baby
aaa
aaaa
aa
this will be funny rhight
this
collapse

output:
stlvist bby
(void)
will be funny rght
'''
