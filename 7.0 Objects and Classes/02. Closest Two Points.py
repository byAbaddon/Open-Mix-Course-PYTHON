n = int(input())
points = [list(map(int, input().split())) for i in range(n)]
shortest_dist = float('inf')
closes_p1 = closes_p2 = ''

for i in range(n):
    for j in range(n):
        if i != j:
            dist = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            if dist < shortest_dist:
                shortest_dist = dist
                p1, p2 = points[i], points[j]
                closes_p1, closes_p2 = tuple(p1), tuple(p2)

print(f'{shortest_dist:.3f}\n{closes_p1}\n{closes_p2}')


'''
4
-1 6
1 6
-1 -20
1 -20

input:
4
3 4
6 8
2 5
-1 3
OUTPUT:
1.414
(3, 4)
(2, 5)

'''