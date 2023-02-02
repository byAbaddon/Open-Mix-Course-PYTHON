obj = {}

for l in [x for x in iter(input, 'drop the media')]:
    command, key = l.split(None, 1)
    if command == 'post' and key not in obj:
        obj[key] = {'like': 0, 'dislike': 0, 'comment': []}
    elif command == 'comment':
        key, name, comment = key.split(None, 2)
        obj[key][command].append((name, comment))
    else:
        obj[key][command] += 1

for k, v in obj.items():
    print(f'Post: {k} | Likes: {v["like"]} | Dislikes: {v["dislike"]}\nComments:')
    [print(f'*  {x[0]}: {x[1]}') for x in v["comment"]]
    if not v['comment']: print('None')

'''
input:
post FirstPost
like FirstPost
like FirstPost
dislike FirstPost
post SecondPost
comment FirstPost Isacc Cool
comment SecondPost Isacc Lol
like SecondPost
drop the media

output:
Post: FirstPost | Likes: 2 | Dislikes: 1
Comments:
*  Isacc: Cool
Post: SecondPost | Likes: 1 | Dislikes: 0
Comments:
*  Isacc: Lol

'''
