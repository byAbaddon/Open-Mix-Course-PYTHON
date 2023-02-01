loop = int(input())
obj = {}

while True:
    for _ in range(loop):
        key, val = input().split(' -> ')
        if key not in obj:
            obj[key] = []
        obj[key] += val.split(',')

    color_and_item =  input().split(' ')
    if len(color_and_item) == 3:
        color, dress_type = color_and_item[0], ' '.join(color_and_item[1:])
    else:
        color, dress_type = color_and_item

    for key, val in obj.items():
        duplicate = []
        print(key, 'clothes:')
        for v in val:
            if key == color and dress_type == v and dress_type != 'Swimming Shorts': # Fix BUG ?
                found = '(found!)'
            else:
                found = ''
            if v not in duplicate:
                print(f'* {v} - {val.count(v)} {found}')
                duplicate.append(v)
    break


'''
input:
4
Blue -> dress,jeans,hat
Gold -> dress,t-shirt,boxers
White -> briefs,tanktop
Blue -> gloves
Blue dress

output:
Blue clothes:
* dress - 1 (found!)
* jeans - 1
* hat - 1
* gloves - 1
Gold clothes:
* dress - 1
* t-shirt - 1
* boxers - 1
White clothes:
* briefs - 1
* tanktop - 1


'''