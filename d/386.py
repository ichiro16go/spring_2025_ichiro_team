N, M = map(int, input().split())

#W[y] <= B[y] かつ  W[x] <= B[x] という状況になったら、その時点でNoを出力する
coordinates = []
for i in range(M):
    y, x, c = input().split()
    coordinates.append([int(y), int(x), c])

coordinates.sort()
minimum_x = N+1
for y, x, c in coordinates:
    if c == "W":
        minimum_x = min(minimum_x, x)
    else:
        if minimum_x <= x:
            print('No')
            exit()
print('Yes')