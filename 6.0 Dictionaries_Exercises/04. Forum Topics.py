obj = {}

while True:
    try:
        key, val = input().split(' -> ')
        if key not in obj:
            obj[key] = val
        else:
            obj[key] += (', ' + val)
    except:
        uniq_obj = {x[0]: sorted(set(x[1].split(', ')), key=x[1].index) for x in obj.items()}
        filters = input().split(', ')
        for k, v in uniq_obj.items():
            if len(v) == len(set(v + filters)):
                print(f'{k} | #{" #".join([str(x) + "," for x in v]).rstrip(",")}')
        break

'''
input:
HelloWorld -> hello, forum, topic
HelpWithHomework -> homework, forum, topic
filter
forum, topic

output:
HelloWorld | #hello, #forum, #topic
HelpWithHomework | #homework, #forum, #topic
'''
