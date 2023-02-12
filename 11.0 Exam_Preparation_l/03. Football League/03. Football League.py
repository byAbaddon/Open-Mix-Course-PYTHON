from re import findall, escape    #todo: WTF Fucking Judge

lst = [x for x in iter(input, 'final')]
key = escape(lst.pop(0))
regex = rf'{key}([\w]+){key}|(\d+:\d+)'

obj = {}

for line in lst:
    try:
        a_tim, b_tim, res = [x[0][::-1].upper() if x[0] else x[1] for x in findall(regex, line)]
    except:
        continue
    for i in range(2):
        a_r, b_r = map(int, res.split(':'))
        tim = a_tim if i == 0 else b_tim
        goals = a_r if i == 0 else b_r
        if i == 0:
            pts = 3 if a_r > b_r else 1 if a_r == b_r else 0
        else:
            pts = 3 if a_r < b_r else 1 if a_r == b_r else 0

        obj.setdefault(tim, {'points': 0, 'goals': 0})
        obj[tim]['points'] += pts
        obj[tim]['goals'] += goals

sort_res_lst = sorted(obj.items(), key=lambda x: (-x[1]['points'], x[0]) )
sort_goals_lst = sorted(obj.items(), key=lambda x: (-x[1]['goals'], x[0]))[:3]

print('League standings:')
[print(f'{i + 1}. {x[0]} {x[1]["points"]}') for i, x in enumerate(sort_res_lst)]
print('Top 3 scored goals:')
[print(f'- {x[0]} -> {x[1]["goals"]}') for x in sort_goals_lst]


'''
input:
??
??ecnarF?? ??kramneD?? 0:0
..??airagluB??32 ??dnalgnE??gf 3:2
Fg??NIAPS?? fgdrt%#$??YNAMREG??gtr 3:4
??eCnArF?? >>??yLATi??<< 2:2
final

output:
League standings:
1. BULGARIA 3
2. GERMANY 3
3. FRANCE 2
4. DENMARK 1
5. ITALY 1
6. ENGLAND 0
7. SPAIN 0
Top 3 scored goals:
- GERMANY -> 4
- BULGARIA -> 3
- SPAIN -> 3
'''
