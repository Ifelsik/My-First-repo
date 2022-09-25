x=1.28402542# 0 < x < 2
s=0
for i in range (1,1001):
	if i%2==0:
		k=-1
	else:
		k=1
	s+=k*1/i*(x-1)**i
print(s)