x=0.28402542# |x|<1
s=0
for i in range (1,101):
	if i%2==0:
		k=-1
	else:
		k=1
	s+=k*1/i*x**i
print(s)