from re import findall    #TODO: WTF?

regex = r"https:\/\/github.com\/([A-Za-z0-9\-]+)\/([A-Za-z\-_]+)\/commit\/((?:\d|[a-f]){40}),(.+?),(\d+),(\d+)"
#regex = r"https://github.com/([a-zA-Z0-9-]+)/([a-zA-Z0-9_-]+)/commit/([a-fA-F0-9]{40}),(.+?),(\d+),(\d+)"
#regex = r"\bhttps:\/\/github\.com\/(?P<name>[A-Za-z0-9-]+)\/(?P<repo>[A-za-z-_]+)\/commit\/(?P<hash>[a-fA-F0-9|10]{40})\,(?P<message>[^\n].*)\,(?P<add>[\d]+)\,(?P<del>[\d]+)\b"
obj = {}

for line in [x for x in iter(input, "git push")]:
    matches = findall(regex, line)
    if matches:
        n, r, h, m, a, d = matches[0]
        obj.setdefault(n, {}).setdefault(r, []).append([h, m, a, d])

sort_lst_obj = sorted(obj.items(),key=lambda x: (x[0], x[1]))

for user in sort_lst_obj:
    total_add = total_del = 0
    print(user[0] + ':')
    for repo ,commits in user[1].items():
        print(' ',repo + ':')
        for c in commits:
            print("    commit " + c[0] + ": " + c[1] + " (" + c[2] + " additions, " + c[3] + " deletions)")
            total_add += int(c[2])
            total_del += int(c[3])
        print("\tTotal: " + str(total_add) + " additions, " + str(total_del) + " deletions")

'''
input:
https://github.com/gosho/http-parser/commit/f17c563aed112dabbdbe977fcdb88772be7d85eb,general fixes,14,3
https://github.com/pesho-1232/db-checker/commit/5ca49ccc157c98af2c71391223e4b254ee327134,fix SELECT statement,9,19
https://github.com/gosho/http-parser/commit/1f0abbdf5006b4a88aed1b72f9a937b35a5126dc,One does not simply merge into master,1,15
https://github.com/stamat4o/hackertools/commit/ddb473ab0304e5e843983da8b26925dbb3495afa,another big bag of changes,8,18
git push

output:     
gosho:
  http-parser:
    commit f17c563aed112dabbdbe977fcdb88772be7d85eb: general fixes (14 additions, 3 deletions)
    commit 1f0abbdf5006b4a88aed1b72f9a937b35a5126dc: One does not simply merge into master (1 additions, 15 deletions)
    Total: 15 additions, 18 deletions
pesho-1232:
  db-checker:
    commit 5ca49ccc157c98af2c71391223e4b254ee327134: fix SELECT statement (9 additions, 19 deletions)
    Total: 9 additions, 19 deletions
stamat4o:
  hackertools:
    commit ddb473ab0304e5e843983da8b26925dbb3495afa: another big bag of changes (8 additions, 18 deletions)
    Total: 8 additions, 18 deletions
'''
