import re

regex = r"([2-9]|10|[JKQA])([SHDC])"

matches = re.finditer(regex, input())
[print(str(match[0]), end=" ") for match in matches]

'''
input:
2S3S4S5S6S
output:
2S 3S 4S 5S 6S
'''
