from itertools import combinations


N, K = map(int, input().split())
A = list(map(int, input().split()))

max_XOR=0
xor_A=0
# A全体のxor計算
for a_i in A:
    xor_A^=a_i
# print(xor_A)

defo=0
if K*2>N:
    defo=xor_A
    K=N-K
for k in combinations(A,K):
        xor_i=defo
        for k_i in k:
            xor_i^=k_i
        max_XOR=max(max_XOR ,xor_i)
print(max_XOR)
    
# kがNの半分より大きければ、最小の組み合わせを出して、xorA-minXorすればいい
# if K*2>N:
#     min_XOR=0
#     L=N-K
#     for l in combinations(A,L):
#         xor_i=0
#         for l_i in l:
#             xor_i^=l_i
#         min_XOR=min(min_XOR,xor_i)
#     print(min_XOR)
#     print(xor_A^min_XOR)
# else:       
#     for k in combinations(A,K):
#         xor_i=0
#         for k_i in k:
#             xor_i^=k_i
#         max_XOR=max(max_XOR ,xor_i)
#     print(max_XOR)


#K=2で考える
# for i in range(N):
#     for j in range(N):
#         xor=A[i]^A[j]
#         if i!=j and xor>max_XOR:
#             max_XOR=xor
# print(xor)