import re

c, t = list(input())
txt = [x for x in iter(input, 'end')]

regex = r"(^[A-Z])(.+)(\.|!|\?)$"
matches = []

for token in txt:
    match = re.findall(regex, token)
    if match:
        words = re.findall(r"\w+", token)
        for word in words:
            if word.count(c) >= int(t):
                matches.append(word)

print(", ".join(matches))

'''
input:
l2
This will, likely be a funny feeling, Laslo.
Will you come to my playlife ;)?
end
output:
will, likely, Will, playlife
'''
