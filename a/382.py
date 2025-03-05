N,D=map(int,input().split())
S=list(input())

def cockies(N,D,S):
    l=0
    for s in S:
        if s==".":
            l+=1
            
    ans=N-l+D
    return ans
print(cockies(D,S))