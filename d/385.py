from collections import defaultdict
from sortedcontainers import SortedList


n, m, Sx, Sy = map(int, input().split())
x = defaultdict(SortedList)
y = defaultdict(SortedList)


for _ in range(n):
    x_i, y_i = map(int, input().split())
    x[x_i].add(y_i)
    y[y_i].add(x_i)
print(x,y)

ans = 0
for _ in range(m):
    direction, count = input().split()
    c = int(count)
    if direction == "U":
        
        list_house_Sx = x[Sx].irange(Sy, Sy + c)
        data = [(Sx, l_i) for l_i in list_house_Sx]
        # print("data",data)
        Sy += c
    elif direction == "D":
        list_house_Sx = x[Sx].irange(Sy - c, Sy)
        data = [(Sx, l_i) for l_i in list_house_Sx]
        # print("data",data)
        Sy -= c
    elif direction == "R":
        list_house_Sy = y[Sy].irange(Sx, Sx + c)
        data = [(l_i, Sy) for l_i in list_house_Sy]
        # print("data",data)
        Sx += c
    else:
        list_house_Sy = y[Sy].irange(Sx - c, Sx)
        data = [(l_i, Sy) for l_i in list_house_Sy]
        # print("data",data)
        Sx -= c

    ans += len(data)
    for x_i, y_i in data:
        x[x_i].discard(y_i)
        y[y_i].discard(x_i)

print(Sx, Sy, ans)

