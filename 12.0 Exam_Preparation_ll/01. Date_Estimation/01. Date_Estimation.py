import datetime

exam_date = datetime.datetime(2018, 8, 26)
current_date = datetime.datetime(*map(int, input().split('-')))
res = exam_date - current_date

if res.days == 0:
    print('Today date')
elif res.days > 0:
    print('Passed')
else:
    print(f'{abs(res.days) + 1} days left')

'''
input:
2021-08-26

output:
1097 days left
'''
