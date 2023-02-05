left1, top1, width1, height1 = map(int, input().split())
left2, top2, width2, height2 = map(int, input().split())

if left1 >= left2 and top1 >= top2 and left1 + width1 <= left2 + width2 and top1 + height1 <= top2 + height2:
    print("Inside")
else:
    print("Not inside")