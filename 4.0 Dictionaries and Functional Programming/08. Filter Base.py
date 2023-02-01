obj = {}
input_order = {'Position': [], 'Age' : [], 'Salary': []}

while True:
    try:
        key, val = input().split(' -> ')
        if key not in obj:
            obj[key] = {}

        if  val.isalpha():
            obj[key].update({'Position' : val})
            input_order['Position'].append(key)
        else:
            if val.isdigit():
                obj[key].update({'Age': int(val)})
                input_order['Age'].append(key)
            else:
                obj[key].update({'Salary': float(val)})
                input_order['Salary'].append(key)
    except:
        option = input()
        [print(f'Name: {name}\n{option}: {obj[name][option]}\n{"=" * 20}') for name in input_order[option]]
        break


'''
input:
Isacc -> 34
Peter -> CEO
Isacc -> 4500.054321
George -> Cleaner
John -> Security
Nina -> Secretary
filter base
Position

output:
Name: Peter
Position: CEO
====================
Name: George
Position: Cleaner
====================
Name: John
Position: Security
====================
Name: Nina
Position: Secretary
====================
'''