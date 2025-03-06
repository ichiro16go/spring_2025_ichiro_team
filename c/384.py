a=list(map(int,input().split()))
b=['A','B','C','D','E']
s=[]
t=[]
for i in range(5):
    s.append(a[i])
    t.append(b[i])
    for j in range(i+1,5):
        s.append(a[i]+a[j])
        t.append(b[i]+b[j])
        for k in range(j+1,5):
            s.append(a[i]+a[j]+a[k])
            t.append(b[i]+b[j]+b[k])
            for l in range(k+1,5):
                s.append(a[i]+a[j]+a[k]+a[l])
                t.append(b[i]+b[j]+b[k]+b[l])
x=sorted(s,reverse=True)
print('ABCDE')
for r in range(30):
    for w in range(len(s)):
        if x[r]==s[w]:
            print(t[w])
            del s[w]
            del t[w]
            break
    