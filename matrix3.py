q=input().split()
a=[]
m=int(q[len(q)-1])
for i in range(int(q[len(q)-2])):
    s=input().split()
    z=0
    if len(s)==m:
        for j in range (len(s)):
            s[j]=int(s[j])
            z+=s[j]
        s.append(z)
        a.append(s)
mx=a[0][m]
t=0
for k in range(int(q[len(q)-2])):
    if a[k][m]>mx:
        mx=a[k][m]
        t=k
print(mx)
print(t)

