def F(n):
	if n>30:
		return n*n+5*n+4
	elif n%2==0:
		return F(n+1)+3*F(n+4)
	else:
		return 2*F(n+2)+F(n+5)
c=0
for i in range (1,1001):
	y=F(i)
	k=0
	while y>0:
		k+=y%10
		y=y//10
	if k==28:
		c+=1
print(c)