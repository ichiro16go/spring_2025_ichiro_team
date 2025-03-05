a, b, c, d, e = map(int, input().split())
S = [a, b, c, d, e]
ans = "No"

for i in range(4):
    S[i], S[i + 1] = S[i + 1], S[i]
    if S == sorted(S):
        ans = "Yes"
    S[i], S[i + 1] = S[i + 1], S[i]

print(ans)