from re import findall

regex = r'(^\d+)([A-Za-z]+)([^A-Za-z]*)$'
lst = [x for x in iter(input, 'Over!')]

for i in range(0, len(lst),2):
        line = lst[i]
        number = int(lst[i + 1])
        try:
            matches = [x for x in findall(regex, line)[0]]
            if matches:
                word = matches.pop(1)
                if len(word) != number: continue
                matches[1] = ''.join([x for x in matches[1] if x.isdigit()])
                inx_lst= sum([list(map(int, ' '.join(x).split())) for x in matches if x.isdigit()], [])
                result = ''.join([word[i] if i < len(word) else ' ' for i in inx_lst])
                print(f'{word} == {result}')
        except:
            continue

'''
input:
1234test4321
4
0000oooo0000
4
Over!
output:

'''
