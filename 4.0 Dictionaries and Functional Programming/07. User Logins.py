obj = {}
failed_login_count = 0

while True:
    try:
        key, val = input().split(' -> ')
        obj[key] = val
    except:
        break

while True:
    try:
        key, val = input().split(' -> ')
        if key in obj:
            if obj[key] == val:
                print(f'{key}: logged in successfully')
                continue
        print(f'{key}: login failed')
        failed_login_count += 1
    except:
        print('unsuccessful login attempts:', failed_login_count)
        break

'''
input:
ivan_ivanov -> java123
pesh0 -> qwerty
stamat4e -> 111111
princess_penka -> MyPrince
login
pesh0 -> qwertt
ivan_ivanov -> java123
stamat4e -> 111112
princess_penka -> MyPrince
end

output:
pesh0: login failed
ivan_ivanov: logged in successfully
stamat4e: login failed
princess_penka: logged in successfully
unsuccessful login attempts: 2
'''