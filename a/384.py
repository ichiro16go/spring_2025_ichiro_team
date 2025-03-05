N, c1, c2 = input().split()
N = int(N)  # Nを整数に変換
S = list(input())

for i in range(N):
    if S[i] != c1:
        S[i] = c2
print ("".join(S))