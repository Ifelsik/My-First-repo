a=list(map(int,input().split()))
b=sorted(a)
c=0
for i in range(len(b)):
	for j in range(i+1,len(b)):
		if b[i]==b[j]:
			b[j]="*"
			c=1
	if c==0:
		b[i]="*"
	c=0
for k in range(len(b)):
		if b[k]!="*":
			print(b[k], end=" ")
		