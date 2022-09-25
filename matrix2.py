n=int(input())
a=[]
for i in range(n):
    s=input().split()
    for j in range (len(s)):
        s[j]=int(s[j])
    a.append(s)
c=0
for k in range(1,n):
    for l in range(0,k):
        if a[k][l]!=a[l][k]:
            c=1
            break
if c==0:
    print('yes')
else:
    print('no')
