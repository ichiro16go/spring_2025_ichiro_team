N=int(input())
A=list(map(int,input().split()))

def check(A):
    di={}
    l=0
    ans=0
    for i in range(len(A)//2):
        if A[2*i]==A[2*i+1]:
            a=A[2*i]
            if a in di:
                l=min(l+1,i-di[a])
            else:
                l+=1
                di[a]=i
        else:
            l=0
            di[a]={}
        ans=max(ans,2*l)
    return ans
ans=max(check(A),check(A[1:]))
print(ans)