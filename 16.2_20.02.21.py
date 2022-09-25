def F(n):
	if n<=3:
		return n
	elif n%2==0:
		return F(n-1)+2*F(n/2)
	else:
		return F(n-1)+F(n-3)
i=1
while F(i)<100000000:
	i+=1
print(i-1)