N, S = map(int, input().split())
A = list(map(int, input().split()))
minumuization=False
can=False

# DがAの最小値より小さくないか調べる
if min(A)>S:
    minumuization=True
if minumuization==False :    
    j=0
    B=A+A
    C=0
    amari=S%sum(A)
    for i in range(len(B)):
       C+=B[i]
       while C>amari:
           C-=B[j]
           j+=1
       if C==amari:
           can=True
           
    

# if(minumuization==False):    
#     C=A+A
#     for i in range(N):
#         for j in range(N):
#             # print('Aiから', i+1,'Ajまで',i+j+2)
#             summary=sum(C[i:i+j+2])
#             # print(summary)
#             if S%sum(A)==summary:
#                 can=True

if can==True:
    print("Yes")
else:
    print("No")