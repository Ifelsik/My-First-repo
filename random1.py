import random
a=[]
x1, x2= map(int,input('интервал в целых').split())
n=int(input())
for i in range(n):
	r=random.randint(x1, x2)
	if r not in a:
		print(r)
		a.append(r)
	else:
		continue
	
