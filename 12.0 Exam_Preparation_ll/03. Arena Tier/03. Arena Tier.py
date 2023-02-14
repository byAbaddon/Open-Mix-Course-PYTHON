obj = {}
for token in [x.split(' -> ') for x in iter(input, 'Ave Cesar')]:
    if len(token) != 1:
        name, skill, pts = token
        pts = int(pts)
        if name not in obj:
            obj[name] = {skill: pts}
        else:
            if skill not in obj[name]:
                obj[name].update({skill: pts})
            else:
                if pts > obj[name][skill]:
                    obj[name][skill] = pts
    else:  # battle
        f_w, _, s_w = token[0].split()
        try:
            if obj[f_w] and obj[s_w]:
                f_all_tech = [x for x in obj[f_w].keys()]
                for tech in f_all_tech:
                    if tech in obj[s_w]:
                        if obj[f_w][tech] > obj[s_w][tech]:  # if equal ???
                            obj.pop(s_w)
                        else:
                            obj.pop(f_w)
        except:
            continue

sorted_obj = sorted(obj.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for key, value in sorted_obj:
    print(f"{key}: {sum(value.values())} skill")
    sort_val_point = sorted(dict(value).items(), key=lambda x: -x[1])
    for technique, points in sort_val_point:
        print(f"- {technique} <!> {points}")

'''
input:
Pesho -> BattleCry -> 400
Gosho -> PowerPunch -> 300
Stamat -> Duck -> 200
Stamat -> Tiger -> 250
Ave Cesar

output:
Stamat: 450 skill
- Tiger <!> 250
- Duck <!> 200
Pesho: 400 skill
- BattleCry <!> 400
Gosho: 300 skill
- PowerPunch <!> 300
'''
