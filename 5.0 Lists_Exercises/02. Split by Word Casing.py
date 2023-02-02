txt = input()
regex = (',',';', ':', '. ', '!', '(', ')', '"', "'", '\\', '/', '[', ']',"''",'  '," .",'.')
for r in regex:
    txt = txt.replace(r, ' ')
lower_case = []
upper_case = []
mixed_case = []

for word in txt.split():
    if word.islower() and word.isalpha():
        lower_case.append(word)
    elif word.isupper() and word.isalpha():
        upper_case.append(word)
    else:
        mixed_case.append(word)

print('Lower-case:', ', '.join(lower_case))
print('Mixed-case:', ', '.join(mixed_case))
print('Upper-case:', ', '.join(upper_case))



'''
input:
Learn programming at SoftUni: Java, PHP, JS, HTML 5, CSS, Web, C#, SQL, databases, AJAX, etc.
output:
Lower-case: programming, at, databases, etc
Mixed-case: Learn, SoftUni, Java, 5, Web, C#
Upper-case: PHP, JS, HTML, CSS, SQL, AJAX
'''
