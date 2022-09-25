m=int(input())
n=int(input())
a=[[0]*(m+1) for q in range(n)]
for i in range(n):
    s=input()
    l=len(s)
    k,z=0,0
    for j in range(l):
        if s[j]!=" ":
            a[i][k]=int(s[j])
            z+=a[i][k]
            k+=1
    a[i][m]=z
mx,f=a[0][m],0
for t in range (n):
	if a[t][m]>mx:
		mx=a[t][m]
		f=t
print(f+1)	
print(mx)	
print(a)