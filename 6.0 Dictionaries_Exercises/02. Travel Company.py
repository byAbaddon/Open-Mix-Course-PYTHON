obj = {}  # [x.split(':') for x in iter(input, 'ready')]

while True:
    command = input()
    if command != 'ready':
        key, val = command.split(':')
        if not key in obj:
            obj[key] = dict([x.split('-') for x in val.split(',')])
        else:
            for token in val.split(','):
                transport, places = token.split('-')
                if transport not in obj[key]:
                    obj[key].update({transport: places})
                else:
                    obj[key][transport] = places
    else:
        break

while True:
    token = input()
    if token != 'travel time!':
         town, places = token.split()
         # print(obj)
         for k, v in obj.items():
             if town == k:
                 print(f'{town} -> ', end='')
                 all_places = sum([int(x[1]) for x in v.items()])
                 print(f"all {places} accommodated") if all_places >= int(places) \
                     else print(f"all except {abs(all_places - int(places))} accommodated")
    else:
        break


'''
input:
Athens:bus-40,airplane-300,train-150
Athens:minibus-8,airplane-350
Warsaw:bus-30,train-150,airplane-120
ready
Athens 400
Warsaw 500
travel time!

output:
Athens -> all 400 accommodated
Warsaw -> all except 200 accommodated
'''
