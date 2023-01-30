def triangle_area(base, height):
  area = (base * height) / 2
  if str(area).split('.')[1] == '0':
    return int(area)
  return f'{area:.12}'


a, b = [float(input()) for _ in range(2)]
print(triangle_area(a, b))


'''
input:
3
4
output:
6
'''