def nuber(n):
    sign = {n > 0: 'positive', n < 0: 'negative', n == 0: 'zero'}
    return f'The number {n} is {sign[True]}.'


print(nuber(int(input())))
