f=open('26-75.txt')
n=int(f.readline())
a,b=[],[]
for i in range(n):
    S=f.readline()
    s=S.split()
    a.append(int(s[0]))
    b.append(int(s[1]))
T=a[0]
Pmax=0
p_1=1
for i in range(1,n):
    p=i
    t=0
    for j in range(i):
        if a[i]>=b[j]:
            p-=1
    if p==1:
    	t+=a[i]-b[j]
    	if p_1==1:
    		t+=b[j]-a[j]
    if p==2 and p_1==1:
        t+=a[i]-a[i-1]
    p_1=p
    T+=t
    if p>Pmax:
        Pmax=p
print(Pmax, T)
            
            
            
            
