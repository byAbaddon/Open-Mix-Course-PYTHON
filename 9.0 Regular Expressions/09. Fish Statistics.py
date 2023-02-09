import re

regex = r"((>*)<(\(+)(['|x|-])>)"
fishes = input()
fish_count = 1

matches = re.findall(regex, fishes)

if not matches:
    print('No fish found.')
    exit()

size = body = status = count = ''

for match in matches:
    count = match[0]
    fish_size = len(match[1])
    fish_body = len(match[2])
    fish_status = match[3].lower()

    if fish_size > 5:
        size =  f"Long ({fish_size * 2} cm)"
    elif 1 < fish_size <= 5:
        size = f"Medium ({fish_size * 2} cm)"
    elif fish_size == 1:
        size = f"Short ({fish_size * 2} cm)"
    else:
        size = "None"

    if fish_body > 10:
        body = f"Long ({fish_body * 2} cm)"
    elif 5 < fish_body <= 10:
        body = f"Medium ({fish_body * 2} cm)"
    else:
        body = f"Short ({fish_body * 2} cm)"

    if fish_status == "'":
        status =  "Awake"
    elif fish_status == "-":
        status =  "Asleep"
    elif fish_status == "x":
        status = "Dead"


    print(f"Fish {fish_count}: {count}")
    print(f"  Tail type: {size}")
    print(f"  Body type: {body}")
    print(f"  Status: {status}")
    fish_count += 1

'''
input:

output:
'''
