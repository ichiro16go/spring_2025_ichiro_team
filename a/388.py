N, D = map(int, input().split())
T = []
L = []

for i in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)

for k in range(1, D + 1):
    max_weight = 0
    for i in range(N):
        new_length = L[i] + k
        weight = T[i] * new_length
        if weight > max_weight:
            max_weight = weight
    print(max_weight)