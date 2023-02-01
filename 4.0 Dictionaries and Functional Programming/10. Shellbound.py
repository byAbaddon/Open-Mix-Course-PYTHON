obj = {}

while True:
    try:
        key, val = input().split()
        if key not in obj:
            obj[key] = []
        if val not in obj[key]:
            obj[key].append(val)
    except:
        for k, v in obj.items():
            print(f'{k} -> {", ".join(v)} ({sum(map(int,obj[k])) - sum(map(int,obj[k])) // len(obj[k])})')
        break


'''
input:
Sofia 50
Sofia 20
Sofia 30
Varna 10
Varna 20
Aggregate

output:

'''