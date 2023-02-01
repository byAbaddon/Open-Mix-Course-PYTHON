obj = {}

while True:
    try:
        _, key, val = input().split()
        if key not in obj:
            obj[key] = 0
        obj[key] += int(val)
    except:
        break

while True:
    try:
        _, key, val = input().split()
        if key in obj:
            if obj[key] <= 0:
                print(key, 'out of stock')
            obj[key] -= int(val)
        else:
            print(key, 'doesn\'t exist')
    except:
        [print(k, '->', v) for k, v in obj.items() if v > 0]
        break

'''
input:
stock Boca_Cola 10
stock Boca_Cola 10
stock Kay's 3
stock Kay's 2
shopping time
buy Boca_Cola 5
buy Kay's 5
exam time

output:
Boca_Cola -> 15

'''
