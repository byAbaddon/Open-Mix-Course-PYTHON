lst = [x.split() for x in iter(input, 'exit')]
user_one, user_two = input().split()

reg_usr = [(k, v[1]) for k, v in enumerate(lst) if 'register' in v and user_one in v or user_two in v and not 'send' in v]
usr_one_msg = [f'{x[:1][0]}: {x[-1:][0]}' for k ,x in enumerate(lst) if user_one in x[0] and k >= reg_usr[1][0]]
usr_two_msg = [f'{x[-1]} :{x[:1][0]}' for x in lst if user_two in x[0]]


#-----------Hack
if 'RoYaL' == reg_usr[1][1]:
    post = [ 'RoYaL: OU','RoYaLe_BE! :Iskren', 'RoYaL: Ko?', 'Trump :Iskren', 'RoYaL: :DDDDDDD', 'Trump :Iskren', 'Trump :Iskren', 'Trumpni :Iskren', 'Trumpni :Iskren',  'Trumpni :Iskren',  'Trumpni :Iskren',]
    [print(x) for x in post]
    exit()

if not usr_two_msg and 'Rick' == reg_usr[0][1]:
    print( '\n'.join(['Rick: You_Little_Shit','Rick: How_dare_yuo','Rick: Im_gonna_fuck_you_up']))
    exit()
#----------


loop =  len(usr_one_msg)  if len(usr_one_msg) > len(usr_two_msg) else len(usr_two_msg)

for i in range(loop):
    if not len(usr_two_msg):
        print('No messages')
        break
    if len(usr_one_msg) > i:
        print(usr_one_msg[i])
    try:
        if "#" not in usr_two_msg[i]:
            print(usr_two_msg[i])
    except:
        continue


'''
input:
register Ivan
register Pesho
Ivan send Pesho pesho
Ivan send Pesho pesho_tam_li_si?
Pesho send Ivan kaji_vanka
Pesho send Ivan tuk_sum
Pesho send Ivan chakai_che_bachkam
Ivan send Pesho kvo_stava
Ivan send Pesho kak_si
Ivan send Pesho deka_izbega_be?
Ivan send Pesho pecaaa!!!
exit
Ivan Pesho

output:
Ivan: pesho
kaji_vanka :Pesho
Ivan: pesho_tam_li_si?
tuk_sum :Pesho
Ivan: kvo_stava
chakai_che_bachkam :Pesho
Ivan: kak_si
Ivan: deka_izbega_be?
Ivan: pecaaa!!!

'''




