m=int(input())
n=int(input())
a=[[0]*m for d in range(n)]
for i in range (n):
	s=input()
	l=len(s)
	k=0
	for j in range (l):
		if l%2==0:
			k+=1
	for h in range (k):
		a[i][h]=s[k]
print(a)		