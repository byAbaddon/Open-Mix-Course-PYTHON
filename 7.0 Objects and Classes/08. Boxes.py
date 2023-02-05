class Boxes:
    def __init__(self, ul, ur, bl, br):
        self.ul = ul
        self.ur = ur
        self.bl = bl
        self.br = br

    def distance(self, ):
        x1, y1 = map(int, self.ul)
        x2, y2 = map(int, self.ur)
        x3, y3 = map(int, self.bl)
        x4, y4 = map(int, self.br)
        f_point = (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
        s_point =(((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5)
        return int(f_point), int(s_point)

    def perimeter(self, width, height):
        return f'Perimeter: {2 * width + 2 * height}'

    def area(self, width, height):
        return f'Area: {width * height}'


lst = [x.split('|') for x in iter(input, 'end')]

for token in lst:
    u_l, u_r, b_l, b_r = [x.split(':') for x in token]
    box = Boxes(u_l, u_r, b_l, b_r)
    p1, p2 = box.distance()
    print(f'Box: {p1}, {p2}')
    print(box.perimeter(p1, p2))
    print(box.area(p1, p2))




'''
input:
0:2 | 2:2 | 0:0 | 2:0
-3:0 | 0:0 | -3:-3 | 0:-3
-2:2 | 2:2 | -2:-2 | 2:-2
end

output:
Box: 2, 2
Perimeter: 8
Area: 4
Box: 3, 3
Perimeter: 12
Area: 9
Box: 4, 4
Perimeter: 16
Area: 16
'''
