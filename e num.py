s=2
n=1
for i in range(1,1000):
	n=(i+1)*n
	s+=1/n
print('число e=',s)