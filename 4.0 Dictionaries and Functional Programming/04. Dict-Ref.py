obj = {}

while True:
    try:
        entry, val = input().split(' = ')
        if val.isnumeric():
            obj[entry] = int(val)
        else:
            if val in obj:
                obj[entry] = obj[val]
    except:
        [print(k, '===', v) for k, v in obj.items()]
        break

'''
input:
Vladi = 5
Ivo = Vladi
Vladi = Bok
Nakov = Bok
Bok = 7
Ivo = Bok
end

output:
Vladi === 5
Ivo === 7
Bok === 7
'''